from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import random
import numpy as np

#############################################################
# cancer.py
# in theory, detects if patient has a cancerous tumor
#
# Ankur Mishra: Sept 2017
############################################################

def getData():
	x = []
	y = []
	input_array = np.genfromtxt('training.csv',delimiter=',')
	for i in input_array:
		exp = i[9]
		outputArray = [i[0], i[6], i[1], i[2], i[7], i[8]]
		x.append(outputArray)
		y.append(exp)
	return x,y

x, y = getData()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state=45)

clf = svm.SVC(kernel='rbf')

clf.fit(x_train, y_train)

test_array = np.genfromtxt('testing.csv',delimiter=',')

y_predict = clf.predict(x_test)
print(x_test)
print(accuracy_score(y_test, y_predict))
