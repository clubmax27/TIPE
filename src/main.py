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

import config

def main():

	#Generate the Matix
	if config.MATRIX_TYPE == "SARTHE":
		matrix = GenerateSartheDensityMatrix(BINS = config.MATRIX_SIZE)
	else:
		matrix = DensityMatrix.GenerateDensityMatrix(NUM_OF_HOTPOINT = 10, SIGMA = 1.2, BINS = config.MATRIX_SIZE)


	if config.SOLVE_GREEDY:
		#Solve this matrix with the Greedy Algorithm
		greedyResult = GreedyAlgorithm.Execute(matrix, NUM_OF_POINTS = config.NUM_OF_HOSPITALS, NUM_OF_LOOPS = config.LOOP)
		
	if config.SOLVE_ANNEALING:
		#Solve this matrix with the Simulated Annealing Algorithm
		initialTemp = 100
		endingTemp = 0
		annealingResult = RecuitSimuleAlgorithm.Execute(matrix, NUM_OF_POINTS = config.NUM_OF_HOSPITALS, INITIAL_TEMP = initialTemp, ENDING_TEMP = endingTemp, GRADIENT = (initialTemp - endingTemp)/config.LOOP, alpha = 100)

	if config.SOLVE_TIGHT_NEIGHBORHOOD:
		if not config.SOLVE_ANNEALING:
			#Solve this matrix with the Simulated Annealing Algorithm
			initialTemp = 100
			endingTemp = 0
			annealingResult = RecuitSimuleAlgorithm.Execute(matrix, NUM_OF_POINTS = config.NUM_OF_HOSPITALS, INITIAL_TEMP = initialTemp, ENDING_TEMP = endingTemp, GRADIENT = (initialTemp - endingTemp)/config.LOOP, alpha = 100)

		#Solve this matrix with tight neighborhood
		tightNeighborhoodResult = GreedyAlgorithm.Execute(matrix, NUM_OF_POINTS = config.NUM_OF_HOSPITALS, INITIAL_SOLUTION = annealingResult[0], NEIGHBOR_RANGE = config.MATRIX_SIZE/10, NUM_OF_LOOPS = config.LOOP)

	if config.SOLVE_GENETIC:
		#Solve this matrix with the Genetic Algorithm
		geneticResult = GeneticAlgorithm.Execute(matrix, NUM_OF_POINTS = config.NUM_OF_HOSPITALS, NUM_OF_LOOPS = int(config.LOOP/10), POPULATION_SIZE = config.POPULATION_SIZE, MUTATION_RATE = 0.1)

	if config.SOLVE_TABOO:
		#Solve this matrix with taboo search
		tabooSearchResult = TabooSearchAlgorithm.Execute(matrix, NUM_OF_POINTS = config.NUM_OF_HOSPITALS, NUM_OF_LOOPS = 50, NEIGHBOR_RANGE = 5)
	

	extent = [-5, 5, -5, 5]
	offset = (10/config.MATRIX_SIZE)*(math.sqrt(2)/3)
	
	plot1 = plt.figure(1)
	plt.title("Comparaison des méthodes d'optimisation")

	if config.SOLVE_GREEDY:
		plt.plot([k for k in range(len(greedyResult[2]))], greedyResult[2], label = "Méthode Gloutonne", color="magenta")

	if config.SOLVE_ANNEALING:
		plt.plot([k for k in range(len(annealingResult[2]))], annealingResult[2], label = "Méthode du Recuit Simulé", color="orangered")

	if config.SOLVE_TIGHT_NEIGHBORHOOD:
		plt.plot([k for k in range(len(tightNeighborhoodResult[2]))], tightNeighborhoodResult[2], label = "Méthode du Recuit Simulé + voisinage serré", color="green")

	if config.SOLVE_GENETIC:
		plt.plot([k for k in range(len(geneticResult[2]))], geneticResult[2], label = "Méthode génétique", color="royalblue")

	if config.SOLVE_TABOO:
		plt.plot([k for k in range(len(tabooSearchResult[2]))], tabooSearchResult[2], label = "Méthode de la recherche taboo", color="chartreuse")

	plt.legend(loc="best")

	plot2 = plt.figure(2)
	plt.imshow(matrix, cmap='autumn_r', extent=extent, origin='lower')

	if config.ONLY_SHOW_BEST:
		bestResult = math.inf
		bestAlgorithmPoints = []

		if config.SOLVE_GREEDY:
			bestResult = greedyResult[1] if bestResult > greedyResult[1] else bestResult
			bestAlgorithmPoints = greedyResult[0]

		if config.SOLVE_ANNEALING:
			bestResult = annealingResult[1] if bestResult > annealingResult[1] else bestResult
			bestAlgorithmPoints = annealingResult[0]

		if config.SOLVE_TIGHT_NEIGHBORHOOD:
			bestResult = tightNeighborhoodResult[1] if bestResult > tightNeighborhoodResult[1] else bestResult
			bestAlgorithmPoints = tightNeighborhoodResult[0]

		if config.SOLVE_GENETIC:
			bestResult = geneticResult[1] if bestResult > geneticResult[1] else bestResult
			bestAlgorithmPoints = geneticResult[0]

		if config.SOLVE_TABOO:
			bestResult = tabooSearchResult[1] if bestResult > tabooSearchResult[1] else bestResult
			bestAlgorithmPoints = tabooSearchResult[0]
			
		for point in bestAlgorithmPoints:
			
			x = point[0]
			y = point[1]

			x = x*10/config.MATRIX_SIZE - 5
			y = y*10/config.MATRIX_SIZE - 5

			plt.scatter(x - offset, y - offset, s=500/config.MATRIX_SIZE, c='blueviolet', marker='o')
	
	else:
		if config.SOLVE_GREEDY:
			for point in greedyResult[0]:
				
				x = point[0]
				y = point[1]

				x = x*10/config.MATRIX_SIZE - 5
				y = y*10/config.MATRIX_SIZE - 5

				plt.scatter(x - offset, y - offset, s=500/config.MATRIX_SIZE, c='green', marker='o')

		if config.SOLVE_ANNEALING:
			for point in annealingResult[0]:
				
				x = point[0]
				y = point[1]

				x = x*10/config.MATRIX_SIZE - 5
				y = y*10/config.MATRIX_SIZE - 5

				plt.scatter(x - offset, y - offset, s=500/config.MATRIX_SIZE, c='darkviolet', marker='o')

		if config.SOLVE_TIGHT_NEIGHBORHOOD:
			for point in tightNeighborhoodResult[0]:
				
				x = point[0]
				y = point[1]

				x = x*10/config.MATRIX_SIZE - 5
				y = y*10/config.MATRIX_SIZE - 5

				plt.scatter(x - offset, y - offset, s=500/config.MATRIX_SIZE, c='lightblue', marker='o')

		if config.SOLVE_GENETIC:
			for point in geneticResult[0]:
				
				x = point[0]
				y = point[1]

				x = x*10/config.MATRIX_SIZE - 5
				y = y*10/config.MATRIX_SIZE - 5

				plt.scatter(x - offset, y - offset, s=500/config.MATRIX_SIZE, c='royalblue', marker='o')
		
		if config.SOLVE_TABOO:
			for point in tabooSearchResult[0]:
				
				x = point[0]
				y = point[1]
				x = x*10/config.MATRIX_SIZE - 5
				y = y*10/config.MATRIX_SIZE - 5
				plt.scatter(x - offset, y - offset, s=500/config.MATRIX_SIZE, c='deeppink', marker='o')
			

	plt.show()


if __name__=="__main__":
	logging.config.fileConfig(fname="logger.ini", disable_existing_loggers=False)
	logger = logging.getLogger(__name__)
	logger.info('Logging enabled')
	main()