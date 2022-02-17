import random
import numpy as np

def GenerateNeighboorSolution(solution, SIZE_OF_MATRIX, neighboorRange = -1, pointId = -1): #Returns a NeighboorSolution
	NUM_OF_POINTS = len(solution)

	if pointId == -1:
		pointId = random.randint(0, NUM_OF_POINTS - 1) #Choose a random point

	randomAxis = random.randint(0, 1)
	randomCoordinate = (SIZE_OF_MATRIX + 1, SIZE_OF_MATRIX)

	while not ((0 <= randomCoordinate[0] <= SIZE_OF_MATRIX) and 
			   (0 <= randomCoordinate[1] <= SIZE_OF_MATRIX)): #We do this to prevent the coordinate from being on the border
		if neighboorRange == -1: #If there is no range, the range is the entire matrix
			randomCoordinate = (int(random.random()*SIZE_OF_MATRIX), int(random.random()*SIZE_OF_MATRIX))
		else:
			randomCoordinate = (solution[pointId][0] + int(random.random()*neighboorRange*2 - neighboorRange),
								solution[pointId][1] + int(random.random()*neighboorRange*2 - neighboorRange))


	solutionCopy = np.empty((NUM_OF_POINTS,), dtype=object) #We operate on a copy of the solution

	for k in range(NUM_OF_POINTS):
		if k == pointId:
			solutionCopy[k] = randomCoordinate
		else:
			solutionCopy[k] = solution[k]

	return solutionCopy