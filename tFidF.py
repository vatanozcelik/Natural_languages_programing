# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 13:32:47 2020

@author: Dell
"""


# >>>>> t f    i d f <<<<<<<<
from sklearn.feature_extraction.text import TfidfVectorizer
# sentences for anaysis:
sentences = ['this is the first decument','this is the second decument']
#print(sentences[0],"\n",sentences[1],"\n")

# create an object:
vectorizer = TfidfVectorizer(norm=None)
# generating output for tf idf:
X = vectorizer.fit_transform(sentences).toarray()
# total words with their index in model:
print(vectorizer.vocabulary_)
print("\n")
# features:
print(vectorizer.get_feature_names())
print("\n")
# show the output
print(X)
