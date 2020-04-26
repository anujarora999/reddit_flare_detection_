import pandas as pd
import io
import nltk
import random
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from pre_functions import remove_stopwords







df = pd.read_csv('testset.csv')
df.fillna("")
title= df["title"].tolist()
body= df["body"].tolist()
comment = df["comments"].tolist()
#print("-----------------")
#print(comment)

t_remove = remove_stopwords(title)
b_remove = remove_stopwords(body)
c_remove = remove_stopwords(comment)

#print(t_remove)
#print(b_remove)
df["title"] = t_remove
df["body"] = b_remove
df["comments"] = c_remove
df.to_csv("test_stopwords.csv")
