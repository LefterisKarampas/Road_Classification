from sklearn.metrics import classification_report
from sklearn import preprocessing
from sklearn.model_selection import KFold,cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_validate
from os import path
import pandas as pd
import numpy as np
from ast import literal_eval
import csv
from KNN import KNN
from sklearn import preprocessing
from DTW import DTW
from Harvesine import Harvesine
from sklearn.cross_validation import train_test_split

trainSet = pd.read_csv(
	'../train_set.csv', # replace with the correct path
	converters={"Trajectory": literal_eval},
	index_col='tripId')

train,_ = train_test_split(trainSet,test_size=0.9)


#Initialize Encoder
le = preprocessing.LabelEncoder()
le.fit(train["journeyPatternId"])
y = le.transform(train["journeyPatternId"])

X = train['Trajectory']

knn = KNN(5,DTW(Harvesine))


scoring = ['accuracy']

classifier_pipeline = make_pipeline(knn)
scores = cross_validate(classifier_pipeline, X, y, cv=10,scoring=scoring)
print mean(scores['test_accuracy'])
