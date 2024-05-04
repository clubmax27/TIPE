from EvaluateFunction import evaluate

import time
import scipy.special
import numpy as np

class RandomSolution:

	def __binomialCoefficient(k, n):
		return scipy.special.binom(n, k)

	def GenerateRandomPoint(MatrixSize):
		x = MatrixSize
		y = MatrixSize

		while (x == MatrixSize or y == MatrixSize): #Improbable situation, but better safe than sorry
			x = int(np.random.rand()*MatrixSize) + 1
			y = int(np.random.rand()*MatrixSize) + 1

		return (x,y)

	def GenerateRandomSolution(MatrixSize, NUM_OF_POINTS = 10):
		solution = np.empty((NUM_OF_POINTS,), dtype=object)

		for k in range(NUM_OF_POINTS):
			point = RandomSolution.GenerateRandomPoint(MatrixSize)
			solution[k] = point

		return solution

	def EstimateTimeAllSolutions(Matrix, NUM_OF_POINTS = 10, NUM_OF_SOLUTIONS = 10):
		solutions = np.empty((NUM_OF_SOLUTIONS,), dtype=object)

		shape = Matrix.shape
		MatrixSize = shape[0]

		initialTime = time.time()

		for k in range(NUM_OF_SOLUTIONS):
			solution = RandomSolution.GenerateRandomSolution(MatrixSize, NUM_OF_POINTS)
			solutions[k] = solution

		for k in range(NUM_OF_SOLUTIONS):
			evaluate(Matrix, solutions[k])[0]

		finishTime = time.time()
		computationTime = finishTime - initialTime

		print("Time it took to compute 100 solutions : {}s".format(computationTime))
		print("Time it would take to compute all solutions : {}s".format(computationTime*RandomSolution.__binomialCoefficient(NUM_OF_POINTS, MatrixSize**2)/NUM_OF_SOLUTIONS))
