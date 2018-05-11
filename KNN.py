
class KNN:
	
	def __init__(self,k,metric,origin):
		self.k = k
		self.metric = metric
		self.origin = origin
		self.neigh = [ (None,float('Inf')) for x in range(k) ]
		print self.neigh


	def calculate_neighbor(self,destination,id):
		dist = self.metric.Distance(self.origin,destination)
		self.neigh.append((id,dist))
		self.neigh = sorted(self.neigh, key = lambda x: x[1])
		self.neigh = self.neigh[:self.k]

	def results(self):
		return self.neigh