import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

def marks_per_house_feature(data, feature, house):
	tab = data[data['Hogwarts House'] == house]
	return tab[feature]

if __name__ == "__main__":
	np.warnings.filterwarnings('ignore')
	try:
		data = pd.read_csv(sys.argv[1])
	except:
		print("Usage: python3 histogram.py datasets/dataset_train.csv")
		exit (-1)
	features_name = ["Arithmancy","Astronomy","Herbology","Defense Against the Dark Arts","Divination","Muggle Studies","Ancient Runes","History of Magic","Transfiguration","Potions","Care of Magical Creatures","Charms","Flying"]
	fig = plt.figure(figsize=(20,12))
	plt.style.use('fivethirtyeight')
	for i in range(13):
		plt.subplot(4, 4, i+2)
		plt.hist(marks_per_house_feature(data, features_name[i], 'Ravenclaw'), alpha = 0.5, label = 'Ravenclaw')
		plt.hist(marks_per_house_feature(data, features_name[i], 'Slytherin'), alpha = 0.5, label = 'Slytherin')
		plt.hist(marks_per_house_feature(data, features_name[i], 'Gryffindor'), alpha = 0.5, label = 'Gryffindor')
		plt.hist(marks_per_house_feature(data, features_name[i], 'Hufflepuff'), alpha = 0.5, label = 'Hufflepuff')
		plt.title(features_name[i], fontsize=12)
		plt.xlabel('Grades', fontsize=8)
		plt.ylabel('students', fontsize=8)
	fig.tight_layout(rect=[0, 0, 1, 1])
	fig.legend(['Ravenclaw', 'Slytherin', 'Gryffindor', 'Hufflepuff'], loc=2, fontsize=16, shadow=True, bbox_to_anchor=(0.05, 0.95))
	plt.show()