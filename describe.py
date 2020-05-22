import pandas as pd
import numpy as np
import math
import sys

def information(data):
	max_val, min_val, count, somme, result = data[0], data[0], 0, 0, []
	for x in data:
		if not np.isnan(x):
			if max_val < x:
				max_val = x
			if min_val > x:
				min_val = x
			count += 1
			somme += x
			result.append(x)
	return max_val, min_val, count, somme, result

def std(data, count, mean):
	s = 0
	for x in data:
		if not np.isnan(x):
			s += (x - mean) **2
	s /= (count - 1)
	return (math.sqrt(s))

def percent(sorted_tab, count):
	length = count - 1
	if (count % 2 == 1):
		q1 = sorted_tab[int(length * 0.25)]
		q2 = sorted_tab[int(length * 0.5)]
		q3 = sorted_tab[int(length * 0.75)]
	else:
		q1 = (sorted_tab[int(length * 0.25)] + sorted_tab[int(length * 0.25) + 1]) / 2
		q2 = sorted_tab[int(length * 0.5)] + sorted_tab[int((length * 0.5) + 1)] / 2
		q3 = (sorted_tab[int(length * 0.75)] + sorted_tab[int(length * 0.75) + 1]) / 2
	return q1, q2, q3

if __name__ == '__main__':
    try:
        data = pd.read_csv(sys.argv[1])
    except:
        print("Usage: python3 describe resources/dataset_train.csv")
        exit (-1)
    features = {}
    features_name = ["Arithmancy","Astronomy","Herbology","Defense Against the Dark Arts","Divination","Muggle Studies","Ancient Runes","History of Magic","Transfiguration","Potions","Care of Magical Creatures","Charms","Flying"]
    for i in range(13):
        feature = {}
        max_val, min_val, count, somme, tab = information(data[features_name[i]])
        feature["Count"] = count
        feature["Mean"] = somme / count
        feature["Std"] = std(data[features_name[i]], count, feature["Mean"])
        feature["Min"] = min_val
        sorted_tab = sorted(tab)
        q1, q2, q3 = percent(sorted_tab, count)
        feature["25%"] = q1
        feature["50%"] = q2
        feature["75%"] = q3
        feature["Max"] = max_val
        features[features_name[i]] = feature
    print(pd.DataFrame.from_dict(features))
        