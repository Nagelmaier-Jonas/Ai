#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy as sp
nlp = sp.load("en_core_web_sm")
import pandas as pd


# In[10]:


covid19_faqs = pd.read_csv("covid_faq.csv")
covid19_faqs


# #### 6.1 Implementieren Sie die Funktion calculate_similarity, die die Ähnlichkeit zweier Dokumente bestimmt und retourniert. Testen Sie deren Funktionsweise mit den COVID19-FAQs3. Ziel ist es, die beste Antwort zu finden. Ermitteln Sie hierzu die Ähnlichkeiten der Suchanfrage zu den gegebenen Fragen im Dataset und retournieren Sie jene Antwort, deren Frage am ehesten zur Suche passt

# In[11]:


def calculate_similarity(doc1, doc2):
    return doc1.similarity(doc2)

def find_best_answer(search_query_token, df_faq_data):
    # get row from dataframe with the highest similarity to search_query
    # return the answer of that row
    best_answer = ""
    best_similarity = -1
    for index, row in df_faq_data.iterrows():
        similarity = calculate_similarity(search_query_token, nlp(row["questions"]))
        if similarity > best_similarity:
            best_similarity = similarity
            best_answer = row["answers"]
    return best_answer

search_query = nlp("Will hot weather stop the outbreak of the virus?")

answer = find_best_answer(search_query, covid19_faqs)

print(answer)

