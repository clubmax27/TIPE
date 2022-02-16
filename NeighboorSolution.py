import random
import numpy as np

def GenerateNeighboorSolution(solution, SIZE_OF_MATRIX, neighboorRange = -1, pointId = -1): #Returns a NeighboorSolution
	NUM_OF_POINTS = len(solution)

	if pointId == -1:
		pointId = random.randint(0, NUM_OF_POINTS - 1) #Choose a random point

	randomAxis = random.randint(0, 1)
	randomCoordinate = SIZE_OF_MATRIX + 1

	while not (1 <= randomCoordinate <= SIZE_OF_MATRIX): #We do this to prevent the coordinate from being on the border
		if neighboorRange == -1: #If there is no range, the range is the entire matrix
			randomCoordinate = int(random.random()*SIZE_OF_MATRIX)
		else:
			randomCoordinate = solution[pointId][randomAxis] + int(random.random()*neighboorRange*2 - neighboorRange)

	if randomAxis == 0:
		solution[pointId] = (solution[pointId][0], randomCoordinate)
	else:
		solution[pointId] = (randomCoordinate, solution[pointId][1])

	return solution