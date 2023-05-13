#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# # Extracting Data II – Regular Expressions 

# ## Einfache Suche nach Zahlen 

# In[2]:


p = re.compile("5")
print(p.findall("Für 5 Semmeln habe ich 3.90€ bezahlt.")) 


# In[3]:


p = re.compile("[1234567890]")
print(p.findall("Für 5 Semmeln habe ich 3.90€ bezahlt.")) 


# In[4]:


p = re.compile("[0-9]") 
print(p.findall("Für 5 Semmeln habe ich 3.90€ bezahlt.")) 


# In[5]:


## 3.1
p = re.compile("[0-9]\.[0-9][0-9][€$]") 
print(p.findall("Für 5 Semmeln habe ich 3.90€ bezahlt.")) 
print(p.findall("Für 5 Semmeln habe ich 3.90$ bezahlt.")) 


# In[6]:


## 3.2
p = re.compile(" [0-9][0-9][0-9] ")
print(p.findall("Für 5 Semmeln habe ich 3.90€ bezahlt."))
print(p.findall("Für 15 Semmeln habe ich 19.50$ bezahlt."))
print(p.findall("Für 150 Semmeln habe ich 190.50$ bezahlt."))

## Es werden nun nur 3stellige Zahlen berücksichtigt. 


# In[7]:


p = re.compile(" [0-9]+ ")
print(p.findall("Für 5 Semmeln habe ich 3.90€ bezahlt."))
print(p.findall("Für 15 Semmeln habe ich 19.50$ bezahlt."))
print(p.findall("Für 150 Semmeln habe ich 190.50$ bezahlt.")) 


# In[8]:


p = re.compile(" [0-9]+\.[0-9][0-9][€$] ")
print(p.findall("Für 5 Semmeln habe ich 3.90€ bezahlt."))
print(p.findall("Für 15 Semmeln habe ich 19.50$ bezahlt."))
print(p.findall("Für 150 Semmeln habe ich 190.50$ bezahlt.")) 


# In[9]:


p = re.compile(" [0-9]+\.[0-9]{2}[€$] ") 
print(p.findall("Für 5 Semmeln habe ich 3.90€ bezahlt."))
print(p.findall("Für 15 Semmeln habe ich 19.50$ bezahlt."))
print(p.findall("Für 150 Semmeln habe ich 190.50$ bezahlt.")) 


# In[10]:


## 3.3
p = re.compile(" [0-9]+[\.,][0-9]{2}[$€]? ")
print(p.findall("Für 5 Semmeln habe ich 3.90 bezahlt."))
print(p.findall("Für 15 Semmeln habe ich 19.50$ bezahlt."))
print(p.findall("Für 150 Semmeln habe ich 190,50$ bezahlt.")) 


# ## Einfache Suche nach Strings

# In[11]:


p = re.compile("Telefonnummer")
print(p.search("Meine Telefonnummer ist 0664 555 0 123. Ruf schnell an!")) 


# In[12]:


match = p.search("Meine Telefonnummer ist 0664 555 0 123. Ruf schnell an!")
print(match.span())
print(match.start())
print(match.end()) 


# ## 3.4 
# Die Methode re.finditer() funktioniert genauso wie die Methode re.findall(), mit dem Unterschied, dass sie einen Iterator zurückgibt, der Match-Objekte liefert, die dem Regex-Muster in einer Zeichenkette statt in einer Liste entsprechen.
# Wenn 0 oder mehr Zeichen am Anfang vom string mit dem Muster des regex Expression übereinstimmen, wird ein entsprechendes Match-Objekt zurückgegeben. Gibt None zurück, wenn die Zeichenkette nicht mit dem Muster übereinstimmt. Zu beachten ist, dass dies ein Unterschied zu einer 'zero-length match' ist.

# # Zusätzliche Regex-Syntax
# ## Oder-Operator 

# In[13]:


print(re.search("Frau|Herr", "Sehr geehrte Frau Musterfrau! Ich darf Sie darauf hinweisen, dass..."))
print(re.search("Frau|Herr", "Sehr geehrter Herr Mustermann! Ich darf Sie darauf hinweisen, dass...")) 


# ## Wildcard Operator

# In[14]:


re.findall(".und","Der Hund hat keinen Mund ")


# ## Bezeichner für den Anfang und das Ende 

# In[15]:


someText = ["a", "abc", "bac"]
for text in someText:
 print(re.findall("^a", text)) 


# ## Ausschluss von Zeichen 

# In[16]:


re.findall("[^ ]","Das ist ein Text mit Leerzeichen!") 


# ## 3.5 https://www.programiz.com/python-programming/regex durchlesen

# In[21]:


# 3.6
# zusätzlicher Import
import urllib
# Website laden
response = urllib.request.urlopen('https://www.htlkrems.ac.at')
html_doc = response.read().decode("utf-8")
p = re.compile("\w{1,}@\w{1,}.[a-zA-Z]{2,}")
print(p.findall(html_doc))


# In[22]:


import pandas as pd
data = p.findall(html_doc)
df = pd.DataFrame(data, columns=["E-Mail"])
df.to_csv('emails.csv', index=False)


# ## 3.7 IMDB

# In[26]:


from bs4 import BeautifulSoup
response = urllib.request.urlopen('https://www.imdb.com/chart/top')
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')

movies = {
    "title": [],
    "year": [],
    "rating": [],
}

for movie in soup.select('.lister-list tr'):
    movies["title"].append(movie.select_one('.titleColumn a').text)
    movies["year"].append(movie.select_one('.titleColumn span').text[1:-1])
    movies["rating"].append(movie.select_one('.imdbRating strong').text)

df = pd.DataFrame(movies)
df.head()


# In[ ]:




