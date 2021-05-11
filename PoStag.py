# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 10:59:30 2020

@author: Dell
"""
import nltk
from nltk import word_tokenize
# PoS tagging :
sentencess = "A very beautiful young lady is walking on the beach"
# tokenizing words :
tokenized = word_tokenize(sentencess)
for words in tokenized:
    taggedWordsss = nltk.pos_tag(tokenized)
print(taggedWordsss)








