# Reddit Flair Detector

The link for the app : https://flaredetect.herokuapp.com
The link for automated testing(also avaialable through the app) : https://flaredetect.herokuapp.com/automated_testing

This is an app to detect flairs of Reddit India, r/india. 
The app takes input from the user, in the form of URL for the post and return the predicted and actual flair of the post. The application has used been deployed on Heroku server. It also has an option of automated tesing the app. 

## Steps followed:

Described each step along with code in the notebooks. 

### Step 1: Extraction of r/india data 
Used praw library of python for extraction.

### Step 2: Exploratory Data Analysis
Analysed the data using graphs and scattered points as well as correlation. Used matplotlib library for the same.

### Step 3: Made Reddit Flair Detector. Performed the following the steps:
- Preprocessed the data: Removed stopwords and performed stemming on the data
- Diving into training and test: Divided the dataset into training and   test set. Used standard, 0.7:0.3 metric
- Testing accross classifiers: Tested along 3 classifiers: Naive Bayees, SVM   and Logisitic Regression. Checked accuracy of each of the classifiers.
- Saving the model: Saved the model with highest accuracy in a .sav file to   use it for prediction. 
- Model testing: Take input URL from the user and return the predicted and    actual flairs. Call the saved model for predicted flairs

### Step 4: Creating an app to predict flair: Used flask to create the app. 
- The app URL input from the user and outputs Actual and Predicted flair of   the same.
- The app also has an option of automated testing. The user has to upload a text file with a list of URLs. The app return a json file with urls as key and predicted flair as value. User can download the same from the website. A sample text file is available in the repository

### Step5: Depoyment on heroku: 
The app is deployed on heroku using this github repository. 


## Accuracy:
- Naive Bayes: 
	- Using title as a feature:0.54
	- Using body as a feature:0.22
	- Using comments as a feature:0.21
	- Using combine as feature:0.30
- Support vector machine:
	- Using title as a feature:0.52
	- Using body as a feature:0.23
	- Using comments as a feature:0.51
	- Using combine as feature:0.63
- Logistic Regression:
	Using title as a feature:0.54
	- Using body as a feature:0.22
	- Using comments as a feature:0.52
	- Using combine as feature:0.64	
	
## Automated testing:

The app also provides a benefit o automated testing.

### How to use:

Send a post request to [Link](https://flaredetect.herokuapp.com/automated_testing) with a text file.

### How it works:
-The app reads all the urls in the file line by line and predict the flair
- The same is stored in json file.

### Output:

It will be a json file with url as key and predicted flair as value.

    
