from DensityMatrix import DensityMatrix
from RandomSolution import RandomSolution
from GreedyAlgorithm import GreedyAlgorithm
from EvaluateFunction import evaluate

import math
import numpy as np
import matplotlib.pyplot as plt

MATRIX_SIZE = 50
NUM_OF_HOSPITALS = 6
LOOPS = 5000


def main():
	Matrix = DensityMatrix.GenerateDensityMatrix(NUM_OF_HOTPOINT = 10, BINS = MATRIX_SIZE)

	solutions = []
	for _ in range(10):
		solutions.append(RandomSolution.GenerateRandomSolution(MATRIX_SIZE, NUM_OF_HOSPITALS))

	
	#print(evaluate(Matrix, solutions[k]))

	greedyResult = GreedyAlgorithm.Execute(Matrix, NUM_OF_HOSPITALS, NUM_OF_LOOPS = LOOPS)
	greedySolution = greedyResult[0]
	greedyScore = greedyResult[1]
	print(evaluate(Matrix, greedySolution)[1], greedySolution)

	#RandomSolution.EstimateTimeAllSolutions(Matrix, 10, 100)


	extent = [-5, 5, -5, 5]
	offset = (10/MATRIX_SIZE)*(math.sqrt(2)/3)
	plot1 = plt.figure(1)
	plt.plot([k for k in range(LOOPS)], greedyResult[2])

	plot2 = plt.figure(2)
	plt.imshow(Matrix, extent=extent, origin='lower')

	for point in greedySolution:
		
		x = point[0]
		y = point[1]

		x = x*10/MATRIX_SIZE - 5
		y = y*10/MATRIX_SIZE - 5

		plt.scatter(x - offset, y - offset, s=500/MATRIX_SIZE, c='red', marker='o')
	
	plt.show()


if __name__=="__main__":
   main()