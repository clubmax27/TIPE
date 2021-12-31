from DensityMatrix import DensityMatrix
from RandomSolution import RandomSolution
from GreedyAlgorithm import GreedyAlgorithm
from EvaluateFunction import evaluate

import math
import numpy as np
import matplotlib.pyplot as plt

MATRIX_SIZE = 100


def main():
	Matrix = DensityMatrix.GenerateDensityMatrix(NUM_OF_HOTPOINT = 20, BINS = MATRIX_SIZE)

	solutions = []
	for _ in range(10):
		solutions.append(RandomSolution.GenerateRandomSolution(MATRIX_SIZE, 5))

	
	#print(evaluate(Matrix, solutions[k]))

	greedyResult = GreedyAlgorithm.Execute(Matrix, 6)
	greedySolution = greedyResult[0]
	greedyScore = greedyResult[1]
	print(evaluate(Matrix, greedySolution)[1])

	#RandomSolution.EstimateTimeAllSolutions(Matrix, 10, 100)


	extent = [-5, 5, -5, 5]
	offset = (10/MATRIX_SIZE)*(math.sqrt(2)/3)
	plt.imshow(Matrix, extent=extent, origin='lower')

	for point in greedySolution:
		
		x = point[0]
		y = point[1]

		x = x*10/MATRIX_SIZE - 5
		y = y*10/MATRIX_SIZE - 5

		plt.scatter(x - offset, y - offset, s=200/MATRIX_SIZE, c='red', marker='o')

	plt.show()


if __name__=="__main__":
   main()