#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import praw
import json
from flask import request
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import pickle

client_id = "LoffJKJOYt2vYg"
client_secret = "mUy-jpJ6nCUxPRj5rE7_qttqGqE"
user_agent= "Reddit Flare detection"
username = "pragya2211"
password = "Pragya2211!"

reddit = praw.Reddit(client_id = client_id,client_secret=client_secret,
                    user_agent = user_agent,username= username,
                     password=password)










# In[ ]:


def remove_stopwords(text):
    for w in text:
        if w == "\n":
            w= ""
    text_tokens = word_tokenize(text)
    w_sw = [word for word in text_tokens if not word in stopwords.words()]
    return w_sw


ps= PorterStemmer()
def stemming(text):
    lis = []
    t = str(text)
    aux_l = ""
    words = []
    for w in text:
        rootword = ps.stem(w)
        rootword = str(rootword)
        aux_l = aux_l+ rootword+ " "
    lis.append(aux_l)
    return lis


# In[ ]:

def actual(url):
    submission = reddit.submission(url = url)
    tr = submission.link_flair_text
    return tr


def predict(url):
    s = ""
    submission = reddit.submission(url=url)
    #print(submission.title)
    posts = {"title":[], "body":[], "comments": [],"combine": []}
    posts["title"] = submission.title
    posts["body"] = submission.selftext
    comment_list = []
    submission.comments.replace_more(limit = 0)
    for comment in submission.comments:
        comment_list.append(comment.body)
    posts["comments"] = comment_list
    c_remove = []
    for i in posts["comments"]:
    	c = remove_stopwords(i)
    	c_remove.append(c)
    t_remove = remove_stopwords(posts["title"])
    b_remove = remove_stopwords(posts["body"])
    posts["title"] = stemming(t_remove)
    posts["body"] = stemming(b_remove)
    posts["comments"] = []
    for i in c_remove:
    	a = stemming(i)
    	posts["comments"].append(a)
    #print(posts["title"])
    #posts["comments"] =  stemming(c_remove)
    if(posts["comments"] != []):
        posts["combine"] = posts["title"]+ posts["body"]+ posts["comments"][0]
    else:
        posts["combine"] = posts["title"]+ posts["body"]
    loaded_model = pickle.load(open("finalized_model.sav", 'rb'))
    return loaded_model.predict(posts['combine'])[0]


# In[ ]:

"""print("Enter a url")
url = "https://www.reddit.com/r/india/comments/g1qttv/watch_moradabad_some_people_pelted_stones_at/"
print(predict(url))
print(actual(url))"""

