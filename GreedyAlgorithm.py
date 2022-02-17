from RandomSolution import RandomSolution
from NeighboorSolution import GenerateNeighboorSolution
from EvaluateFunction import evaluate

class GreedyAlgorithm:

	def Execute(Matrix, NUM_OF_POINTS = 10, NUM_OF_LOOPS = 1000):

		shape = Matrix.shape
		MatrixSize = shape[0]
		scoreHistory = []

		#We start off from a random solution
		solution = RandomSolution.GenerateRandomSolution(MatrixSize, NUM_OF_POINTS)
		solutionScore = evaluate(Matrix, solution)[0]

		#For each cycle of the loop, we modify one coordinate of one point randomly, see if the result is positive, and act accordingly
		for _ in range(NUM_OF_LOOPS):

			newSolution = GenerateNeighboorSolution(solution, MatrixSize, MatrixSize/2)

			newSolutionScore = evaluate(Matrix, newSolution)[0]

			if newSolutionScore < solutionScore: #Our change made the score better
				solution = newSolution
				solutionScore = newSolutionScore
			scoreHistory.append(solutionScore)

		return (solution, solutionScore, scoreHistory)