#!/usr/bin/env python
# coding: utf-8

# In[3]:


import nltk as nl
import spacy as sp
nlp = sp.load('en_core_web_sm')
nl.download('averaged_perceptron_tagger')


# #### 3.2.1 Extrahieren Sie alle Hauptwörter sowie Eigennamen und speichern Sie diese in einer Liste. Ermitteln Sie außerdem die Anzahl der Elemente. Arbeitsgrundlage bildet die Job Description3 der letzten Übung. Duplikate und Stoppwörter sind zulässig. Ergebnisse: Spacy: 527, NLTK: 515

# In[4]:


job_desc = open('dataScientistJobDesc.txt', encoding="utf-8").read()
job_desc_tokens = nl.word_tokenize(job_desc)
words = [t for t in nl.pos_tag(job_desc_tokens) if t[1][:2] == 'NN']
len(words)


# In[5]:


job_desc_tokens_sp = nlp(job_desc)
nouns = [token for token in job_desc_tokens_sp if token.pos_ == 'PROPN' or token.pos_ == 'NOUN']
len(nouns)


# #### 3.2.2 Wir sind an der Häufigkeitsverteilung der Wortklassen interessiert. Ermitteln Sie die Anzahl der Substantive, Verben etc. Gesucht ist folgendes Ergebnis:
# 
# ##### {'NOUN': 386, 'VERB': 174, 'PUNCT': 149, 'PROPN': 141, 'ADP': 108, 'DET': 104, 'ADJ': 96, 'SPACE': 63, 'CCONJ': 54, 'AUX': 43, 'PRON': 43, 'ADV': 41, 'PART': 36, 'SCONJ': 15, 'NUM': 8, 'SYM': 6, 'INTJ': 1, 'X': 1}

# In[6]:


from collections import Counter


# In[7]:


pos = [t.pos_ for t in job_desc_tokens_sp]
counted_pos = Counter(pos)
dict(counted_pos.most_common())


# ####  3.2.3 Welches Wort kommt am häufigsten vor in dem Text?

# In[8]:


words = [t.text for t in job_desc_tokens_sp]
counted_words = Counter(words)
counted_words.most_common(1)[0][0]

