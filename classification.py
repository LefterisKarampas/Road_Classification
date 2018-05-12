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

trainSet = trainSet[:400]

train,test = train_test_split(trainSet,test_size=0.01)

print len(train)
print len(test)
#Initialize Encoder
le = preprocessing.LabelEncoder()
le.fit(train["journeyPatternId"])
y = le.transform(train["journeyPatternId"])


X = train['Trajectory']
Y = test['Trajectory']
knn = KNN(5,DTW(Harvesine))

knn.fit(X,y)

knn_pred = knn.predict(Y)
predicted_categories = le.inverse_transform(knn_pred)
print(predicted_categories)
print(test['journeyPatternId'])
# with open('testSet_JourneyPatternIDs.csv', 'wb') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter=',',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     csvwriter.writerow(['tripId','journeyPatternId'])
#     for i in range(len(test_data['tripId'])):
#       csvwriter.writerow([str(test_data['tripId'][i]),predicted_categories[i]])