import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

def marks_per_house_feature(data, feature, house):
	tab = data[data['Hogwarts House'] == house]
	return tab[feature]

if __name__ == "__main__":
	try:
		data = pd.read_csv(sys.argv[1])
	except:
		print("Usage: python3 scatter_plot.py datasets/dataset_train.csv")
		exit (-1)
	#first one
	x1 = marks_per_house_feature(data, "Arithmancy", 'Ravenclaw')
	x2 = marks_per_house_feature(data, "Arithmancy", 'Slytherin')
	x3 = marks_per_house_feature(data, "Arithmancy", 'Gryffindor')
	x4 = marks_per_house_feature(data, "Arithmancy", 'Hufflepuff')
	y1 = marks_per_house_feature(data, "Flying", 'Ravenclaw')
	y2 = marks_per_house_feature(data, "Flying", 'Slytherin')
	y3 = marks_per_house_feature(data, "Flying", 'Gryffindor')
	y4 = marks_per_house_feature(data, "Flying", 'Hufflepuff')
	fig = plt.figure()
	plt.xlabel("Arithmancy")
	plt.ylabel("Flying")
	plt.scatter(x1, y1, label = 'Ravenclaw', marker='*')
	plt.scatter(x2, y2, label = 'Slytherin', marker='x')
	plt.scatter(x3, y3, label = 'Gryffindor', marker='o')
	plt.scatter(x4, y4, label = 'Hufflepuff', marker='+')
	plt.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)
	#Second one
	x1 = marks_per_house_feature(data, "Astronomy", 'Ravenclaw')
	x2 = marks_per_house_feature(data, "Astronomy", 'Slytherin')
	x3 = marks_per_house_feature(data, "Astronomy", 'Gryffindor')
	x4 = marks_per_house_feature(data, "Astronomy", 'Hufflepuff')
	y1 = marks_per_house_feature(data, "Defense Against the Dark Arts", 'Ravenclaw')
	y2 = marks_per_house_feature(data, "Defense Against the Dark Arts", 'Slytherin')
	y3 = marks_per_house_feature(data, "Defense Against the Dark Arts", 'Gryffindor')
	y4 = marks_per_house_feature(data, "Defense Against the Dark Arts", 'Hufflepuff')
	fig = plt.figure()
	plt.xlabel("Astronomy")
	plt.ylabel("Defense Against the Dark Arts")
	plt.scatter(x1, y1, label = 'Ravenclaw', marker='*')
	plt.scatter(x2, y2, label = 'Slytherin', marker='x')
	plt.scatter(x3, y3, label = 'Gryffindor', marker='o')
	plt.scatter(x4, y4, label = 'Hufflepuff', marker='+')
	plt.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)
	plt.show()