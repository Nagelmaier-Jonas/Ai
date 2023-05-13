#!/usr/bin/env python
# coding: utf-8

# # Pipeline

# In[23]:


import spacy as sp
import nltk
from nltk.corpus import stopwords


# ## Functions

# In[50]:


def to_lower(text):
    return text.lower()

def remove_url(text):
        print("remove_url: not implemented")
    
def remove_email(text):
        print("remove_email: not implemented")
        
def remove_punctuations(text):
    nlp = sp.load("en_core_web_sm")  # Load the English language model
    doc = nlp(text)  # Create a spacy document from the input text
    return "".join([token.text for token in doc if not token.is_punct])
    
def remove_stopwords(text):
    nlp = sp.load("en_core_web_sm")  # Load the English language model
    doc = nlp(text)  # Create a spacy document from the input text
    return " ".join([token.text for token in doc if not token.is_stop])


# In[51]:


def preprocess_text(text, keywords):
    for keyword in keywords:  # Iterate through the keywords list
        text = keyword(text)  # Apply the keyword function to the text
    return text  # Return the processed text
text = "This is some sample text with stopwords."
keywords = [to_lower, remove_punctuations, remove_stopwords]


# In[52]:


preprocessed_text = preprocess_text(text, keywords)
print(preprocessed_text)  # Output: "sample text stopwords"


# In[ ]:




