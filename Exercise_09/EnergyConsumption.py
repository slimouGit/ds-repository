import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("CrossTraining.csv")
print(df)

X = df[["dist", "time"]]
Y = df[["cal"]]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,Y, random_state=0, test_size=0.25)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print("Intercept ", model.intercept_)
print("Cofficient ", model.coef_)

print(model.predict([[13.5,40.08]]))


