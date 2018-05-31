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

#trainSet = trainSet[:400]

testSet = pd.read_csv(
	'test_dataset/test_set_a2.csv', # replace with the correct path
	sep = "\t",
	converters={"Trajectory": literal_eval})

#train,test = train_test_split(trainSet,test_size=0.01)

#rint len(train)
#print len(test)
#Initialize Encoder
le = preprocessing.LabelEncoder()
le.fit(trainSet["journeyPatternId"])
y = le.transform(trainSet["journeyPatternId"])


X = trainSet['Trajectory']
Y = testSet['Trajectory']
knn = KNN(5,DTW(Harvesine))

knn.fit(X,y)

knn_pred = knn.predict(Y)
predicted_categories = le.inverse_transform(knn_pred)
print(predicted_categories)

with open('testSet_JourneyPatternIDs.csv', 'wb') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(['Test_Trip_ID','Predicted_JourneyPatternID]'])
    for i in range(len(testSet)):
      csvwriter.writerow([str(i+1),predicted_categories[i]])