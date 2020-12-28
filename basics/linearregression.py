# linear regression and prediction of speed of car at age 20
# a list consists of car age
# b list consists of car speed
# r is for relationship
from scipy import stats
import matplotlib.pyplot as plt

x = [5, 6, 7, 8, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
slope, intercept, r, p, std_err = stats.linregress(x, y)


def myfunc(x):
    return slope * x + intercept


mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
speed = myfunc(20)
print(speed)
print(r)
