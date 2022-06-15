import numpy as np

from progress.bar import Bar

class DensityMatrix:

	def GenerateDensityMatrix(NUM_OF_HOTPOINT = 10, NUM_OF_POINTS_PER_HOTPOINT = 10000, SIGMA = 1.2, BINS = 100):
	
		NUM_OF_POINTS_PER_HOTPOINT = NUM_OF_POINTS_PER_HOTPOINT*BINS #We have to scale the number of people to the number of bins, or else it looks ugly
		#NUM_OF_POINTS_PER_HOTPOINT = 10000
		#SIGMA = 1.2

		x = []
		y = []

		#Choose 10 hotpoints with coordinates in [-5, 5]
		hottestPoints = [((np.random.rand()*10 - 5), (np.random.rand()*10 - 5)) for _ in range(NUM_OF_HOTPOINT)]
		#hottestPoints = [(5,5), (-5, -5)]

		with Bar('Generating Density Matrix', max=2*NUM_OF_HOTPOINT, suffix='%(percent)d%%') as bar:
			for i in range(NUM_OF_HOTPOINT):

				x_hotpoint, y_hotpoint = hottestPoints[i]

				while len(x) < NUM_OF_POINTS_PER_HOTPOINT * (i + 1):
					point = SIGMA * np.random.randn() + x_hotpoint
					if -5 < point < 5:
						x.append(point)
				bar.next()

				while len(y) < NUM_OF_POINTS_PER_HOTPOINT * (i + 1):
					point = SIGMA * np.random.randn() + y_hotpoint
					if -5 < point < 5:
						y.append(point)
				bar.next()

			#print(hottestPoints)
			bar.finish()


		heatmap, xedges, yedges = np.histogram2d(x, y, bins=BINS)

		return heatmap


	def GenerateParisDensityMatrix(NUM_OF_HOTPOINT = 10, NUM_OF_POINTS_PER_HOTPOINT = 10000, SIGMA = 1.2, BINS = 100):
	
		NUM_OF_POINTS_PER_HOTPOINT = NUM_OF_POINTS_PER_HOTPOINT*BINS #We have to scale the number of people to the number of bins, or else it looks ugly
		#NUM_OF_POINTS_PER_HOTPOINT = 10000
		#SIGMA = 1.2

		x = []
		y = []

		#Choose 10 hotpoints with coordinates in [-5, 5]
		hottestPoints = [((np.random.rand()*10 - 5), (np.random.rand()*10 - 5)) for _ in range(NUM_OF_HOTPOINT)]
		#hottestPoints = [(5,5), (-5, -5)]

		with Bar('Generating Density Matrix', max=2*NUM_OF_HOTPOINT, suffix='%(percent)d%%') as bar:
			for i in range(NUM_OF_HOTPOINT):

				x_hotpoint, y_hotpoint = hottestPoints[i]

				while len(x) < NUM_OF_POINTS_PER_HOTPOINT * (i + 1):
					point = SIGMA * np.random.randn() + x_hotpoint
					if -5 < point < 5:
						x.append(point)
				bar.next()

				while len(y) < NUM_OF_POINTS_PER_HOTPOINT * (i + 1):
					point = SIGMA * np.random.randn() + y_hotpoint
					if -5 < point < 5:
						y.append(point)
				bar.next()

			#print(hottestPoints)
			bar.finish()


		heatmap, xedges, yedges = np.histogram2d(x, y, bins=BINS)

		return heatmap