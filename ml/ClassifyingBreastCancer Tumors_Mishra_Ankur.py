from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

#############################################################
# cancer.py
# in theory, detects if patient has a cancerous tumor
#
# Ankur Mishra: January 2017
############################################################

def getData():
	x = []
	y = []
	input = open("BreastCancerData.txt").read().split("\n")
	for i in input:
		inputArray = i.split(",")
		outputArray = [inputArray[3], inputArray[4], inputArray[10]]
		#according to science malignant tumors aren't uniform in shape or size and grow rapidly
		exp = inputArray.pop(1)
		x.append(outputArray)
		y.append(exp)
	return x,y


x = []
y = []
x, y = getData()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state=45)

clf = svm.SVC(kernel='rbf')

clf.fit(x_train, y_train)

y_predict = clf.predict(x_test)

print(accuracy_score(y_test, y_predict))
