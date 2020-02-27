# Geolocation of tweets with Decision Tree and Random Forest

This project aims to compare and contrast the differences in accuracy, precision and f1 score of Both Decision Tree and Random Forest Regression machine learning algorithms throught the classification of US locality (California, Georgia and NY) of labelled Twitter posts.

Sci-kit learn and pandas were the predominant tools.

The labelled twitter training data set is from: 

Eisenstein, Jacob's, et al (2010) 'A Latent Variable Model for Geographic Lexical Variation'

and Rahimi, Afshin, Trevor Cohn, and Timothy Baldwin's (2018) 'Semi-supervised user geolocation via graph convolutional networks.'

## Getting Started
---
To run this project download a python 3 distribution and create a virtual environment with the needed requirements found in requirements.txt. 

From within your virtual environment and in the main project directory

```
pip install -r requirements.txt
python main.py
```

This will train both a random forest  regressor and decsion tree classifier then print the accuracy, precision and f1 score on the trian test split.

## How it works
---

All data was originally in the form of the csv's prepended with _tweets.csv. This was converted into feature vectors by the encode class. The features were arrived at from the 100 best feature words found in all data sets through collaborative filtering, however this feauture not included in the package for relevance. These feature sets are prepended with _data.csv. This conversion can be found in the Transform class in the encode.py file. Other heuristic feautures such as the use of twitter tags # and @ were also added.

A generic train test split of 70/30 was established.
