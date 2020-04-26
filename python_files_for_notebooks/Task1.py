#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import praw
import json
from flask import request
import pandas as pd
import datetime


# In[ ]:


client_id = "LoffJKJOYt2vYg"
client_secret = "mUy-jpJ6nCUxPRj5rE7_qttqGqE"
user_agent= "Reddit Flare detection"
username = "pragya2211"
password = "Pragya2211!"


# In[ ]:


reddit = praw.Reddit(client_id = client_id,client_secret=client_secret,
                    user_agent = user_agent,username= username,
                     password=password)


# In[ ]:


subreddit = reddit.subreddit('india')
flairs = {"Scheduled":0, "Politics":0, "Photography":0,"Policy/Economy":0,"AskIndia":0,
         "Sports":0,"Non-Political":0,"Science/Technology":0,"Food":0,
            "Business/Finance":0,"Coronavirus":0,"Megathread":0,"CAA-NRC-NPR":0,"[R]eddiquette":0}



# In[ ]:
print("okay")

top_subreddit = subreddit.top()
top_subreddit = subreddit.top(limit=1500)
posts = {"url": [],"flair":[],"title" : [],"id": [],"score" : [],"body": [],"numberOfcomments":[], "created": [], "author" :[],"upvoteRatio": [],"comments": []}
c=0

"""for submission in top_subreddit:
    if submission.link_flair_text not in flairs:
        print(submission.link_flair_text)
        continue 
    flairs[submission.link_flair_text] = flairs[submission.link_flair_text]+1
    posts["flair"].append(submission.link_flair_text)
    posts["title"].append(submission.title)
    posts["id"].append(submission.id)
    posts["score"].append(submission.score)
    posts["body"].append(submission.selftext)
    posts["numberOfcomments"].append(submission.num_comments)
    posts["created"].append(submission.created)
    posts["author"].append(submission.author)
    posts["url"].append(submission.url)
    posts["upvoteRatio"].append(submission.upvote_ratio)
    comment_list = []
    submission.comments.replace_more(limit = 0)
    for comment in submission.comments:
        comment_list.append(comment.body)
    posts["comments"].append(comment_list)
    c=c+1 
print(c)"""



# In[ ]:


for submission in reddit.subreddit('india').search('flair:"Scheduled"', limit=250):
    #flairs[submission.link_flair_text] = flairs[submission.link_flair_text]+1
    posts["flair"].append(submission.link_flair_text)
    posts["title"].append(submission.title)
    posts["id"].append(submission.id)
    posts["score"].append(submission.score)
    posts["body"].append(submission.selftext)
    posts["numberOfcomments"].append(submission.num_comments)
    posts["created"].append(submission.created)
    posts["author"].append(submission.author)
    posts["url"].append(submission.url)
    posts["upvoteRatio"].append(submission.upvote_ratio)
    comment_list = []
    submission.comments.replace_more(limit = 0)
    for comment in submission.comments:
        comment_list.append(comment.body)
    posts["comments"].append(comment_list)
    print("in1")
    c=c+1 
print(c)
flairs["Scheduled"] = c
c= 0
for submission in reddit.subreddit('India').search('flair:"Politics"', limit=250):
    #flairs[submission.link_flair_text] = flairs[submission.link_flair_text]+1
    posts["flair"].append(submission.link_flair_text)
    posts["title"].append(submission.title)
    posts["id"].append(submission.id)
    posts["score"].append(submission.score)
    posts["body"].append(submission.selftext)
    posts["numberOfcomments"].append(submission.num_comments)
    posts["created"].append(submission.created)
    posts["author"].append(submission.author)
    posts["url"].append(submission.url)
    posts["upvoteRatio"].append(submission.upvote_ratio)
    comment_list = []
    submission.comments.replace_more(limit = 0)
    for comment in submission.comments:
        comment_list.append(comment.body)
    posts["comments"].append(comment_list)
    print("in1")
    c=c+1 
print(c)
    
flairs["Politics"] = c

# In[ ]:

c= 0
for submission in reddit.subreddit('India').search('flair:"Photography"', limit=250):
    #flairs[submission.link_flair_text] = flairs[submission.link_flair_text]+1
    posts["flair"].append(submission.link_flair_text)
    posts["title"].append(submission.title)
    posts["id"].append(submission.id)
    posts["score"].append(submission.score)
    posts["body"].append(submission.selftext)
    posts["numberOfcomments"].append(submission.num_comments)
    posts["created"].append(submission.created)
    posts["author"].append(submission.author)
    posts["url"].append(submission.url)
    posts["upvoteRatio"].append(submission.upvote_ratio)
    comment_list = []
    submission.comments.replace_more(limit = 0)
    for comment in submission.comments:
        comment_list.append(comment.body)
    posts["comments"].append(comment_list)
    print("in1")
    c=c+1 
