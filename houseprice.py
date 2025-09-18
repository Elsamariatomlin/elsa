import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



x=np.array(["200","1000","1500","2000","2500"]).reshape(-1,1)
y=np.array(["300000","500000","600000","700000","800000"])
model=LinearRegression()
model.fit(x,y)


#MODEL PARAMETERS
print("intercept(base price):",model.intercept_)
print("slope(price per square foot):",model.coef_[0])

size=1100
predicted_price=model.predict([[size]])
print(f"predicted price for a {size} sqft={predicted_price[0]:.2f}")
