import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,root_mean_squared_error,mean_absolute_error
from sklearn.linear_model import LinearRegression
data=pd.read_csv("house_data.csv")
#print(data)
x=data[["Area","Bedrooms","Bathrooms","Age","Distance_City"]]
y=data["Price"]
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=7)
model=LinearRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("predicted price:",y_pred)
print("actual price:",y_test.values)
score=r2_score(y_test,y_pred)
print("score is ",score)
mae=mean_absolute_error(y_test,y_pred)
print("mae is ",mae)