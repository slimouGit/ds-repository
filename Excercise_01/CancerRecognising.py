import pandas as pd

df = pd.read_csv("data/openml_phpJNxH0q.csv")
df.head()

from sklearn.model_selection import train_test_split

#X = df[["Clump_Thickness","Cell_Size_Uniformity","Cell_Shape_Uniformity","Marginal_Adhesion","Single_Epi_Cell_Size","Bare_Nuclei","Bland_Chromatin","Normal_Nucleoli","Mitoses"]].values
X = df.drop("Class", axis=1).values
y = df["Class"].values

X_train, X_test, y_train, y_test = train_test_split(X,y, random_state = 0, test_size=0.25)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)

print(model.score(X_test,y_test))

predict = model.predict([[8.0,10.0,10.0,8.0,7.0,10.0,9.0,7.0,1.0]])
print("Predict ", predict)

predict = model.predict([[0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,1.0]])
print("Predict ", predict)


