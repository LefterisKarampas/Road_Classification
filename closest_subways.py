from LCSS import LCSS
from Harvesine import Compare_Harvesine
from KNN import KNN
import pandas as pd
from ast import literal_eval
from gmplot import gmplot
import time
import os

def print_map(traj,name,path,subway):
	lon = []
	lan = []
	for i in traj:
		lon.append(i[1])
		lan.append(i[2])

	gmap = gmplot.GoogleMapPlotter(lan[0],lon[0],len(lon))
	gmap.plot(lan,lon,'green', edge_width=10)
	if subway != None:
		lon = []
		lan = []
		#print subway
		for j in subway:
			lon.append(traj[j][1])
			lan.append(traj[j][2])
		gmap.plot(lan,lon,'red', edge_width=10)
	gmap.draw(path+'/'+name+'.html')


def Find_Subsequence(Matrix):
	n = len(Matrix)
	subway = []
	if n > 0:
		m = len(Matrix[0])
	else:
		return subway
	i = n-1;
	j = m-1;
	index = 0
	last = None
	while(Matrix[i][j] != 0):
		if(Matrix[i][j] == Matrix[i-1][j]):
			i = i-1
		elif(Matrix[i][j] == Matrix[i][j-1]):
			j = j-1
		else:
			i = i-1
			j = j-1
			subway.append(j)
	return list(reversed(subway))



trainSet = pd.read_csv(
	'../train_set.csv', # replace with the correct path
	converters={"Trajectory": literal_eval},
	index_col='tripId')

testSet = pd.read_csv(
	'test_dataset/test_set_a2.csv', # replace with the correct path
	sep = "\t",
	converters={"Trajectory": literal_eval})

path = 'Test_Subways/'
if not os.path.exists(path):
	os.makedirs(path)
#trainSet = trainSet[:400]

for i in range(len(testSet)):
	start_time = time.time()
	origin = testSet['Trajectory'].iloc[i]
	knn = KNN(5,LCSS(Compare_Harvesine),origin,True)
	for j in range(len(trainSet)):
		knn.calculate_neighbor(trainSet['Trajectory'].iloc[j],j)
	results = knn.results()
	elapsed_time = time.time() - start_time
	path = 'Test_Subways/Test_Subways_'+str(i+1)
	if not os.path.exists(path):
		os.makedirs(path)
	file = open(path+'/results','w')
	file.write("Test_Subways_"+str(i+1)+"\n")
	print_map(origin,'Test_Subways_'+str(i+1),path,None)
	count = 1
	for k in results:
		print_map(trainSet['Trajectory'].iloc[k[0]],'Neighbor_'+str(count),path,Find_Subsequence(k[2]))
		file.write('Neighbor_'+str(count)+'\nJP_ID: '+trainSet['journeyPatternId'].iloc[k[0]]+'\n#Matching Points: '+str(k[1])+'\n\n')
		count+=1
	file.write("dt = "+str(elapsed_time) +" secs\n\n\n")
	file.close()