print(c)

flairs["Photography"] = c




c = 0
for submission in reddit.subreddit('India').search('flair:"Policy/Economy"', limit=250):
    #flairs[submission.link_flair_text] = flairs[submission.link_flair_text]+1
    posts["flair"].append(submission.link_flair_text)
    posts["title"].append(submission.title)
    posts["id"].append(submission.id)
    posts["score"].append(submission.score)
    posts["body"].append(submission.selftext)
    posts["numberOfcomments"].append(submission.num_comments)
    posts["created"].append(submission.created)
    posts["author"].append(submission.author)
    posts["url"].append(submission.url)
    posts["upvoteRatio"].append(submission.upvote_ratio)
    comment_list = []
    submission.comments.replace_more(limit = 0)
    for comment in submission.comments:
        comment_list.append(comment.body)
    posts["comments"].append(comment_list)
    c=c+1 
    print("in1")
print(c)
flairs["Policy/Economy"] = c

# In[ ]:

c= 0
for submission in reddit.subreddit('India').search('flair:"Sports"', limit=250):
    #flairs[submission.link_flair_text] = flairs[submission.link_flair_text]+1
    posts["flair"].append(submission.link_flair_text)
    posts["title"].append(submission.title)
    posts["id"].append(submission.id)
    posts["score"].append(submission.score)
    posts["body"].append(submission.selftext)
    posts["numberOfcomments"].append(submission.num_comments)
    posts["created"].append(submission.created)
    posts["author"].append(submission.author)
    posts["url"].append(submission.url)
    posts["upvoteRatio"].append(submission.upvote_ratio)
    comment_list = []
    submission.comments.replace_more(limit = 0)
    for comment in submission.comments:
        comment_list.append(comment.body)
    posts["comments"].append(comment_list)
    print("in1")
    c=c+1 
print(c)

flairs["Sports"] = c


c=0
for submission in reddit.subreddit('India').search('flair:"Non-Political"', limit=250):
    #flairs[submission.link_flair_text] = flairs[submission.link_flair_text]+1
    posts["flair"].append(submission.link_flair_text)
    posts["title"].append(submission.title)
    posts["id"].append(submission.id)
    posts["score"].append(submission.score)
    posts["body"].append(submission.selftext)
    posts["numberOfcomments"].append(submission.num_comments)
    posts["created"].append(submission.created)
    posts["author"].append(submission.author)
    posts["url"].append(submission.url)
    posts["upvoteRatio"].append(submission.upvote_ratio)
    comment_list = []
    submission.comments.replace_more(limit = 0)
    for comment in submission.comments:
        comment_list.append(comment.body)
    posts["comments"].append(comment_list)
    print("in1")
    c=c+1 
print(c)
flairs["Non-Political"] = c

# In[ ]:

c= 0
for submission in reddit.subreddit('India').search('flair:"Science/Technology"', limit=250):
    #flairs[submission.link_flair_text] = flairs[submission.link_flair_text]+1
    posts["flair"].append(submission.link_flair_text)
    posts["title"].append(submission.title)
    posts["id"].append(submission.id)
    posts["score"].append(submission.score)
    posts["body"].append(submission.selftext)
    posts["numberOfcomments"].append(submission.num_comments)
    posts["created"].append(submission.created)
    posts["author"].append(submission.author)
    posts["url"].append(submission.url)
    posts["upvoteRatio"].append(submission.upvote_ratio)
    comment_list = []
    submission.comments.replace_more(limit = 0)
    for comment in submission.comments:
        comment_list.append(comment.body)
    posts["comments"].append(comment_list)
    print("in1")
    c=c+1 
print(c)

flairs["Science/Technology"] = c

c= 0
for submission in reddit.subreddit('India').search('flair:"Food"', limit=250):
    #flairs[submission.link_flair_text] = flairs[submission.link_flair_text]+1
    posts["flair"].append(submission.link_flair_text)
    posts["title"].append(submission.title)
    posts["id"].append(submission.id)
    posts["score"].append(submission.score)
    posts["body"].append(submission.selftext)
    posts["numberOfcomments"].append(submission.num_comments)
    posts["created"].append(submission.created)
    posts["author"].append(submission.author)
    posts["url"].append(submission.url)
    posts["upvoteRatio"].append(submission.upvote_ratio)
    comment_list = []
    submission.comments.replace_more(limit = 0)
    for comment in submission.comments:
        comment_list.append(comment.body)
    posts["comments"].append(comment_list)
    print("in1")
    c=c+1 
print(c)
flairs["Food"] = c

# In[ ]:

