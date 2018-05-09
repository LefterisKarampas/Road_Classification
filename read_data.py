import pandas as pd
from ast import literal_eval
from gmplot import gmplot



trainSet = pd.read_csv(
	'../train_set.csv', # replace with the correct path
	converters={"Trajectory": literal_eval},
	index_col='tripId')

#print trainSet['journeyPatternId'][1]
#print trainSet['Trajectory'][1]

journey = {}
trajectories = []
counter = 0
print len(trainSet)
for i in range(len(trainSet)):
	key = trainSet['journeyPatternId'].iloc[i]
	traj = trainSet['Trajectory'].iloc[i]
	if journey.has_key(key):
		index = journey[key]
		trajectories[index] = trajectories[index] + traj
	else:
		journey[key] = counter
		trajectories.append(traj)
		counter+=1
		
print len(trajectories)

file = open('file.txt','w')
counter = 0
for key in journey.keys():
	lon = []
	lan = []
	#file.write(str(trajectories[j]))
	#trajectories[j].sort(key=lambda x: x[0])
	#file.write("---------------------------------\n")
	#file.write(str(trajectories[j]))
	for i in trajectories[counter]:
		lon.append(i[1])
		lan.append(i[2])

	gmap = gmplot.GoogleMapPlotter(lan[0],lon[0],len(lon))

	gmap.plot(lan,lon,'green', edge_width=5)

	gmap.draw('map_'+str(key)+'.html')
	counter+=1
	if(counter >= 5):
		break
