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

	for x in range(size):
		for y in range(size):

			lowestDistance = np.inf
			for hospital in solution:
				a,b = hospital
				distance = (a - x)**2 + (b - y)**2 #Applying the square root is a waste of time because the function is strictly evolutive

				if distance < lowestDistance:
					lowestDistance = distance

			distances[x*size + y] = math.sqrt(lowestDistance) * matrix[x][y] * 100 / (math.sqrt(2) * (size)) #Scale to percentages of max length

	mean = distances.mean()
	bestPercentile = np.percentile(distances, 10, axis=0, interpolation="higher") #Takes the 95th best percentile
	median = np.percentile(distances, 50, axis=0, interpolation="higher") #Takes the 50th percentile, so the median
	worst = np.percentile(distances, 100, axis=0, interpolation="higher") #Takes the 0th worst percentile, the worst result
	worstPercentile = np.percentile(distances, 95, axis=0, interpolation="higher") #Takes the 5th worst percentile

	#The better the solution, the lower the score
	score = (mean*1000 + median + bestPercentile + worst + worstPercentile)

	return (score, [mean, median, bestPercentile, worst, worstPercentile])