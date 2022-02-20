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

		#Generate initial population smaller than population size
		population = np.empty((POPULATION_SIZE,), dtype=object)
		for k in range(int(POPULATION_SIZE/2)):
			population[k] = RandomSolution.GenerateRandomSolution(MatrixSize, NUM_OF_POINTS)

		with Bar('Genetic Algorithm', max=NUM_OF_LOOPS, suffix='%(percent)d%%') as bar:

			#For each generation
			for _ in range(NUM_OF_LOOPS):

				sizeOfCurrentPopulation = 0
				for k in range(POPULATION_SIZE):
					if isinstance(population[k], Iterable):
						sizeOfCurrentPopulation = k + 1

				#We reproduce the current generation, and apply a mutation at a very low rate
				while sizeOfCurrentPopulation < POPULATION_SIZE:

					#We take two parents randomly
					parent1 = np.random.randint(0, sizeOfCurrentPopulation)
					parent2 = np.random.randint(0, sizeOfCurrentPopulation)
					while parent1 == parent2:
						parent2 = np.random.randint(0, sizeOfCurrentPopulation)

					separationIndex = np.random.randint(0, NUM_OF_POINTS - 1)

					#We create two children
					child1 = np.empty((NUM_OF_POINTS,), dtype=object)
					child2 = np.empty((NUM_OF_POINTS,), dtype=object)

					#We swap points
					for k in range(NUM_OF_POINTS):
						if k <= separationIndex:
							child1[k] = population[parent1][k]
							child2[k] = population[parent2][k]
						else:
							child1[k] = population[parent2][k]
							child2[k] = population[parent1][k]

					#If two population slot are ready
					if sizeOfCurrentPopulation != POPULATION_SIZE - 1:
						population[sizeOfCurrentPopulation] = child1
						sizeOfCurrentPopulation += 1

					population[sizeOfCurrentPopulation] = child2
					sizeOfCurrentPopulation += 1

				for solution in population:

					#We mutate a select few solutions
					if random.random() < MUTATION_RATE:
						randomPoint = np.random.randint(0, NUM_OF_POINTS)
						solution[randomPoint] = RandomSolution.GenerateRandomPoint(MatrixSize)

				#Then, we filter the worst result
				scores = []
				for solution in population:
					scores.append(evaluate(Matrix, solution)[0])

				#We get rid of half of the population
				sortedScores = scores.copy()
				sortedScores.sort()
				thresholdScore = sortedScores[POPULATION_SIZE//2]

				newPopulation = np.empty((POPULATION_SIZE,), dtype=object)
				sizeOfCurrentPopulation = 0
				
				for k in range(POPULATION_SIZE):
					if scores[k] <= thresholdScore:
						newPopulation[sizeOfCurrentPopulation] = population[k]
						sizeOfCurrentPopulation += 1

				#We set the new population
				np.copyto(population, newPopulation)

				scoreHistory.append(thresholdScore)

				bar.next()

		bar.finish()

		solution = population[0]
		solutionScore = evaluate(Matrix, solution)[0]

		return (solution, solutionScore, scoreHistory)