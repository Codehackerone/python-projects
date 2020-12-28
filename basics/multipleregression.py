# pandas to read csv files
# cars.csv file contains list of cars with weight, volume and CO2 emission data
import pandas
from sklearn import linear_model

df = pandas.read_csv("cars.csv")
x = df[['Weight', 'Volume']]
y = df['CO2']
regr = linear_model.LinearRegression()
regr.fit(x, y)
# predict the CO2 emission of car which is 3000 kg heavy and vol is 1500 cc
predictedCO2 = regr.predict([[3000, 1500]])
print(predictedCO2)
# coefficient values
print(regr.coef_)
