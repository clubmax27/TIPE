from RandomSolution import RandomSolution
from NeighborSolution import GenerateNeighborSolution
from EvaluateFunction import evaluate

from progress.bar import Bar

class GreedyAlgorithm:

	def Execute(Matrix, NUM_OF_POINTS = 10, NUM_OF_LOOPS = 1000, INITIAL_SOLUTION = [(-1, -1)], NEIGHBOR_RANGE = -1):

		shape = Matrix.shape
		MatrixSize = shape[0]
		scoreHistory = []

		#On commence a partir d'une solution aléatoire
		if INITIAL_SOLUTION[0] == (-1, -1):
			solution = RandomSolution.GenerateRandomSolution(MatrixSize, NUM_OF_POINTS)
		else:
			solution = INITIAL_SOLUTION

		solutionScore = evaluate(Matrix, solution)[0]

		with Bar('Greedy Algorithm', max=NUM_OF_LOOPS, suffix='%(percent)d%%') as bar:
			#Pour chaque itération, on modifie une coordonnée d'un point, on regarde si le résultat est positif, et si oui, on accepte la solution
			for _ in range(NUM_OF_LOOPS):

				newSolution = GenerateNeighborSolution(solution, MatrixSize, NEIGHBOR_RANGE = NEIGHBOR_RANGE)

				newSolutionScore = evaluate(Matrix, newSolution)[0]

				if newSolutionScore < solutionScore: #Our change made the score better
					solution = newSolution
					solutionScore = newSolutionScore
				scoreHistory.append(solutionScore)

				bar.next()

		bar.finish()

		return (solution, solutionScore, scoreHistory)