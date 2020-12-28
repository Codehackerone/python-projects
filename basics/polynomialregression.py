# polynomial regression and prediction of speed of car at time 20:00
# a list consists of time of day
# b list consists of car speed
# r2_score is for relationship(r squared value)
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import numpy as np

x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]
mymodel = np.poly1d(np.polyfit(x, y, 3))
myline = np.linspace(1, 22, 100)
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
speed = mymodel()
print(speed)
print(r2_score(y, mymodel(x)))
