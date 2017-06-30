import sys
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

data = open('trainingdata.txt')
X = []
Y = []

for line in data:
    input_data = line.strip().split(',')
    if float(input_data[0]) < 4.11:
        X.append(float(input_data[0]))
        Y.append(float(input_data[1]))
    
df_x = np.array(X)
df_x_ = df_x.reshape(len(X),1)

regressor = LinearRegression() 
regressor.fit(df_x_, Y)

timeCharged = float(raw_input().strip())
if timeCharged < 4.11:
    y_pred = regressor.predict(timeCharged)
    print y_pred[0]
else:
    y_pred = 8
    print y_pred
