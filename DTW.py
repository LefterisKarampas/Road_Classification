class DTW:
	def __init__(self, metric):
		self.metric = metric

	def Distance(self,origin,destination):
		n = len(origin)
		m = len(destination)
		Matrix = [[ float('Inf') for x in range(m)] for y in range(n)]
		Matrix[0][0] = 0

		for i in range(1,n):
			for j in range(1,m):
				cost = self.metric(origin[i],destination[j])
				Matrix[i][j] = cost + min(min(Matrix[i-1][j],Matrix[i][j-1]),Matrix[i-1][j-1])

		return Matrix[n-1][m-1]
