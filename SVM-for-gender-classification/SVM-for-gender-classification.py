# Natural Language Processing
 
# Importing the libraries
import numpy as np
import pandas as pd
 
# Importing the dataset
# Suppose that we have 1 million raw text data under *.tsv format
# Suppose that we have already made the label "1" for male and "0" for female tweets
dataset = pd.read_csv('raw_text_data.tsv', delimiter = '\t', quoting = 3)
 
 
# Cleaning the texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 1000000):
    tweet = re.sub('[^a-zA-Z]', ' ', dataset['tweet'][i])
    tweet = tweet.lower()
    tweet = tweet.split()
    ps = PorterStemmer()
    tweet = [ps.stem(word) for word in tweet if not word in set(stopwords.words('english'))]
    tweet = ' '.join(tweet)
    corpus.append(tweet)
 
# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
x = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values
 
# Splitting the dataset into the Training set and Test set
# We use 80% of the data for training and 20% for test
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0)
 
#Support Vector Machine (SVM)
 
# Fitting SVM to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(x_train, y_train)
 
# Predicting the Test set results
y_pred = classifier.predict(x_test)
 
# Making the Confusion Matrix for calculating SVM performance under the test data
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
