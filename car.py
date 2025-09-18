
#car evaluation
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LogisticRegression


columns=['buying','maint','doors','persons','lug_boot','safety','class']  #load dataset
df=pd.read_csv ("C:\\Users\\pc26\\Desktop\\elsamca\\car.data",names=columns)
print("null value under each column")
print(df.isnull().sum())
label_encoder={}
for column in df.columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoder[column] = le

x=df.drop(columns=["class"])
y=df["class"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LogisticRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("accuracy:",r2_score(y_test,y_pred))
print("mean squared error:",mean_squared_error(y_test,y_pred))
new_car=np.array([[2018,3000,1,0]])
price_pred=model.predict(new_car)
print("predicted price:",price_pred[0])
# label_encoder={}
# for column in df.columns:
#     le ={}
    
#     label_encoder[column] = le
