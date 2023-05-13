#!/usr/bin/env python
# coding: utf-8

# ### Imports

# In[1]:


import pandas as pd
import string as st
import nltk as nl
import spacy as sp
from nltk.tokenize import word_tokenize
nl.download('punkt')


# In[2]:


tweets=[
    'This is introduction to NLP',
    'It is likely to be useful, to people ',
    'Machine learning is the new electrcity',
    'There would be less hype around AI and more action going forward',
    'python is the best tool!','R is good langauage',
    'I like this book','I want more books like this'
]


# ### Konvertierung in Kleinbuchstaben

# In[3]:


tweets_lower = [t.lower() for t in tweets]

tweets_df = pd.DataFrame(tweets_lower,columns=['tweet'])
tweets_df


# ### Satzzeichen entfernen

# In[4]:


tweets_df['tweet'].str.replace('[{}]'.format(st.punctuation), '')


# ### Tokenisierung mit NLTK und split()

# In[5]:


text = "This is the first sentence. This is the second one."
list_of_words = text.split()
print(list_of_words)

text="Hello there! Welcome to the programming world."
print(word_tokenize(text)) #Satzzeichen werden als eigene Wörter erkannt


# ### Neue Spalte mit Tokenisierung

# In[6]:


tweets_df['tokenized'] = tweets_df['tweet'].apply(word_tokenize)
tweets_df


# ### Tokenisierung Data Scientist Job Description

# In[7]:


job_desc = open('dataScientistJobDesc.txt', encoding="utf-8").read()

job_desc_tokens = nl.word_tokenize(job_desc)
print(len(job_desc_tokens))

job_desc_tokens = list(set(job_desc_tokens))
print(len(job_desc_tokens))


# ### Tokenisierung mit Spacy

# #### Download en_core_web_sm:
# `python3 -m spacy download en_core_web_sm`

# In[8]:


job_desc = open('dataScientistJobDesc.txt', encoding="utf-8").read()

nlp = sp.load('en_core_web_sm')
job_desc_tokens = nlp(job_desc)
job_desc_tokens = [token.text for token in job_desc_tokens]
print(len(job_desc_tokens))

job_desc_tokens = list(set(job_desc_tokens))
print(len(job_desc_tokens))


# # Stoppwörter

# In[9]:


from nltk.corpus import stopwords
nl.download('stopwords')


# In[14]:


stop = stopwords.words('english')
stop

