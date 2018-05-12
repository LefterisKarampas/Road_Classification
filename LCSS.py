

class LCSS:

	def __init__(self,comp_func):
		self.comp = comp_func

	def Calculate(self,X,Y):
		n = len(X)
		m = len(Y)
		Matrix = [[ 0 for x in range(m+1)] for y in range(n+1)]
		
		for i in range(1,n+1):
			for j in range(1,m+1):
				if self.comp(X[i-1],Y[j-1]):
					Matrix[i][j] = Matrix[i-1][j-1] + 1
				else:
					Matrix[i][j] = max(Matrix[i-1][j],Matrix[i][j-1])

		return Matrix[n][m]



# def comp(a,b):
# 	return a == b


# x = LCSS(comp)

# print(x.LCSLenght(['a','e','b','c'],['b','a','e','b','g']))