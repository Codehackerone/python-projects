import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()
df = pandas.read_csv("cars2.csv")
x = df[['Weight', 'Volume']]
y = df['CO2']
# scaledX is the array containing scaled and standardized values of 'Weight' and 'Volume'
scaledX = scale.fit_transform(x)
# print(scaledX)
regr = linear_model.LinearRegression()
regr.fit(scaledX, y)
scaled = scale.transform([[2300, 1.3]])
predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)
