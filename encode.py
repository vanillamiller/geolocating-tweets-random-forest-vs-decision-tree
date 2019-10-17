import pandas as pd
from sklearn import preprocessing

class Transform:

    @staticmethod
    def encode(data):
        # cast twitter-id to integer and drop from frame
        data['tweet-id']=data['tweet-id'].astype('int')
        data.set_index('tweet-id', inplace=True, drop=True)

        # typecast un-numeric data as a string
        data[['text','loc','user-id']]=data[['text','loc','user-id']].astype('str')
        
        # encode the user-id using sk-learn pre-procession library
        le_uid=preprocessing.LabelEncoder()
        data['user-id']=le_uid.fit_transform(data['user-id'])

        # map consistent target values for any vector (why sk-learn's toolkit wasn't used here)
        data['loc'] = data['loc'].map({'California': 0, 'NewYork': 1, 'Georgia': 2})

        # make sure something is happening 
        print("loc and user-id encoded")
        return data

    @staticmethod
    def vector_text_intuition(data):
        # the set of best from test-data50, train-data5", dev-data50
        all_best = ['dats', 'miami', 'bomb', 'lmaoo', 'la', 'ma', 'ish', 'tho', 'aja', 'u', 'rt', 'childplease', 'quote', 'for', 
        'shyt', 'boaw', 'ahahaha', 'the', 'iight', 'dat', 'inhighschool', 'have', 'skool', 'just', 'lols', 'raining', 'flirty', 'mad', 
        'lmfaoo', 'thatisall', 'spelman', 'tweet-id', 'has', 'that', 'hahahaha', 'will', 'icheatedbecause', 'tacos', 'finna', 'hahaa', 
        'haha', 'da', 'crisantasbreast', 'hella', 'lml', 'tinos', 'ahaha', 'ada', 'followdormtainment', 
        'atl', 'fab', 'san', 'cau', 'ion', 'dem', 'cuhz', 'neighbors', 'deadass', 'atlanta', 'nd', 'cuh', 'ga', 'gsu', 'fasho', 'ii', 
        'lowkey', 'naw', 'a', 'is', 'frequency', 'smh', 'wat', 'sir', 'dis', 'bbm', 'user-id STRING', 'd', 'oovoo', 'dha', 'foo', 
        'hahaha', 'coo', 'dormtainment', 'famu', 'odee', 'lmaooo', 'of', 'rain', 'banget', 'are', 'juss', 'andthenwehadsex', 'sb', 
        'auc', 'neva', 'what', 'this', 'aha', 'break', 'hahah', 'willies', 'to', 'lmaoooo', 'freaknik', 'spring', 'pcb', 'gw', 
        'dead', 'it', 'know', 'knw', 'famusextape', 'nah', 'madd', 'bruh', 'af', 'ive', 'wet', 'hehe', 'dom', 'and', 'with', 'parody', 
        'lmfaooo']

        hyp=['!','...','@USER','#']

        features=all_best+hyp

        for feat in features:
            vector=[]
            for index, row in data.iterrows():
                vector.append(row['text'].upper().count(feat.upper()))
            data[feat]=vector


        print("tweet text vectorized with heuristic values")
        return data

    @staticmethod
    def get_best():
        return ['dats', 'miami', 'bomb', 'lmaoo', 'la', 'ma', 'ish', 'tho', 'aja', 'u', 'rt', 'childplease', 'quote', 'for', 
        'shyt', 'boaw', 'ahahaha', 'the', 'iight', 'dat', 'inhighschool', 'have', 'skool', 'just', 'lols', 'raining', 'flirty', 'mad', 
        'lmfaoo', 'thatisall', 'spelman', 'tweet-id', 'has', 'that', 'hahahaha', 'will', 'icheatedbecause', 'tacos', 'finna', 'hahaa', 
        'haha', 'da', 'crisantasbreast', 'hella', 'lml', 'tinos', 'ahaha', 'ada', 'followdormtainment', 
        'atl', 'fab', 'san', 'cau', 'ion', 'dem', 'cuhz', 'neighbors', 'deadass', 'atlanta', 'nd', 'cuh', 'ga', 'gsu', 'fasho', 'ii', 
        'lowkey', 'naw', 'a', 'is', 'frequency', 'smh', 'wat', 'sir', 'dis', 'bbm', 'user-id STRING', 'd', 'oovoo', 'dha', 'foo', 
        'hahaha', 'coo', 'dormtainment', 'famu', 'odee', 'lmaooo', 'of', 'rain', 'banget', 'are', 'juss', 'andthenwehadsex', 'sb', 
        'auc', 'neva', 'what', 'this', 'aha', 'break', 'hahah', 'willies', 'to', 'lmaoooo', 'freaknik', 'spring', 'pcb', 'gw', 
        'dead', 'it', 'know', 'knw', 'famusextape', 'nah', 'madd', 'bruh', 'af', 'ive', 'wet', 'hehe', 'dom', 'and', 'with', 'parody', 
        'lmfaooo']