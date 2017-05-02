from numpy import genfromtxt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
ds= genfromtxt("../data/testing_data_regresscsv.csv", delimiter=";")
'''
print(y)
model = LinearRegression()
model.fit(x,y)
hx=model.predict(x)

mse=mean_squared_error(hx,y)
print(mse)
'''
vse_ocene=0
vse_abs=0
print("Rezultati za linearno regresijo: ")
for i in range(0,100):
    x = ds[:, [i]]
    X_train, X_test, y_train, y_test = train_test_split(x, ds, test_size=0.25, random_state=42)
    regr = LinearRegression()
    regr.fit(X_train,y_train)
    print("User %d: " % i)
    print("Mean squared error: %.2f"
          % np.mean((regr.predict(X_test) - y_test) ** 2))
    vse_ocene+=np.mean((regr.predict(X_test) - y_test) ** 2)
    print('Mean absolute error : %.2f' % np.mean(abs((regr.predict(X_test) - y_test))))
    vse_abs+=np.mean(abs((regr.predict(X_test) - y_test)))


print(vse_ocene/100)
print(vse_abs/100)