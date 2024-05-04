import numpy as np
import math

def evaluate(matrix, solution): 
	#Matrix is a (n,n) square matrix representing the population
	#Solution is a list of tuples (x,y) representing coordinates of the hospitals

	#The evaluation is made by 4 criteria : average distance, median distance, worst distance, worst 5% distance


	#First we get all the distances
	shape = matrix.shape
	size = shape[0]
	distances = np.empty((size**2,), dtype="int64") #array of 1 dimension
	hopitaux = np.zeros(len(solution))

	for x in range(size):
		for y in range(size):

			lowestDistance = np.inf
			closestHospital = np.inf
			for index, hospital in enumerate(solution):
				a,b = hospital
				distance = (a - x)**2 + (b - y)**2 #On n'applique pas la racine carrée car on souhaite simplement comparer les distances

				if distance < lowestDistance:
					closestHospital = index
					lowestDistance = distance

			distances[x*size + y] = math.sqrt(lowestDistance) * matrix[x][y] * 100 / (math.sqrt(2) * (size)) #Scale to percentages of max length
			hopitaux[closestHospital] = hopitaux[closestHospital] + 1  

	mean = distances.mean()
	bestPercentile = np.percentile(distances, 10, axis=0, interpolation="higher") #Takes the 95th best percentile
	median = np.percentile(distances, 50, axis=0, interpolation="higher") #Takes the 50th percentile, so the median
	worst = np.percentile(distances, 100, axis=0, interpolation="higher") #Takes the 0th worst percentile, the worst result
	worstPercentile = np.percentile(distances, 95, axis=0, interpolation="higher") #Takes the 5th worst percentile
	saturation = max(hopitaux)

	SCALAIRE_MEAN = 1
	SCALAIRE_PERCENTILE10 = 1
	SCALAIRE_PERCENTILE50 = 1
	SCALAIRE_WORST = 1
	SCALAIRE_PERCENTILE95 = 1
	SCALAIRE_SATURATION = 1

	#The better the solution, the lower the score
	mean *= SCALAIRE_MEAN
	median *= SCALAIRE_PERCENTILE50
	bestPercentile *= SCALAIRE_PERCENTILE10
	worst *= SCALAIRE_WORST
	worstPercentile *= SCALAIRE_PERCENTILE95
	saturation *= SCALAIRE_SATURATION

	score = mean + bestPercentile + median + worst + worstPercentile + saturation

	return (score, [mean, bestPercentile, median, worst, worstPercentile, saturation])