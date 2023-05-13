#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow.keras.utils import to_categorical

def one_hot_encoding(sent, vocab):
    word_to_number = dict()
    for word_id in range(len(vocab)):
        word_to_number[vocab[word_id]] = word_id

    sent_numbers = []
    words = sent.split()
    for word in words:
        if word in word_to_number:
            sent_numbers.append(word_to_number[word])
        else:
            sent_numbers.append(-1)

    word_vectors = []
    for number in sent_numbers:
        if number >= 0:
            vector = to_categorical(number, num_classes=len(vocab))
            vector = list(vector)
            word_vectors.append(vector)

    return word_vectors


# In[3]:


vocab = ["Jim", "will", "learn", "NLP", "in", "future", "and", "like", "oranges"]
sent = "Jim will learn NLP in future."
word_vectors = one_hot_encoding(sent, vocab)
print(word_vectors)


# In[ ]:




