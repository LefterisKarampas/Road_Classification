from KNN import KNN
from DTW import DTW
from Harvesine import Harvesine
import pandas as pd
from ast import literal_eval
from gmplot import gmplot
import time

def print_map(traj,id):
	lon = []
	lan = []
	for i in traj:
		lon.append(i[1])
		lan.append(i[2])

	gmap = gmplot.GoogleMapPlotter(lan[0],lon[0],len(lon))
	gmap.plot(lan,lon,'green', edge_width=5)
	gmap.draw(str(id)+'.html')


trainSet = pd.read_csv(
	'../train_set.csv', # replace with the correct path
	converters={"Trajectory": literal_eval},
	index_col='tripId')

testSet = pd.read_csv(
	'../test_set_a1.csv', # replace with the correct path
	converters={"Trajectory": literal_eval})

print testSet

# file = open('../test_set_a1.csv','r')
# print file.readline()
# for i in range(5):
# 	nums =  file.readline()
# 	nums = [[float(y) for y in x] for x in nums]
# 	print nums
#exit()

trainSet = trainSet[:200]
for i in range(len(testSet)):
	start_time = time.time()
	origin = testSet['Trajectory'].iloc[i]
	knn = KNN(5,DTW(Harvesine),origin)
	for j in range(len(trainSet)):
		knn.calculate_neighbor(trainSet['Trajectory'].iloc[j],j)
	print_map(origin,'0')
	results = knn.results()
	for k in results:
		print_map(trainSet['Trajectory'].iloc[k[0]],k[0])
	elapsed_time = time.time() - start_time
	print "dt = "+str(elapsed_time) +" secs"

