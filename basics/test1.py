import numpy
import cv2
from numpy import random

arr = numpy.arange(27)
arr2 = arr.reshape(3, 9)
arr3 = arr.reshape(3, 3, 3)

arrnew = random.randint(266, size=(1500, 1000))
print(arrnew)
# cv2.imwrite("newpic2.png", arrnew)
#  arrnew1=cv2.imread("newpic1.png",0)
# print(arrnew1)
