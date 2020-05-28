import pandas as pd
import seaborn as sns
import sys
import matplotlib.pyplot as plt

if	__name__ == "__main__":
	try:
		data = pd.read_csv(sys.argv[1])
	except:
		print("Usage: python3 pair_plot.py datasets/dataset_train.csv")
		exit (-1)
	marks_col = data[data.columns[6:]]
	houses_col = data[data.columns[1]]
	result = pd.concat([houses_col, marks_col], axis=1)
	sns.pairplot(result, hue="Hogwarts House", markers='.')
	plt.show()
