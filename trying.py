# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 14:23:21 2020

@author: Dell
"""

import nltk
from nltk.util import ngrams
from nltk import word_tokenize
from nltk import sent_tokenize
import matplotlib.pyplot as plt

data = open("albert.txt",errors='ignore')
# read the data
data = data.read()
# sentences tokenize
sent = sent_tokenize(data)
# word tokenize
words = word_tokenize(data)
# REMOVE PUNCTUATION MARKS :
wordsNoPunc = []
# removing punctuation marks:
for w in words:
    if w.isalpha():
        wordsNoPunc.append(w.lower())

# print the words without punctuation marks:
#print(">>>> words without punctuation marks ,. etc >>>> \n",wordsNoPunc)
# length
print("<<<<<< length of no punc >>>>>>\n",len(wordsNoPunc))

# LIST OF STOPWORDS:
from nltk.corpus import stopwords
stopwords = stopwords.words("english")
#print(stopwords)


# empty list to store clean words :
cleanWords = []
for w in wordsNoPunc:
    if w not in stopwords:
        cleanWords.append(w)
#print(cleanWords)
print("\n", len(cleanWords))

from nltk.probability import FreqDist
# Final Frequency destribution :
fDisk = FreqDist(cleanWords)
print(fDisk.most_common(10))

# plot the most common words on graph:
fDisk.plot(10)

# library to form wordcloud:
from wordcloud import WordCloud

#import matplotlib.pyplot as plt
wordcloud = WordCloud().generate(data)
# plot the wordcloud:
plt.figure(figsize=(12,12))
plt.imshow(wordcloud)
# to remove the axis value:
plt.axis("off")
plt.show() 

# Function to generate n-grams from sentences.
def extract_ngrams(cleanWords, num):
    n_grams = ngrams(cleanWords, num)
    return [ ' '.join(grams) for grams in n_grams]


print("2-gram: ", extract_ngrams(cleanWords, 2))


