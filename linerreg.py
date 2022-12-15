import numpy as n
import matplotlib.patches as mpplt
import pandas as pd
from sklearn.linear_model import LinearRegression
data=pd.read_csv("C:\\Users\\12014\\Desktop\\ins.csv")
x=data.iloc[:,0].values
print(x)
y=data.iloc[:,1].values
print(y)
print(type(data))
lr=LinearRegression()
lr.fit(x,y)
#y_pred=lr.predict(x)
mpplt.scatter(x,y)
#mpplt.plot(x,y_pred, color='red')
mpplt.show()

