import operator

class KNN:
	
	def __init__(self,k,metric,origin = None,reverse=True):
		self.k = k
		self.metric = metric
		self.origin = origin
		self.reverse = reverse
		if reverse == True:
			self.neigh = [ (None,float('-Inf')) for x in range(k) ]
		else:
			self.neigh = [ (None,float('Inf')) for x in range(k) ]


	def calculate_neighbor(self,destination,id):
		dist = self.metric.Calculate(self.origin,destination)
		self.neigh.append((id,dist))
		self.neigh = sorted(self.neigh, key = lambda x: x[1],reverse=self.reverse)
		self.neigh = self.neigh[:self.k]

	def results(self):
		return self.neigh


	def score(self, testSet, testSetLabels):
		predictedLabels = self.predict(testSet)
		count = 0
		size = len(predictedLabels)
		for i in range(size):
			if predictedLabels[i] == testSetLabels[i]:
				count = count + 1

		return count / size


	def fit(self, trainSet, trainSetLabels):
		self.trainSet = trainSet
		self.trainSetLabels = trainSetLabels


	def predict(self, testSet):
		resultLabels = []

		for featuresArray in testSet:
			kneighbors = self.getNeighbors(featuresArray)
			label = self.majorityVote(kneighbors)
			resultLabels.append(label)

		return resultLabels


	def getNeighbors(self, featuresArray):
		distances = []

		trainSet = self.trainSet
		trainSize = len(trainSet)

		#for each element in out train set
		for i in range(trainSize):
			distance = self.metric.Calculate(trainSet.iloc[i], featuresArray)
			indexAndDist = (i,distance)
			distances.append(indexAndDist)

		#sort according to dist
		distances.sort(key=operator.itemgetter(1))

		kneighbors = []

		for i in range(self.k):
			#only keep neighbor and his label
			index = distances[i][0] #contains the index of the neighbor
			label = self.trainSetLabels[index]
			neighbor = (trainSet.iloc[index],label)
			kneighbors.append(neighbor)

		return kneighbors


	def majorityVote(self, kneighbors):
		votes = {}

		for neighbor in kneighbors:
			label = neighbor[1]
			if label in votes:
				votes[label] += 1
			else:
				votes[label] = 1

		sortedVotes = sorted(votes.iteritems(), key=operator.itemgetter(1), reverse=True)
		return sortedVotes[0][0]	


# from Harvesine import Harvesine
# from DTW import DTW


# x = KNN(5,DTW(Harvesine),[[5,0,1],[6,0,2]])
# x.calculate_neighbor([[7,3,2],[8,1,3]],1)
# x.calculate_neighbor([[7,0,2],[8,0,3]],2)
# print x.results()