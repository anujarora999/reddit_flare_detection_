import pandas as pd
import io
import nltk
import random
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

def remove_stopwords(text):
	for w in text:
		if w == "\n":
			w= " "
	words = [w for w in text if w not in stopwords.words("english")]
	return words

ps= PorterStemmer()

def stemming(text):
	lis = []
	for t in text:
		t = str(t)
		aux_l = ""
		words = []
		words = word_tokenize(t)
		for w in words:
			rootword = ps.stem(w)
			if(rootword.isalnum()):
				aux_l = aux_l+ rootword+ " "
		lis.append(str(aux_l))
	return lis