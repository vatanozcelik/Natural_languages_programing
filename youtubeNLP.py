# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 08:08:22 2020

@author: Dell
"""

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
ps = PorterStemmer()

ex = "hello Mr. Smith, how are you doing today? the Weather is great and python is great."
stopwords = set(stopwords.words("english"))

# print(sent_tokenize(ex))
# print(word_tokenize(ex))

words = word_tokenize(ex)

'''
filtered = []

for i in words:
    if i not in stopwords:
        filtered.append(i)
'''

filtered = [i for i in words if not i in stopwords]
print(filtered)
example = ["python","pythoner","pythoning","pythoned","pythonly"]
newText = "it is very important to be pythonly while you are pythoning with python. all pythoners have pythoned"
wordss = word_tokenize(newText)

for w in wordss:
    print(ps.stem(w))

