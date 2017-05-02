from numpy import genfromtxt
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
ds= genfromtxt("../data/testing_data_nb.csv", delimiter=";")
y=ds[:,1]
scores=0.0
for i in range(0,100):
    y = ds[:, i]
    X=ds

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)
    clf1 = MultinomialNB()
    clf1.fit(X_train, y_train)
    print("User"+str(i))
    print("SCORE")
    print(clf1.score(X_test, y_test))
    scores+=float(clf1.score(X_test, y_test))

print("Avg scores: ")
print(scores/100)

