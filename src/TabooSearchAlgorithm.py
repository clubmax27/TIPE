from RandomSolution import RandomSolution
from NeighborSolution import GenerateNeighborSolution
from EvaluateFunction import evaluate

import numpy as np
import random
from collections import deque

from progress.bar import Bar

class TabooSearchAlgorithm:

	def Execute(Matrix, NUM_OF_POINTS = 10, NUM_OF_LOOPS = 1000, INITIAL_SOLUTION = [(-1, -1)], NEIGHBOR_RANGE = -1, STACK_SIZE = 3):

		shape = Matrix.shape
		MatrixSize = shape[0]
		scoreHistory = []
		tabooStack = deque([], STACK_SIZE)

		#We start off from a random solution
		if INITIAL_SOLUTION[0] == (-1, -1):
			INITIAL_SOLUTION = RandomSolution.GenerateRandomSolution(MatrixSize, NUM_OF_POINTS)

		with Bar('Taboo Search Algorithm', max=NUM_OF_LOOPS, suffix='%(percent)d%%') as bar:
			#For each cycle of the loop, we modify one coordinate of one point randomly, see if the result is positive, and act accordingly

			currentSolution = INITIAL_SOLUTION
			currentSolutionScore = evaluate(Matrix, currentSolution)[0]

			for _ in range(NUM_OF_LOOPS):

				bestSolution = np.empty((NUM_OF_POINTS,), dtype=object)
				bestSolutionScore = np.inf

				#Choose a random point
				pointId = random.randint(0, NUM_OF_POINTS - 1) 

				#We can't use float in a range, so we convert it to int
				NEIGHBOR_RANGE = int(NEIGHBOR_RANGE)

				#For every point in the neighborhood
				for x in range(-NEIGHBOR_RANGE, NEIGHBOR_RANGE): 
					for y in range(-NEIGHBOR_RANGE, NEIGHBOR_RANGE):

						#We create the neighbor point
						randomCoordinate = (currentSolution[pointId][0] + x, 
											currentSolution[pointId][1] + y)

						#We do this to prevent the coordinate from being on the border, or the current solution
						if (not (1 <= randomCoordinate[0] <= MatrixSize) or 
							not (1 <= randomCoordinate[1] <= MatrixSize) or
							(x == 0 and y == 0)):
							continue			

						#We operate on a copy of the solution
						solutionCopy = np.empty((NUM_OF_POINTS,), dtype=object) 
						for k in range(NUM_OF_POINTS):
							if k == pointId:
								solutionCopy[k] = randomCoordinate
							else:
								solutionCopy[k] = currentSolution[k]

						#If the solution is taboo, we skip
						for tabooSolution in tabooStack:
							if np.array_equal(tabooSolution, solutionCopy):
								print("Solution was tabooed")
								continue

						solutionScore = evaluate(Matrix, solutionCopy)[0]

						#If the score is better, we keep it
						if solutionScore < bestSolutionScore:
							np.copyto(bestSolution, solutionCopy)
							bestSolutionScore = solutionScore

				#We add this solution to the stack
				tabooStack.appendleft(bestSolution)
				scoreHistory.append(bestSolutionScore)

				bar.next()

		bar.finish()

		return (bestSolution, bestSolutionScore, scoreHistory)