c = 0
for submission in reddit.subreddit('India').search('flair:"Business/Finance"', limit=250):
    #flairs[submission.link_flair_text] = flairs[submission.link_flair_text]+1
    posts["flair"].append(submission.link_flair_text)
    posts["title"].append(submission.title)
    posts["id"].append(submission.id)
    posts["score"].append(submission.score)
    posts["body"].append(submission.selftext)
    posts["numberOfcomments"].append(submission.num_comments)
    posts["created"].append(submission.created)
    posts["author"].append(submission.author)
    posts["url"].append(submission.url)
    posts["upvoteRatio"].append(submission.upvote_ratio)
    comment_list = []
    submission.comments.replace_more(limit = 0)
    for comment in submission.comments:
        comment_list.append(comment.body)
    posts["comments"].append(comment_list)
    print("in1")
    c=c+1 
print(c)

flairs["Business/Finance"] = c

c = 0
for submission in reddit.subreddit('India').search('flair:"Coronavirus"', limit=250):
    #flairs[submission.link_flair_text] = flairs[submission.link_flair_text]+1
    posts["flair"].append(submission.link_flair_text)
    posts["title"].append(submission.title)
    posts["id"].append(submission.id)
    posts["score"].append(submission.score)
    posts["body"].append(submission.selftext)
    posts["numberOfcomments"].append(submission.num_comments)
    posts["created"].append(submission.created)
    posts["author"].append(submission.author)
    posts["url"].append(submission.url)
    posts["upvoteRatio"].append(submission.upvote_ratio)
    comment_list = []
    submission.comments.replace_more(limit = 0)
    for comment in submission.comments:
        comment_list.append(comment.body)
    posts["comments"].append(comment_list)
    print("in1")
    c=c+1 
print(c)
flairs["Coronavirus"] = c

# In[ ]:

c = 0 
for submission in reddit.subreddit('India').search('flair:"Megathread"', limit=250):
    #flairs[submission.link_flair_text] = flairs[submission.link_flair_text]+1
    posts["flair"].append(submission.link_flair_text)
    posts["title"].append(submission.title)
    posts["id"].append(submission.id)
    posts["score"].append(submission.score)
    posts["body"].append(submission.selftext)
    posts["numberOfcomments"].append(submission.num_comments)
    posts["created"].append(submission.created)
    posts["author"].append(submission.author)
    posts["url"].append(submission.url)
    posts["upvoteRatio"].append(submission.upvote_ratio)
    comment_list = []
    submission.comments.replace_more(limit = 0)
    for comment in submission.comments:
        comment_list.append(comment.body)
    posts["comments"].append(comment_list)
    print("in1")
    c=c+1 
print(c)
flairs["Megathread"] = c

c = 0
for submission in reddit.subreddit('India').search('flair:"CAA-NRC"', limit=250):
    #flairs[submission.link_flair_text] = flairs[submission.link_flair_text]+1
    posts["flair"].append(submission.link_flair_text)
    posts["title"].append(submission.title)
    posts["id"].append(submission.id)
    posts["score"].append(submission.score)
    posts["body"].append(submission.selftext)
    posts["numberOfcomments"].append(submission.num_comments)
    posts["created"].append(submission.created)
    posts["author"].append(submission.author)
    posts["url"].append(submission.url)
    posts["upvoteRatio"].append(submission.upvote_ratio)
    comment_list = []
    submission.comments.replace_more(limit = 0)
    for comment in submission.comments:
        comment_list.append(comment.body)
    posts["comments"].append(comment_list)
    print("in1")
    c=c+1 
print(c)
flairs["CAA-NRC-NPR"] = c

# In[ ]:

c = 0
for submission in reddit.subreddit('India').search('flair:"[R]eddiquette"', limit=250):
    #flairs[submission.link_flair_text] = flairs[submission.link_flair_text]+1
    posts["flair"].append(submission.link_flair_text)
    posts["title"].append(submission.title)
    posts["id"].append(submission.id)
    posts["score"].append(submission.score)
    posts["body"].append(submission.selftext)
    posts["numberOfcomments"].append(submission.num_comments)
    posts["created"].append(submission.created)
    posts["author"].append(submission.author)
    posts["url"].append(submission.url)
    posts["upvoteRatio"].append(submission.upvote_ratio)
    comment_list = []
    submission.comments.replace_more(limit = 0)
    for comment in submission.comments:
        comment_list.append(comment.body)
    posts["comments"].append(comment_list)
    print("in1")
    c=c+1 
print(c)
flairs["[R]eddiquette"] = c
# In[ ]:


for i in flairs:
    print("Count of " + i+" " + str(flairs[i]))


# In[ ]:


posts_data = pd.DataFrame(posts)
posts_data


# In[ ]:


def get_date(created):
    return datetime.datetime.fromtimestamp(created)
_timestamp = posts_data["created"].apply(get_date)
posts_data = posts_data.assign(timestamp = _timestamp)
posts_data


# In[ ]:


posts_data.to_csv("testset.csv")


# In[ ]:




