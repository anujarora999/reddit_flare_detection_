import pandas as pd
import io
import nltk
import random
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

from pre_functions import stemming


df = pd.read_csv('test_stopwords.csv')
df.fillna("")
title= df["title"].tolist()
body= df["body"].tolist()
comment = df["comments"].tolist()
t_remove_stem= stemming(title)
b_remove_stem = stemming(body)
c_remove_stem =  stemming(comment)
"""for c in comment:
	val = stemming(c)
	print(val)
	c_remove_stem.append(val)"""
#c_remove_stem = stemming(c_remove)
#print(t_remove_stem)
#print("---------------------------------")
#print(b_remove_stem)
t1 = pd.DataFrame(t_remove_stem)
b1 = pd.DataFrame(b_remove_stem)
c1 = pd.DataFrame(c_remove_stem)
df["title"] = t1
df["body"] = b1
df["comments"] = c1
df.to_csv("preprocessed.csv")




