import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import praw
import pandas as pd
import datetime as dt
import logging
import numpy as np
from numpy import random
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import re
from bs4 import BeautifulSoup
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report
import pickle
import pymongo

flairs = ["Scheduled", "Politics", "Photography","Policy/Economy",
         "Sports","Non-Political","Science/Technology","Food",
            "Business/Finance","Coronavirus","Megathread","CAA-NRC","[R]eddiquette"]
#print(df.head())
#y = df["flair"]
#x = df.drop("flair", axis = 1)
#print(x)
#print(y)
#x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25)
#print(x_train)
#print(x_train.shape, x_test.shape)
#print(x_test)
#train = x_train.to_csv("train.csv")
#test = x_test.to_csv("test.csv")
'''Naive Bayees Classfier'''
def nb_classifier(X_train, X_test, y_train, y_test):
	from sklearn.naive_bayes import MultinomialNB
	nb = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB()),])
	nb.fit(X_train, y_train)
	y_pred = nb.predict(X_test)
	new_l = []
	"""for i in flairs:
					if(i in y_test):
						new_l.append(i)"""
	print("Results of Naive Bayes Classifier")
	print('accuracy ' + str(accuracy_score(y_pred, y_test)))
	print("Classification Report is: ")
	print(classification_report(y_test, y_pred,target_names=flairs))
	




def svm_classifier(X_train,X_test,y_train,y_test):
	from sklearn.linear_model import SGDClassifier
	svm = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', SGDClassifier()),])
	svm.fit(X_train, y_train)
	y_pred = svm.predict(X_test)
	new_l = []
	"""for i in flairs:
					if(i in y_test):
						new_l.append(i)"""

	print("Results of Support Vector Machine Classifier")
	print('accuracy ' + str(accuracy_score(y_pred, y_test)))
	print("Classification Report is: ")
	print(classification_report(y_test, y_pred,target_names=flairs))




def logreg_classifier(X_train,X_test,y_train,y_test):
	from sklearn.linear_model import LogisticRegression
	lgr = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', LogisticRegression()),])
	lgr.fit(X_train, y_train)
	new_l = []
	filename = 'finalized_model.sav'
	pickle.dump(lgr, open(filename, 'wb'))
	y_pred = lgr.predict(X_test)
	
	print("Results of Logistic Regression")
	print('accuracy ' + str(accuracy_score(y_pred, y_test)))
	print("Classification Report is: ")
	print(classification_report(y_test, y_pred,target_names=flairs))
	





def train_test(X,y):
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
	#nb_classifier(X_train, X_test, y_train, y_test)
	#svm_classifier(X_train, X_test, y_train, y_test)
	logreg_classifier(X_train, X_test, y_train, y_test)


#df = pd.read_csv('preprocessed.csv')
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['Midaas']
preprocess = db.preprocessed
df = pd.DataFrame(list(preprocess.find()))
df["flair"] = df["flair"].values.astype('U')
df["comments"] = df["comments"].values.astype('U')
df["title"] = df["title"].values.astype('U')
df["body"] = df["body"].values.astype('U')
fl = df["flair"].tolist()
com = df["comments"].tolist()
tit = df["title"].tolist()
bod = df["body"].tolist()
combined = (df["comments"]+ df["title"]+df["body"]).tolist()
#df = df.assign(combine = combined)
#com = df.combine
print("Flair Detection using Title as Feature")
train_test(tit,fl)
print("Flair Detection using Body as Feature")
train_test(bod,fl)
print("Flair Detection using Comments as Feature")
train_test(com,fl)
print("Flair Detection using Combined Features")
train_test(combined,fl) 
