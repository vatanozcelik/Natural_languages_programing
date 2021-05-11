# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 16:58:45 2020

@author: Dell
"""
import nltk
nltk.download()

# OPEN THE TEXT FILE :
textFile = open("TowardsNLP.txt")
# READ THE DATA :
text = textFile.read()
# DATATYPE :

print(type(text))
print("the text\n",text)
print("length of the text\n",len(text))

from nltk import sent_tokenize
from nltk import word_tokenize

# TOKENIZE THE TEXT BY SENTENCES :
sentences = sent_tokenize(text)
# how many sentences are there? :
print("<<<<< how many sentences >>>>>\n",len(sentences))
#print(sentences)

# tokenize the text with words :
words = word_tokenize(text)
# how many words are there? :
print("<<<<<<< length of words>>>>>>> \n",len(words))
# print words :
print("<<<<< word tokenize >>>>>\n",words)

# FIND THE FREQUENCY DISTRIBUTION :
# import required libraries :
from nltk.probability import FreqDist
fDisk = FreqDist(words)
# print 10 most common words:
print("<<<<<<  10 most common words  <<<<<<\n",fDisk.most_common(10))

import matplotlib.pyplot as plt
fDisk.plot(10)

# REMOVE PUNCTUATION MARKS :
wordsNoPunc = []
# removing punctuation marks:
for w in words:
    if w.isalpha():
        wordsNoPunc.append(w.lower())
# print the words without punctuation marks:
print(">>>> words without punctuation marks ,. etc >>>> \n",wordsNoPunc)
# length
print("<<<<<< length of no punc >>>>>>\n",len(wordsNoPunc))

# frequency distrubution:
fDisk = FreqDist(wordsNoPunc)
print("<<<<< most common words >>>>\n",fDisk.most_common(10))
fDisk.plot(10)

# LIST OF STOPWORDS:
from nltk.corpus import stopwords
"""
stopwords = stopwords.words("english")
print(stopwords)


# empty list to store clean words :
cleanWords = []
for w in wordsNoPunc:
    if w not in stopwords:
        cleanWords.append(w)
print(cleanWords)
print("\n", len(cleanWords))

# Final Frequency destribution :
fDisk = FreqDist(cleanWords)
print(fDisk.most_common(10))

# plot the most common words on graph:
fDisk.plot(10)
"""
# library to form wordcloud:
from wordcloud import WordCloud
"""
#import matplotlib.pyplot as plt
wordcloud = WordCloud().generate(text)
# plot the wordcloud:
plt.figure(figsize=(12,12))
plt.imshow(wordcloud)
# to remove the axis value:
plt.axis("off")
plt.show() 

# Stemming: "study", studying, studied, studies...
# snowballstemmer support many languages
"""
from nltk.stem import SnowballStemmer
"""
# print languages supported
print(SnowballStemmer.languages)



# PoS tagging :
sentencess = "A very beautiful young lady is walking on the beach"
# tokenizing words :
tokenized = word_tokenize(sentencess)
for words in tokenized:
    taggedWordsss = nltk.pos_tag(tokenized)
print(taggedWordsss)


# chunking GRAMMER
GRAMMAR = "NP : {<DT>?<JJ>*<NN>} "

# creating a parser :
parser = nltk.RegexpParser(GRAMMAR)
# parsing text:
output = parser.parse(taggedWordsss)
print(output)
# to visualize :
output.draw()


# chinking grammer :
# We generally use chinking when we have a lot of unuseful data even after chunking
# and then we are going to exclude adjectives from it by using chinking
grammer = r NP: {<.*>+}
                  }<JJ>+{
                         
# creating parser :
parser = nltk.RegexpParser(grammer)                        
# parsing string :
OUTPUT = parser.parse(taggedWordsss)
print(OUTPUT)
# to visualize :
OUTPUT.draw()

# >>>>>>>> named entity recognition (NER) <<<<<<<<
# USE CASES: customer supprt, summarizing resumes ..
# 1 : binary = True, whether a particular entity is named entity or not.

# sentence for NER:
sente = "Mr. Smith made a deal on a beach of Switzerland near WHO."
# tekenizing words:
tokenizeWords = word_tokenize(sente)
# PoS tagging :
for w in tokenizeWords:
    taggedWordss = nltk.pos_tag(tokenizeWords)

print (taggedWordss)
# Named Entity Recognition:
NEG = nltk.ne_chunk(taggedWordss, binary=True)
print(NEG)
NEG = nltk.ne_chunk(taggedWordss, binary=False)
print(NEG)

# to visualize:
NEG.draw()
"""

# W   O   R   D   N   E   T 
## WordNet: to find maening of the words, synonyms, antonyms
from nltk.corpus import wordnet
"""
for words in wordnet.synsets("Happy"):
    print(words)

# for many different meaning:
for words in wordnet.synsets("Happy"):
    for lemma in words.lemmas():
        print(lemma)
    print("\n")

# all details for a word.
word = wordnet.synsets("mind")[0]
# checking the name:
print(word.name())
# checking definition:
print(word.definition())
# checking examples:
print(word.examples())

# all details for all meanings of word.
for word in wordnet.synsets("Fun"):
    print(word.name())
    print(word.definition())
    print(word.examples())
    
    for lemma in word.lemmas():
        print(lemma)
    print("\n")
# hypernyms gives us a more abstract term for a word.
word = wordnet.synsets("play")[0]
# find more abstract term:
print(word.hypernyms())

# hyponyms gives us a more specific term a word.
print(word.hyponyms())

# get a name only.
print(word.lemmas()[0].name())


"""

"""
# <<<<<<<    s y n o n y m s   and  a n t o n y m s >>>>>>>>>>>>
synonmys = []
antonyms = []

for words in wordnet.synsets("New"):
    for lemma in words.lemmas():
        synonmys.append(lemma.name())
        if lemma.antonyms():
            antonyms.append(lemma.antonyms()[0].name())
# print synonmys:
print(synonmys)
print("\n")
# print antonyms:
print(antonyms)
"""

"""
# finding similarity between words.
word1 = wordnet.synsets("go","n")[0]
word2 = wordnet.synsets("come","n")[0]
# checking similarity
print(word1.wup_similarity(word2))
# 0.234294


# >>>>>>>>> B A G   O F   W O R D S  <<<<<<<<<<<<
from sklearn.feature_extraction.text import CountVectorizer
# text for analysis:
sentences = ["Jim and Pam travelled by the bus:",
             "The train was late",
             "The flight was full. travelling by flight is expensive"]
# create an object:
cv = CountVectorizer()
# generating output for bag of words:
BOW = cv.fit_transform(sentences).toarray()
# total words with their index in model:
print(cv.vocabulary_)
print("\n")
# features:
print(cv.get_feature_names())
print("\n")
# show the output
print(BOW)


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

"""














                         
    