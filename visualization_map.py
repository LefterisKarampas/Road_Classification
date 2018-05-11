import pandas as pd
from ast import literal_eval
from gmplot import gmplot
import random
import os


trainSet = pd.read_csv(
	'../train_set.csv', # replace with the correct path
	converters={"Trajectory": literal_eval},
	index_col='tripId')

directory = 'map'
if not os.path.exists(directory):
    os.makedirs(directory)

items = random.sample(range(len(trainSet)),5)
for item in items:
	traj = traj = trainSet['Trajectory'].iloc[item]
	lon = []
	lan = []
	for i in traj:
		lon.append(i[1])
		lan.append(i[2])

	gmap = gmplot.GoogleMapPlotter(lan[0],lon[0],len(lon))

	gmap.plot(lan,lon,'green', edge_width=5)

	gmap.draw(directory+'/map_'+str(trainSet['journeyPatternId'].iloc[item])+'_'+str(item)+'.html')
