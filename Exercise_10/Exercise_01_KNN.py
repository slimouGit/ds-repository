# - funct: You normalize your data in another table
# - funct: You code a simple euclid distance function
# - funct: You take a point and calculate the distance to all points
# - funct: You take the list from above and sort it
# - funct: You aggregate by target variable
# - funct: you take the max to determine the targe class

import numpy as np
np.random.seed(42)
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris = load_iris()
data = iris.data
labels = iris.target
features = iris.values()
from scipy.spatial import distance

exerciseData = [5.2,2.7,3.9,1.4]
# exerciseData = [4.8, 2.5, 5.3, 2.4]
# exerciseData = [5.2,4.1,1.5,0.1]

x, y = data, labels
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)

#plot sepal features
plt.scatter(x[:, 0], x[:, 1])
plt.show()

#function to plot data
def plot_dataset(data_x, data_y, exercise_data_x, exercise_data_y):
    colors = ["yellow", "blue", "green"]
    for index, point in enumerate(data_x):
        plt.scatter(point[0], point[1], color=colors[data_y[index]])
    plt.scatter(exercise_data_x,exercise_data_y, color="red")
    plt.show()

plot_dataset(iris["data"][:, (0, 1)], iris["target"], exerciseData[0], exerciseData[1])

class KNeighborsClassifier:
    def __init__(self, k: int = 5):
        self.k = k

    def normalizer(X: np.ndarray):
        data_min = np.min(X, axis=0)
        data_max = np.max(X, axis=0)
        x_transformed = (x - data_min) / (data_max - data_min)
        return x_transformed

    def distance(x:np.ndarray, y):
        distances = list()
        for i in x:
            distances.append(distance.euclidean(i, y))
        return distances

    def sortDistances(x:list):
        return np.argsort(x)

    def predictTargetClass(x: list, y: np.ndarray):
        targetList = list()
        neighbors = x[0:3]
        for i in neighbors:
            targetList.append(y[i])
        return targetList

    def predictTargetClass2(x:list, y: np.ndarray):
        targetList= list()
        neighbors = x[0:3]
        for i in neighbors:
            targetList.append(y[i])
        return targetList


clf = KNeighborsClassifier

x_transformed = clf.normalizer(x)
# print(x_transformed)

distances = clf.distance(x,exerciseData)
# print(distances)

sortedDistances = clf.sortDistances(distances)
# print(sortedDistances)

targetClasses = clf.predictTargetClass(sortedDistances, x)
# print(targetClasses)

targetClasses2 = clf.predictTargetClass2(sortedDistances, labels)
print("Classes: ", targetClasses2)

for i in targetClasses:
    print(model.predict([i]))

for j in targetClasses:
    print(j)






x_train_transformed = clf.normalizer(X_train)
x_test_transformed = clf.normalizer(X_test)

plot_dataset(x_test_transformed[:, (0, 1)], iris["target"], y[0], y[1])

plt.scatter(x_test_transformed[:, 0], x_test_transformed[:, 1])
plt.show()




