from DensityMatrix import DensityMatrix
from RandomSolution import RandomSolution
from GreedyAlgorithm import GreedyAlgorithm
from RecuitSimuleAlgorithm import RecuitSimuleAlgorithm
from EvaluateFunction import evaluate

import math
import numpy as np
import matplotlib.pyplot as plt

MATRIX_SIZE = 100
NUM_OF_HOSPITALS = 10
LOOP = 2000

def main():

	#Generate the test Matix
	Matrix = DensityMatrix.GenerateDensityMatrix(NUM_OF_HOTPOINT = 15, SIGMA = 1.5, BINS = MATRIX_SIZE)

	#RandomSolution.EstimateTimeAllSolutions(Matrix, 10, 100)


	#Solve this Matrix with the Greedy Algorithm
	greedyResult = GreedyAlgorithm.Execute(Matrix, NUM_OF_POINTS = NUM_OF_HOSPITALS, NUM_OF_LOOPS = LOOP)
	
	#Solve this Matrix with the Simulated Annealing Algorithm
	initialTemp = 10
	endingTemp = 0
	annealingResult = RecuitSimuleAlgorithm.Execute(Matrix, NUM_OF_POINTS = NUM_OF_HOSPITALS, INITIAL_TEMP = initialTemp, ENDING_TEMP = endingTemp, GRADIENT = (initialTemp - endingTemp)/LOOP, alpha = 170)

	tightNeighborhoodResult = GreedyAlgorithm.Execute(Matrix, NUM_OF_POINTS = NUM_OF_HOSPITALS, INITIAL_SOLUTION = annealingResult[0], NEIGHBOR_RANGE = MATRIX_SIZE/10, NUM_OF_LOOPS = LOOP)

	print(evaluate(Matrix, greedyResult[0])[0])
	print(evaluate(Matrix, annealingResult[0])[0])
	print(evaluate(Matrix, tightNeighborhoodResult[0])[0])
	print(greedyResult[0])
	print(annealingResult[0])
	print(tightNeighborhoodResult[0])

	extent = [-5, 5, -5, 5]
	offset = (10/MATRIX_SIZE)*(math.sqrt(2)/3)

	plot1 = plt.figure(1)
	plt.title("Comparaison des méthodes d'optimisation")
	plt.plot([k for k in range(len(greedyResult[2]))], greedyResult[2], label = "Méthode Gloutonne", color="magenta")
	plt.plot([k for k in range(len(annealingResult[2]))], annealingResult[2], label = "Méthode du Recuit Simulé", color="orangered")
	plt.plot([k for k in range(len(tightNeighborhoodResult[2]))], tightNeighborhoodResult[2], label = "Méthode du Recuit Simulé + voisinage serré", color="aqua")
	plt.legend(loc="best")

	plot2 = plt.figure(2)
	plt.imshow(Matrix, extent=extent, origin='lower')

	for point in greedyResult[0]:
		
		x = point[0]
		y = point[1]

		x = x*10/MATRIX_SIZE - 5
		y = y*10/MATRIX_SIZE - 5

		plt.scatter(x - offset, y - offset, s=500/MATRIX_SIZE, c='red', marker='o')

	for point in annealingResult[0]:
		
		x = point[0]
		y = point[1]

		x = x*10/MATRIX_SIZE - 5
		y = y*10/MATRIX_SIZE - 5

		plt.scatter(x - offset, y - offset, s=500/MATRIX_SIZE, c='orange', marker='o')

	for point in tightNeighborhoodResult[0]:
		
		x = point[0]
		y = point[1]

		x = x*10/MATRIX_SIZE - 5
		y = y*10/MATRIX_SIZE - 5

		plt.scatter(x - offset, y - offset, s=500/MATRIX_SIZE, c='gold', marker='o')
	
	plt.show()


if __name__=="__main__":
   main()