from DensityMatrix import DensityMatrix
from RandomSolution import RandomSolution
from GreedyAlgorithm import GreedyAlgorithm
from RecuitSimuleAlgorithm import RecuitSimuleAlgorithm
from TabooSearchAlgorithm import TabooSearchAlgorithm
from GeneticAlgorithm import GeneticAlgorithm
from EvaluateFunction import evaluate
from Sarthe import GenerateSartheDensityMatrix

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import logging
import logging.config

MATRIX_SIZE = 4
NUM_OF_HOSPITALS = 1
LOOP = 1000

def main():

	#Generate the test Matix
	matrix = DensityMatrix.GenerateDensityMatrix(NUM_OF_HOTPOINT = 10, SIGMA = 1.2, BINS = MATRIX_SIZE)
	#matrix = GenerateSartheDensityMatrix(BINS = MATRIX_SIZE)

	#MatrixParis = DensityMatrix.GenerateParisDensityMatrix(NUM_OF_HOTPOINT = 1, SIGMA = 1.1, BINS = MATRIX_SIZE)

	"""
	matrix = np.array([[ 4454,  7979,   505],
 						[ 5690, 10020,   602],
 						[  243,   461,    46]])
 	"""

	
	matrix = np.array([[ 10,  0, 0, 10],
							 [ 0,  0, 0, 0],
							 [ 0,  0, 0, 0],
							 [ 10,  0, 0, 10]])
	
	
	originalPoint = [(1,1), (4,4), (1,4), (4,1)]

	resultPoints1 = [(2,4), (3,4), (4,4),
						  (2,3),        (4,3),
						  (2,2), (3,2), (4,2),]

	resultPoints2 = [(1,5), (2,5), (3,5), (4,5), (5,5),
						  (1,4), (2,4), (3,4), (4,4), (5,4),
						  (1,3),	(2,3),        (4,3), (5,3),
						  (1,2), (2,2), (3,2), (4,2), (5,2),
						  (1,1), (2,1), (3,1), (4,1), (5,1)]


	extent = [-5, 5, -5, 5]
	MatrixLen = len(matrix)
	offset = (10/MatrixLen)*(math.sqrt(2)/3)
	plt.imshow(matrix, cmap='autumn_r', extent=extent, origin='lower')

	for point in originalPoint:
		
		x = point[0]
		y = point[1]

		x = x*10/MatrixLen - 5
		y = y*10/MatrixLen - 5

		plt.scatter(x - offset, y - offset, s=200, c="green", marker='o') #s=500/MATRIX_SIZE
		"""
	for point in resultPoints1:
		
		x = point[0]
		y = point[1]

		x = x*10/MatrixLen - 5
		y = y*10/MatrixLen - 5

		plt.scatter(x - offset, y - offset, s=200, c="royalblue", marker='o') #s=500/MATRIX_SIZE
"""
	plt.show()
	"""
	plt.imshow(matrix, cmap='autumn_r', extent=extent, origin='lower')
		
	for point in originalPoint:
		
		x = point[0]
		y = point[1]

		x = x*10/MatrixLen - 5
		y = y*10/MatrixLen - 5

		plt.scatter(x - offset, y - offset, s=200, c="green", marker='o') #s=500/MATRIX_SIZE

	for point in resultPoints1:
		
		x = point[0]
		y = point[1]

		x = x*10/MatrixLen - 5
		y = y*10/MatrixLen - 5

		plt.scatter(x - offset, y - offset, s=200, c="royalblue", marker='o') #s=500/MATRIX_SIZE

	for point in resultPoints2:
		
		x = point[0]
		y = point[1]

		x = x*10/MatrixLen - 5
		y = y*10/MatrixLen - 5

		plt.scatter(x - offset, y - offset, s=200, c="royalblue", marker='o') #s=500/MATRIX_SIZE
	"""
	
	#Solve this matrix with the Greedy Algorithm
	greedyResult = GreedyAlgorithm.Execute(matrix, NUM_OF_POINTS = NUM_OF_HOSPITALS, NUM_OF_LOOPS = LOOP)
	
	#Solve this matrix with the Simulated Annealing Algorithm
	initialTemp = 100
	endingTemp = 0
	#annealingResult = RecuitSimuleAlgorithm.Execute(matrix, NUM_OF_POINTS = NUM_OF_HOSPITALS, INITIAL_TEMP = initialTemp, ENDING_TEMP = endingTemp, GRADIENT = (initialTemp - endingTemp)/LOOP, alpha = 100)

	#Solve this matrix with tight neighborhood
	#tightNeighborhoodResult = GreedyAlgorithm.Execute(matrix, NUM_OF_POINTS = NUM_OF_HOSPITALS, INITIAL_SOLUTION = annealingResult[0], NEIGHBOR_RANGE = MATRIX_SIZE/10, NUM_OF_LOOPS = LOOP)

	#Solve this matrix with the Genetic Algorithm
	POPULATION_SIZE = 100
	#geneticResult = GeneticAlgorithm.Execute(matrix, NUM_OF_POINTS = NUM_OF_HOSPITALS, NUM_OF_LOOPS = int(LOOP/10), POPULATION_SIZE = POPULATION_SIZE, MUTATION_RATE = 0.1)

	#Solve this matrix with taboo search
	#tabooSearchResult = TabooSearchAlgorithm.Execute(matrix, NUM_OF_POINTS = NUM_OF_HOSPITALS, NUM_OF_LOOPS = 50, NEIGHBOR_RANGE = 5)
	
	

	#addMethodToComparaison(greedyResult[2], greedyResult[0], matrix, "magenta", "green", "Méthode Gloutonne", handles)	
	#addMethodToComparaison(annealingResult[2], annealingResult[0], matrix, "orangered", "darkviolet", "Méthode du Recuit Simulé", handles)
	#addMethodToComparaison(tightNeighborhoodResult[2], tightNeighborhoodResult[0], matrix, "green", "lightblue", "Méthode du Recuit Simulé + voisinage serré", handles)
	#addMethodToComparaison(geneticResult[2], geneticResult[0], matrix, "royalblue", "royalblue", "Méthode génétique")
	#addMethodToComparaison(tabooSearchResult[2], tabooSearchResult[0], matrix, "darkred", "green", "Méthode de la recherche taboo")


	extent = [-5, 5, -5, 5]
	offset = (10/MATRIX_SIZE)*(math.sqrt(2)/3)
	
	plot1 = plt.figure(1)
	plt.title("Comparaison des méthodes d'optimisation")
	plt.plot([k for k in range(len(greedyResult[2]))], greedyResult[2], label = "Méthode Gloutonne", color="magenta")
	#plt.plot([k for k in range(len(annealingResult[2]))], annealingResult[2], label = "Méthode du Recuit Simulé", color="orangered")
	#plt.plot([k for k in range(len(tightNeighborhoodResult[2]))], tightNeighborhoodResult[2], label = "Méthode du Recuit Simulé + voisinage serré", color="green")
	#plt.plot([k for k in range(len(geneticResult[2]))], geneticResult[2], label = "Méthode génétique", color="royalblue")
	#plt.plot([k for k in range(len(tabooSearchResult[2]))], tabooSearchResult[2], label = "Méthode de la recherche taboo", color="chartreuse")
	plt.legend(loc="best")

	plot2 = plt.figure(2)
	plt.imshow(matrix, cmap='autumn_r', extent=extent, origin='lower')
	
	for point in greedyResult[0]:
		
		x = point[0]
		y = point[1]

		x = x*10/MATRIX_SIZE - 5
		y = y*10/MATRIX_SIZE - 5

		plt.scatter(x - offset, y - offset, s=500/MATRIX_SIZE, c='green', marker='o')

	"""
	for point in annealingResult[0]:
		
		x = point[0]
		y = point[1]

		x = x*10/MATRIX_SIZE - 5
		y = y*10/MATRIX_SIZE - 5

		plt.scatter(x - offset, y - offset, s=500/MATRIX_SIZE, c='darkviolet', marker='o')

	for point in tightNeighborhoodResult[0]:
		
		x = point[0]
		y = point[1]

		x = x*10/MATRIX_SIZE - 5
		y = y*10/MATRIX_SIZE - 5

		plt.scatter(x - offset, y - offset, s=500/MATRIX_SIZE, c='lightblue', marker='o')

	for point in geneticResult[0]:
		
		x = point[0]
		y = point[1]

		x = x*10/MATRIX_SIZE - 5
		y = y*10/MATRIX_SIZE - 5

		plt.scatter(x - offset, y - offset, s=500/MATRIX_SIZE, c='royalblue', marker='o')
	
	
	for point in tabooSearchResult[0]:
		
		x = point[0]
		y = point[1]
		x = x*10/MATRIX_SIZE - 5
		y = y*10/MATRIX_SIZE - 5
		plt.scatter(x - offset, y - offset, s=500/MATRIX_SIZE, c='royalblue', marker='o')
	"""

	plt.show()


if __name__=="__main__":
	logging.config.fileConfig(fname="logger.ini", disable_existing_loggers=False)
	logger = logging.getLogger(__name__)
	logger.info('Logging enabled')
	main()