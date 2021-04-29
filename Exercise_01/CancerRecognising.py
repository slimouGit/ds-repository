import pandas as pd

df = pd.read_csv("data/openml_phpJNxH0q.csv")
# df = pd.read_csv("data/data.csv")
print(df.head(10))

from sklearn.model_selection import train_test_split

#DEFINE VARIABLES
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

print("Score:", model.score(X_test,y_test))

#-------------------------------------------------------
print("-------------------------------------------------------------")
print("Classification report")
y_pred = model.predict(X_test)
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

#-------------------------------------------------------

from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Make predictions
y_pred = model.predict(X_test)

print("-------------------------------------------------------------")
print(y_test)
print("amount: 699")
print("amount testdata (25%): 175")
print("malignant: 63")
print("bening: 112")
print("-------------------------------------------------------------")
#print training/test results
print("----------------------------------------------")
#prepare training/test print
y_test_pred = model.predict(X_test)
#print("Testdaten")
#for i in range(0, len(y_test_pred)):
#    print(str(y_test_pred[i]) + " - " + str(y_test[i]))
#print("----------------------------------------------")
#-----------------------------------------------------------------

# Matrix plott
cm = confusion_matrix(y_true=y_test, y_pred=y_pred)
ax= plt.subplot()
sns.heatmap(cm, annot=True, ax = ax, fmt = 'g'); #annot=True to annotate cells
# labels, title and ticks
ax.set_xlabel('Predicted', fontsize=20)
ax.xaxis.set_label_position('top')
ax.xaxis.set_ticklabels(['healthy', 'ill'], fontsize = 15)
ax.xaxis.tick_top()

ax.set_ylabel('Reality', fontsize=20)
ax.yaxis.set_ticklabels(['ill', 'healthy'], fontsize = 15)
plt.show()

#-----------------------------------------------------------------
print("Confusion Matrix")
print("\t\t\t\t\t\tModell: nicht wahr\t\tModell: wahr")
print("Realität: nicht wahr\tRichtig negativ\t\t\tFalsch positiv")
print("Realität: wahr\t\t\tFalsch negativ\t\t\tRichtig positiv")
print("-------------------------------------------------------------")

# Build confusion metrics

from sklearn.metrics import confusion_matrix
y_test_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_test_pred)
print(cm)

print(model.predict([[5.0,1.0,1.0,1.0,2.0,1.0,3.0,1.0,1.0]]))
print(model.predict([[1.0,1.0,1.0,1.0,2.0,1.0,3.0,1.0,1.0]]))