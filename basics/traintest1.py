# Train test Model: 100 customers in a shop and shopping habits
# X axis represents no of minutes before making a purchase
# Y axis represents no of money spent in the purchase
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

numpy.random.seed(2)
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x
##
# plt.scatter(x, y)
# plt.show()
##
# train and test models
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]
###
# Fitting the dataset (Training model)
mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
myline = numpy.linspace(0, 6, 100)
plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()
# r2_score for train model
r2train = r2_score(train_y, mymodel(train_x))
print(r2train)
###
###
# Test Model
# r2_score for test model
r2test = r2_score(test_y, mymodel(test_x))
print(r2test)
###
# Predict Values Now: How much will a customer spend if he/she stays for 5 minutes
print(mymodel(5))
