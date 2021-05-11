# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 13:47:09 2020

@author: Dell
"""

from sklearn.metrics import jaccard_score

def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return float(len(s1.intersection(s2)) / len(s1.union(s2)))
list1 = ['dog', 'cat', 'cat', 'rat']
list2 = ['dog', 'cat', 'mouse', 'rat']
print(jaccard_similarity(list1, list2))






