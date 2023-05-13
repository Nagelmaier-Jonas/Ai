#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer


# ## Datenaufbereitung
# 1. Laden Sie das *spam.csv*-File in das DataFrame *data*
# 2. Ändern Sie die Spaltenbezeichner: v1 -> **target** und v2 -> **message**
# 3. Transfomieren Sie den Inhalt der Spalte *message* in Kleinbuchstaben
# 4. Entfernen Sie Stoppwörter
# 5. Führen Sie Stemming und Lemmatisierung durch

# In[2]:


#1 Daten laden
data = pd.read_csv("spam.csv" , encoding='latin-1')

#2 Spaltenbezeichner ändern
data = data.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)
data.columns = ["target", "message"]

#3 Kleinbuchstaben
data['message'] = data['message'].str.lower()

#4 Stoppwörter entfernen
stop = stopwords.words('german')
data['message'] = data['message'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop]))

#5 Stemming und Lemmatisierung
stemmer = SnowballStemmer("german")
data['message'] = data['message'].apply(lambda x: ' '.join([stemmer.stem(word) for word in x.split()]))

data.head()


# Das Dataset *data* mithilfe von `train_test_split()` in Trainings- und Validierungsdaten aufteilen:

# In[3]:


train_x, valid_x, train_y, valid_y = train_test_split(data['message'], data['target'], test_size=0.3, random_state=42)
print("Check shape: ", train_x.shape, valid_x.shape)


# Die Antworten (*ham* o. *spam*) in 1 oder 0 umwandeln:

# In[4]:


encoder = preprocessing.LabelEncoder()
train_y = encoder.fit_transform(train_y)
valid_y = encoder.fit_transform(valid_y)

print("Encoder hat mit 0 und 1 zwei Klassen erkannt: ", encoder.classes_)
print("Die kodierten Antworten der Trainingsdaten: " , train_y)


# Vektorisierung der Daten mit TF-IDF. Mit der Größe von `max_features` kann experimentiert werden. Diese legt den Umfang des Vokabulars fest.

# In[5]:


vectorizer = TfidfVectorizer(analyzer='word', max_features=5000)
vectorizer.fit(data['message'])

print("Vektor mit 5000 Einträgen: ",  vectorizer.get_feature_names_out().shape)
print("Vokabular: ", vectorizer.get_feature_names_out())


# In[6]:


train_x_tfidf = vectorizer.transform(train_x)
valid_x_tfidf = vectorizer.transform(valid_x)
print("Check expected shape for train data: ", train_x_tfidf.shape)
print("Check expected shape for validation data: ", valid_x_tfidf.shape)


# Classifier trainieren und validieren:

# In[7]:


clf = naive_bayes.MultinomialNB(alpha=0.2)
# fit the training dataset on the classifier
clf.fit(train_x_tfidf, train_y)

# predict the labels on validation dataset
predictions = clf.predict(valid_x_tfidf)

# retrieve accuracy score
metrics.accuracy_score(predictions, valid_y)

