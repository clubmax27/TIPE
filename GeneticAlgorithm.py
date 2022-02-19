from RandomSolution import RandomSolution
from NeighborSolution import GenerateNeighborSolution
from EvaluateFunction import evaluate

from progress.bar import Bar

class GeneticAlgorithm:

	def Execute(Matrix, NUM_OF_POINTS = 10, NUM_OF_LOOPS = 1000, POPULATION_SIZE = 10, MUTATION_RATE = 0.05):

		shape = Matrix.shape
		MatrixSize = shape[0]
		scoreHistory = []

		#Generate initial population smaller than population size
		population = []
		for _ in range(int(POPULATION_SIZE/2)):
			population.append(RandomSolution.GenerateRandomSolution(MatrixSize, NUM_OF_POINTS))

		with Bar('Genetic Algorithm', max=NUM_OF_LOOPS, suffix='%(percent)d%%') as bar:

			#For each generation
			for _ in range(NUM_OF_LOOPS):

				#We reproduce the current generation, and apply a mutation at a very low rate


				bar.next()

		bar.finish()

		return (solution, solutionScore, scoreHistory)