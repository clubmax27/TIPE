from shapely.geometry import Polygon
from shapely.ops import unary_union
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import json
import math
import numpy as np
from progress.bar import Bar

def GenerateSartheDensityMatrix(BINS = 50):

		polygons = []

		f = open('Sarthe.json')
		regions = json.load(f)

		for region in regions:
			sousregions = region["fields"]["geo_shape"]["coordinates"]

			population = region["fields"]["pop_m"]
			if len(sousregions) > 1: #Il y a plusieurs sous-régions
				sousPolygons = []
				for sousregion in sousregions:
					sousPolygons.append(GeneratePolygonFromRegionCoordinates(sousregion[0]))
				polygons.append((unary_union(sousPolygons), population))
			else:
				polygons.append((GeneratePolygonFromRegionCoordinates(sousregions[0]), population))


		x_points = []
		y_points = []
		weights_points = []
		
		with Bar('Generating Sarthe\'s Density Matrix', max=(BINS**2), suffix='%(percent)d%%') as bar:
			increment = 10/BINS
			for x in [-5 + k*increment for k in range(BINS)]:
				for y in [-5 + (10*k)/BINS for k in range(BINS)]:
					carre = Polygon([(x,y), (x + increment, y), (x + increment, y + increment), (x, y + increment)])
					population = 0
					for region in polygons:
						region_ratio = region[0].intersection(carre).area / region[0].area
						population += region_ratio*region[1]

					MAX_VALUE = 8000000/(BINS**2)
					population = (population if population < MAX_VALUE else MAX_VALUE)
					population = 1.01**population
					population = (0 if population == 1 else population)

					offset = (10/BINS)*(math.sqrt(2)/3)
					x_points.append(x + offset)
					y_points.append(y + offset)
					weights_points.append(population)
					bar.next()
			bar.finish()


		Matrix, xedges, yedges = np.histogram2d(x_points, y_points, bins=BINS, weights=weights_points)

		return Matrix.T

def addPoint(x,y):
	plt.scatter(x, y, s=30, c="green", marker='o')
		

def showPolygons(polygons):
	for polygon in polygons:
			polygon = polygon[0]
			if polygon.geom_type == 'MultiPolygon':
				for ComposedPolygon in polygon:
					plotPolygon(ComposedPolygon)
			else:
				plotPolygon(polygon)
	#plt.show()

def plotPolygon(polygon):
	plot1 = plt.figure(2)
	x,y = polygon.exterior.xy
	plt.plot(x,y)

			

def GeneratePolygonFromRegionCoordinates(coordinates):
	coordinatesFormated = []

	for coordinate in coordinates:
		coordinatesFormated.append(scaleCoordinates((coordinate[0], coordinate[1])))

	return Polygon(coordinatesFormated)

def scaleCoordinates(coordinates):
	x, y = coordinates
	MAX_X = 0.9166393287033451
	MIN_X = -0.44792479429320703
	MAX_Y = 48.48457244265838
	MIN_Y = 47.56852419552297

	xoffset = -(MAX_X + MIN_X)/2
	yoffset = -(MAX_Y + MIN_Y)/2

	xmultiplcator = abs(5/(MAX_X + xoffset))
	ymultiplcator = abs(5/(MAX_Y + yoffset))

	return (xmultiplcator*(x + xoffset), ymultiplcator*(y + yoffset))
