from numpy import genfromtxt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

ds= genfromtxt("../data/primozcsvfive.csv", delimiter=";")

print("Rezultati za linearno regresijo: ")
myarr=np.array([])
x = ds[:, [0]]
X_train, X_test, y_train, y_test = train_test_split(x, ds[:,2], test_size=0.25, random_state=42)
regr = LinearRegression()
regr.fit(X_train,y_train)

myarr=abs(regr.predict(X_test))
#print(myarr)


myabs=0
for i in range(1,100):
    X_train, X_test, y_train, y_test = train_test_split(x, ds[:, i], test_size=0.25, random_state=3)
    regr = LinearRegression()
    regr.fit(X_train, y_train)
    #print(regr.predict(X_test))
    myarr += abs(regr.predict(X_test))
    print('Mean absolute error : %.2f' % np.mean(abs((regr.predict(X_test) - y_test))))
    myabs+=np.mean(abs((regr.predict(X_test) - y_test)))

print("Koncne vrednosti, napoved na 25 filmih")
print(myarr/100)
print("Avg abs")
print(myabs/100)