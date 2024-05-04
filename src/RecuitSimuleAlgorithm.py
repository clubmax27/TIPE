from RandomSolution import RandomSolution
from NeighborSolution import GenerateNeighborSolution
from EvaluateFunction import evaluate

from progress.bar import Bar

import random
import numpy as np

class RecuitSimuleAlgorithm:

	def Execute(Matrix, NUM_OF_POINTS = 10, INITIAL_TEMP = 300, ENDING_TEMP = 0.1, GRADIENT = 0.1, alpha = 200):

		shape = Matrix.shape
		MatrixSize = shape[0]
		scoreHistory = []

		#On commence a partir d'une solution aléatoire
		solution = RandomSolution.GenerateRandomSolution(MatrixSize, NUM_OF_POINTS)
		solutionScore = evaluate(Matrix, solution)[0]

		bestSolution = solution
		bestSolutionScore = solutionScore

		currentTemp = INITIAL_TEMP #On initialise la température 

		#Pour chaque itération, on modifie une coordonnée d'un point, on regarde si le résultat est positif
		#Si oui, on accepte la solution
		#Si non, on compare la différence de score avec le facteur de Boltzman

		MAX = ((INITIAL_TEMP - ENDING_TEMP)/GRADIENT)
		with Bar('Recuit Simulé Algorithm', max= MAX, suffix='%(percent)d%%') as bar:

			while currentTemp > ENDING_TEMP:

				newSolution = GenerateNeighborSolution(solution, MatrixSize, MatrixSize/4)
				newSolutionScore = evaluate(Matrix, newSolution)[0]

				scoreDifference = solutionScore - newSolutionScore

				if newSolutionScore < bestSolutionScore:
					bestSolution = newSolution
					bestSolutionScore = newSolutionScore

				if scoreDifference > 0: #Si le score est meilleur ou si le changement n'est pas trop brutal
					solution = newSolution
					solutionScore = newSolutionScore
				else:
					temp = random.random()
					if temp < np.exp((scoreDifference / currentTemp)/alpha):
						solution = newSolution
						solutionScore = newSolutionScore


				currentTemp -= GRADIENT

				scoreHistory.append(solutionScore)

				bar.next()

		bar.finish()

		return (bestSolution, bestSolutionScore, scoreHistory)