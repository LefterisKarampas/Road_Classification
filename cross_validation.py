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

trainSet = pd.read_csv(
	'../train_set.csv', # replace with the correct path
	converters={"Trajectory": literal_eval},
	index_col='tripId')

trainSet = trainSet[:100]

#Initialize Encoder
le = preprocessing.LabelEncoder()
le.fit(trainSet["journeyPatternId"])
y = le.transform(trainSet["journeyPatternId"])

X = trainSet['Trajectory']

knn = KNN(5,DTW(Harvesine))


scoring = ['accuracy']

classifier_pipeline = make_pipeline(knn)
scores = cross_validate(classifier_pipeline, X, y, cv=10,scoring=scoring)
print mean(scores['test_accuracy'])
