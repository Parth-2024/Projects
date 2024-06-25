import pandas as pd
from sklearn.linear_model import LinearRegression
#Machine Learning Model
def machine_learning(query):
			'''This function creates a prediction model based on the fat percentage of a person and risk for that person getting a heart attack'''
			data=pd.read_csv("Heart Attack Reponses - Form Responses 1.csv")
			print(type(data))
			mind=LinearRegression()
			y=data["Heart Attack Risk"]
			x=data["Body Fat Percentage"]
			x=x.values
			x=x.reshape(5,1)
			mind.fit(x,y)
			print(mind.predict([[query]]))