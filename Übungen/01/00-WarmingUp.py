#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd


# ## 0.1 - Movie-Dataset laden
#  Erstellen Sie das Jupyter-Notebook (JN) 00-WarmingUp und laden Sie das referenzierte Movie-Dataset1. Über welche Dimensionalität verfügt das Movie-Dataset bzw. das erstellte DataFrame?

# In[25]:


movie_df = pd.read_csv('movie.csv')


# In[26]:


movie_df.shape


# ## 0.2 - Ausgabe
# Generieren Sie nachfolgende JN-Ausgabe und ersetzen Sie die Platzhalter (siehe „?“) mit den fachspezifischen Bezeichnern.

# In[27]:


movie_df


# In[28]:


### Row, Column-Label, Auslassungspunkte, index, column, NaN-Value, float-value


# ## 0.3 - Movie-Title Series
# Selektiert man eine Spalte (z.B. movie_title) des erstellten Movie-DataFrames, ist das Ergebnis vom Typ Series. Treten Sie den Beweis an!
# Mögliche JN-Ausgabe:
# 
# > <class 'pandas.core.series.Series'>

# In[29]:


type(movie_df['movie_title'])


# ## 0.4 - DataFrame Manipulation
# Sicherlich wissen Sie noch, dass man DataFrames manipulieren kann. Fügen Sie die Spalte „has_seen“ mit dem Initialwert „0“ hinzu

# In[30]:


movie_df['has_seen'] = 0
movie_df


# ## 0.5 - Erstellung director_actor_facebook_likes - Spalte
# ### a) an der Gesamtanzahl der Director- und Actor_{1,2,3}-Likes interessiert.
# Um nicht jedes Mal die Summe über alle bilden zu müssen, empfiehlt sich mit „director_actor_facebook_likes“ eine weitere Spalte, die die Summe der definierten Likes je Film aufweist. Bilden Sie diese.

# In[31]:


movie_df['director_actor_facebook_likes'] = movie_df['actor_1_facebook_likes'] + movie_df['actor_2_facebook_likes'] + movie_df['actor_3_facebook_likes'] + movie_df['director_facebook_likes']
movie_df


# ### b) Wie man der exemplarischen Ergebnisdarstellung entnehmen kann, weist zumindest ein Eintrag den Wert „NaN“ auf. Was ist die Ursache?

# In[32]:


movie_df['director_actor_facebook_likes'].isna().sum()


# ###  c) finden Sie heraus, um wie viele Einträge es tatsächlich handelt und eliminieren Sie
# ### d) das Problem, indem Sie die betroffenden Felder des Datasets auf „0“ setzen.

# In[33]:


movie_df['director_actor_facebook_likes'] = movie_df['director_actor_facebook_likes'].fillna(0)
movie_df['director_actor_facebook_likes']


# ### 0.6 - Film Kostenspieligkeit
#  Es stellt sich die Frage, ob ein Film, dessen Produktion (vgl. Budget) 22 Millionen beträgt, kostspielig ist oder nicht. Wie könnte man das herausfinden?

# In[34]:


if movie_df['budget'].mean() > 22000:
    print('kostenspielig')
else:
    print('nicht kostenspielig')


# ## 0.7
# ### a) Datensatz als Plain Text laden

# In[35]:


spam_df = pd.read_csv('spam.csv')
spam_df


# ## b)  Fügen Sie eine weitere Spalte hinzu, die die Gesamtlänge der jeweiligen Nachricht aufweist

# In[36]:


spam_df['length'] = spam_df['v2'].str.len()
spam_df

