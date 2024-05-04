from RandomSolution import RandomSolution
from NeighborSolution import GenerateNeighborSolution
from EvaluateFunction import evaluate

from progress.bar import Bar

import numpy as np
import random
from collections.abc import Iterable

class GeneticAlgorithm:

	def Execute(Matrix, NUM_OF_POINTS = 10, NUM_OF_LOOPS = 1000, POPULATION_SIZE = 20, MUTATION_RATE = 0.05):

		shape = Matrix.shape
		MatrixSize = shape[0]
		scoreHistory = []

		#On génère une population initiale
		population = np.empty((POPULATION_SIZE,), dtype=object)
		for k in range(int(POPULATION_SIZE/2)):
			population[k] = RandomSolution.GenerateRandomSolution(MatrixSize, NUM_OF_POINTS)

		with Bar('Genetic Algorithm', max=NUM_OF_LOOPS, suffix='%(percent)d%%') as bar:

			#Pour chaque génération
			for _ in range(NUM_OF_LOOPS):

				sizeOfCurrentPopulation = 0
				for k in range(POPULATION_SIZE):
					if isinstance(population[k], Iterable):
						sizeOfCurrentPopulation = k + 1

				#On reproduit la population actuelle
				while sizeOfCurrentPopulation < POPULATION_SIZE:

					#On choisit deux parents
					parent1 = np.random.randint(0, sizeOfCurrentPopulation)
					parent2 = np.random.randint(0, sizeOfCurrentPopulation)
					while parent1 == parent2:
						parent2 = np.random.randint(0, sizeOfCurrentPopulation)

					separationIndex = np.random.randint(0, NUM_OF_POINTS - 1)

					#On crée deux enfants
					child1 = np.empty((NUM_OF_POINTS,), dtype=object)
					child2 = np.empty((NUM_OF_POINTS,), dtype=object)

					#On coupe des gènes des parents en deux, et on les injecte dans les enfants
					for k in range(NUM_OF_POINTS):
						if k <= separationIndex:
							child1[k] = population[parent1][k]
							child2[k] = population[parent2][k]
						else:
							child1[k] = population[parent2][k]
							child2[k] = population[parent1][k]

					#On ajotue les enfants à la population
					if sizeOfCurrentPopulation != POPULATION_SIZE - 1:
						population[sizeOfCurrentPopulation] = child1
						sizeOfCurrentPopulation += 1

					population[sizeOfCurrentPopulation] = child2
					sizeOfCurrentPopulation += 1

				for solution in population:

					#On mute queleques éléments de la population
					if random.random() < MUTATION_RATE:
						randomPoint = np.random.randint(0, NUM_OF_POINTS)
						solution[randomPoint] = RandomSolution.GenerateRandomPoint(MatrixSize)

				#On filtre les pires candidats
				scores = []
				for solution in population:
					scores.append(evaluate(Matrix, solution)[0])

				#On supprime la moitié de la population
				sortedScores = scores.copy()
				sortedScores.sort()
				thresholdScore = sortedScores[POPULATION_SIZE//2]

				newPopulation = np.empty((POPULATION_SIZE,), dtype=object)
				sizeOfCurrentPopulation = 0
				
				for k in range(POPULATION_SIZE):
					if scores[k] <= thresholdScore:
						newPopulation[sizeOfCurrentPopulation] = population[k]
						sizeOfCurrentPopulation += 1

				#On définit la nouvelle population
				np.copyto(population, newPopulation)

				scoreHistory.append(thresholdScore)
				scoreHistory.append(thresholdScore)
				scoreHistory.append(thresholdScore)
				scoreHistory.append(thresholdScore)
				scoreHistory.append(thresholdScore)
				scoreHistory.append(thresholdScore)
				scoreHistory.append(thresholdScore)
				scoreHistory.append(thresholdScore)
				scoreHistory.append(thresholdScore)
				scoreHistory.append(thresholdScore)

				bar.next()

		bar.finish()

		solution = population[0]
		solutionScore = evaluate(Matrix, solution)[0]

		return (solution, solutionScore, scoreHistory)