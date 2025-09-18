# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.preprocessing import LabelEncoder,StandardScaler
# from sklearn.metrics import accuracy_score,classification_report

# df=pd.read_excel('/content/petadoption.xlsx')
# print("the first 5 rows",df.head())
# print(df.isnull().sum())

# le_breed=LabelEncoder()
# df['Breed']=le_breed.fit_transform(df['Breed'])

# X=df[['PetID','Type','Age','Breed','Gender','Vaccinated','Sterilized','Fee','PhotoAmt']]
# y=df['AdoptionSpeed']

# scaler=StandardScaler()
# X=scaler.fit_transform(X)

# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

# model=LogisticRegression(max_iter=1000)
# model.fit(X_train,y_train)

# y_pred=model.predict(X_test)

# print("accuracy score",accuracy_score(y_test,y_pred))
# print("classification report",classification_report(y_test,y_pred))
# print("model coefficients",model.coef_) 



import tensorflow as tf
from tensorflow.keras  import layers,models
import matplotlib.pyplot as plt
(X_train,y_train),(x_test,y_test)=tf.keras.datasets.mnist.load_data()
X_train=X_train.astype('float32')/255.0
x_test=x_test.astype('float32')/255.0

_X_train=X_train.reshape(-1,28,28,1)#1 is the number opf channels
_x_test=x_test.reshape(-1,28,28,1)#-1 means "figure this dimension out automatically"
