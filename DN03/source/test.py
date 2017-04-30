from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_iris
from copy import copy
# prepare dataset
iris = load_iris()
X = iris.data[:, :2]

y = iris.target
print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# model
clf1 = MultinomialNB()
clf2 = MultinomialNB()
print(id(clf1), id(clf2)) # two different instances

clf1.fit(X_train, y_train)
print(clf1.score(X_test, y_test))

print(clf2.fit(X_train, y_train).score(X_test, y_test))
