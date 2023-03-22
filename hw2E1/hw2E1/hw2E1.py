import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model as lm


names = ['date','temperature','anomoly']

df = pd.read_csv("avgHigh_jan_1895-2018.csv",skiprows=[0], names = names)
print(df)

x = np.array(df["date"]).reshape(-1,1)
y = np.array(df["temperature"]).reshape(-1,1)
x_test = np.array([201901, 202301, 202401]).reshape(-1,1)

regr = lm.LinearRegression()
regr.fit(x, y)

y_mod = regr.predict(x)
y_pred = regr.predict(x_test)

plt.scatter(x,y, color='blue', label='Data Points')
plt.scatter(x_test, y_pred, color='green', label='Predicted')
plt.plot(x, y_mod, color='red', label='Model')
plt.legend()

plt.show()