from RandomSolution import RandomSolution
from EvaluateFunction import evaluate

import random
import numpy as np

class GreedyAlgorithm:

	def Execute(Matrix, NUM_OF_POINTS = 10, NUM_OF_LOOPS = 1000):

		shape = Matrix.shape
		MatrixSize = shape[0]

		#We start off from a random solution
		solution = RandomSolution.GenerateRandomSolution(MatrixSize, NUM_OF_POINTS)
		solutionScore = evaluate(Matrix, solution)[0]

		#For each cycle of the loop, we modify one coordinate of one point randomly, see if the result is positive, and act accordingly
		for _ in range(NUM_OF_LOOPS):
			randomPoint = random.randint(0, NUM_OF_POINTS - 1) #Choose a random point

			randomAxis = random.randint(0, 1)
			randomCoordinate = MatrixSize
			while (randomCoordinate == MatrixSize): #Improbable situation, but better safe than sorry
				randomCoordinate = int(random.random()*MatrixSize)



			solutionCopy = np.empty((NUM_OF_POINTS,), dtype=object) #We operate on a copy of the solution

			for k in range(NUM_OF_POINTS):
				if k == randomPoint:
					if randomAxis == 0: #if the axis is x
						solutionCopy[k] = (randomCoordinate, solution[k][1])
					else:
						solutionCopy[k] = (solution[k][0], randomCoordinate)
				else:
					solutionCopy[k] = solution[k]

		#	solutionCopy[randomPoint][randomAxis] = randomCoordinate

			solutionCopyScore = evaluate(Matrix, solutionCopy)[0]

			if solutionCopyScore < solutionScore: #Our change made the score better
				solution = solutionCopy
				solutionScore = solutionCopyScore

		return (solution, solutionScore)