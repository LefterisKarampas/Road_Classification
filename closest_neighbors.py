from KNN import KNN
from DTW import DTW
from Harvesine import Harvesine
import pandas as pd
from ast import literal_eval
from gmplot import gmplot
import time
import os

def print_map(traj,name,path):
	lon = []
	lan = []
	for i in traj:
		lon.append(i[1])
		lan.append(i[2])

	gmap = gmplot.GoogleMapPlotter(lan[0],lon[0],len(lon))
	gmap.plot(lan,lon,'green', edge_width=5)
	gmap.draw(path+'/'+name+'.html')


trainSet = pd.read_csv(
	'../train_set.csv', # replace with the correct path
	converters={"Trajectory": literal_eval},
	index_col='tripId')

testSet = pd.read_csv(
	'test_dataset/test_set_a1.csv', # replace with the correct path
	sep = "\t",
	converters={"Trajectory": literal_eval})

path = 'Test_Trip/'
if not os.path.exists(path):
	os.makedirs(path)
#trainSet = trainSet[:200]

for i in range(len(testSet)):
	start_time = time.time()
	origin = testSet['Trajectory'].iloc[i]
	knn = KNN(5,DTW(Harvesine),origin,False)
	for j in range(len(trainSet)):
		knn.calculate_neighbor(trainSet['Trajectory'].iloc[j],j)
	results = knn.results()
	elapsed_time = time.time() - start_time
	path = 'Test_Trip/Test_Trip_'+str(i+1)
	if not os.path.exists(path):
		os.makedirs(path)
	file = open(path+'/results','w')
	file.write("Test_Trip_"+str(i+1)+"\n")
	print_map(origin,'Test_Trip_'+str(i+1),path)
	count = 1
	for k in results:
		print_map(trainSet['Trajectory'].iloc[k[0]],'Neighbor_'+str(count),path)
		file.write('Neighbor_'+str(count)+'\nJP_ID: '+trainSet['journeyPatternId'].iloc[k[0]]+'\nDTW: '+str(k[1])+'km\n\n')
		count+=1
	file.write("dt = "+str(elapsed_time) +" secs\n\n\n")
	file.close()
