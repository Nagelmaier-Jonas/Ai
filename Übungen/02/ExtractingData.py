#!/usr/bin/env python
# coding: utf-8

# In[1]:


import PyPDF2 as pypdf
with open('schachnovelletext13.pdf', 'rb') as pdf:
    reader = pypdf.PdfFileReader(pdf)
    # Doc-Info ausgeben
    print(reader.documentInfo)
    # Anzahl der Seiten ausgeben
    print(reader.numPages) 


# In[2]:


with open('schachnovelletext13.pdf', 'rb') as pdf:
    info = reader.getDocumentInfo()
    author = info.author
    producer = info.producer
    title = info.title
    print(f"Author: \t{author}\nProducer: \t{producer}\nTitle: \t\t{title}")


# In[3]:


with open('schachnovelletext13.pdf', 'rb') as pdf:
    reader = pypdf.PdfFileReader(pdf)
    print(reader.getPage(0).extractText())


# In[4]:


with open('schachnovelletext13.pdf', 'rb') as pdf:
    reader = pypdf.PdfFileReader(pdf)
    for i in range(reader.getNumPages()):
        print(reader.getPage(i).extractText())


# In[5]:


with open('schachnovelletext13.pdf', 'rb') as pdf:
    list = []
    reader = pypdf.PdfFileReader(pdf)
    for i in range(reader.getNumPages()):
        list.append(reader.getPage(i).extractText())
    for i in list:
        print(i)


# In[7]:


# Bibliotheken laden
import urllib.request as urllib2
from bs4 import BeautifulSoup
# Website laden
response = urllib2.urlopen('https://www.htlkrems.ac.at')
html_doc = response.read()
# Das BeautifulSoup Object soup repräsentiert das „geparste“ HTML-Dokument
soup = BeautifulSoup(html_doc, 'html.parser')
# Das „geparste“ HTML-Dokument formatieren, sodass jeder Tag bzw. Textblock
# in einer separaten Zeile ausgegeben wird
strhtm = soup.prettify()
# Ein paar Zeilen ausgeben
list = soup.find_all('a')
print(f"Hyperlink {len(list)}")
for i in list:
    print(i)


# In[8]:


with open('schachnovelletext13.pdf', 'rb') as pdf:
    list = []
    reader = pypdf.PdfFileReader(pdf)
    page = reader.getPage(0)
    print(page.extractText())
    pypdf.py > word.docx


# In[ ]:




