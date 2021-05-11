# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:56:09 2020

@author: Dell
"""
import os
import nltk
import nltk.corpus
import nltk
from nltk.util import ngrams
from nltk import word_tokenize
from nltk import sent_tokenize
import matplotlib.pyplot as plt

#print(os.listdir(nltk.data.find("corpora")))

from nltk.corpus import brown
print(" <<<<<<< james brown >>>>>>>",brown.words())


# hamlet = nltk.corpus.gutenberg.words("shakespeare-hamlet.txt")



data = open("albert.txt",errors='ignore')
# read the data
data = data.read()
# sentences tokenize
sent = sent_tokenize(data)
# word tokenize
words = word_tokenize(data)

from nltk.probability import FreqDist
fdist = FreqDist()

for word in words:
    fdist[word.lower()]+=1
print(fdist["space"])

fdishMost = fdist.most_common(10)
print(fdishMost)

from nltk.tokenize import blankline_tokenize
AIblank = blankline_tokenize(data)
print(len(AIblank))
print(AIblank[2])


from nltk.util import bigrams, trigrams, ngrams
string = "i have to write any code on my own, cause of by this way it is not helpful."
quarterToken = nltk.word_tokenize(string)
print("<<<<<< word tokenize >>>>>\n ",quarterToken)

biagram = list(nltk.bigrams(quarterToken))
print("<<<<<< biagrammm >>>>>>>\n",biagram)

triagram = list(nltk.trigrams(quarterToken))
print("<<<<< trigram >>>>>>>\n",triagram)

ngramm = list(nltk.ngrams(quarterToken, 4))
print("<<<<<< ngram N = 4 >>>>>> \n",ngramm)




