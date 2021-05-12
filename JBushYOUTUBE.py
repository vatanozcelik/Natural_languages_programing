# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 06:45:40 2020

@author: Dell
"""

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

trainText = "A malapropism also called a malaprop, acyrologia, or Dogberryism is the mistaken use of an incorrect word in place of a word with a similar sound, resulting in a nonsensical, sometimes humorous utterance. An example is the statement by baseball player Yogi Berra, Texas has a lot of electrical votes, rather than electoral votes. Malapropisms often occur as errors in natural speech and are sometimes the subject of media attention, especially when made by politicians or other prominent individuals. Philosopher Donald Davidson has said that malapropisms show the comple process through which the brain translates thoughts into language.Humorous malapropisms are the type that attract the most attention and commentary, but bland malapropisms are common in speech and writing."


customSentTokenizer = PunktSentenceTokenizer(trainText)
tokenized = customSentTokenizer.tokenize(trainText)

def processContent():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            #chunkGram = """Chunk: {<RB}"""
            print(tagged)
    
    except Exception as e:
        print(str(e))
        
processContent()
