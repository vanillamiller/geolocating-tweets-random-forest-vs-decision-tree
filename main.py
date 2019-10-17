import pandas as pd
from sklearn.metrics import accuracy_score, precision_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
import featuretools as ft
import re
from sklearn import preprocessing
from to_csv import CSV
from encode import Transform as ts
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import FeatureHasher
import numpy as np

# .txt preprocessed and stored in .csv. vectorized with
train_data=pd.read_csv('train_data.csv')
dev_data=pd.read_csv('dev_data.csv')

# There was an unnoticed error when writing to the sanitized .csv file, the scikit-learn.preprocessing.LabelEncoder
# encoded the two dev and train files differently... the mapping below fixes this.
# these are the sanitized files 
train_temp=pd.read_csv('train_tweets.csv', encoding="ISO-8859-1", header=None, names=['tweet-id','user-id','text','loc'])
dev_temp=pd.read_csv('dev_tweets.csv', encoding="ISO-8859-1",header=None, names=['tweet-id','user-id','text','loc'])

# replace mismatching encoding with the original string
train_data['loc']=train_temp['loc']
dev_data['loc']=dev_temp['loc']

# map integer representations to these values
train_data['loc'] = train_data['loc'].map({'California': 0, 'NewYork': 1, 'Georgia': 2})
dev_data['loc'] = dev_data['loc'].map({'California': 0, 'NewYork': 1, 'Georgia': 2})

# set tweet-id as index and drop from dataframe
train_data['tweet-id']=train_data['tweet-id'].astype('int')
train_data.set_index('tweet-id', inplace=True, drop=True)
dev_data['tweet-id']=dev_data['tweet-id'].astype('int')
dev_data.set_index('tweet-id', inplace=True, drop=True)

# print(train_data.head(10))
# print(dev_data.head(10))

# concatonate the two datasets
data=pd.concat([train_data, dev_data])
print(len(data))

# make sure the concatonation was performed axis=1
print(data.head())

# remove labels from training data
x_data=data.drop(['loc'], axis=1)

# establish location as the target vector
y_data=data[['loc']]

# split the data 70/30
x_train, x_test, y_train, y_test=train_test_split(x_data, y_data, test_size=0.3)

# initialize decision tree and random forest classifiers
dtm=DecisionTreeClassifier()
rfr=RandomForestRegressor()

# fit the vector and target to the decision tree classifier
dtm.fit(x_train, y_train)

# fit the vector and target to the random forest ensemble classifier
rfr.fit(x_train, y_train)

# map predicitons to predicition vector
Yhat=dtm.predict(x_test)
Yhat2=rfr.predict(x_test)

print("Decison Tree Accuracy: "+accuracy_score(y_test, Yhat))
print('Random Forest Accuracy: '+accuracy_score(y_test, Yhat2.round()))

print('Decision Tree Precision: '+precision_score(y_test, Yhat, average=None))
print('Random Forest Precision: '+precision_score(y_test, Yhat2.round(), average=None))