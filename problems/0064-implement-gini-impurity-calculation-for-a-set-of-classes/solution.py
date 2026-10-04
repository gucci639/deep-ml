
import numpy as np

def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
	_, counts = np.unique(y, return_counts=True)
	probs = counts / len(y)
	return round(1 - np.sum(probs**2),3)	