import numpy as np
import pandas as pd
from matplotlib import pyplot as py
index = int(input("How many numbers are in your data? "))
a = []
while index > 0:
    answer = float(input("What is a number in your data? "))
    a.append(answer)
    index -= 1
mean  = np.mean(a)
median = np.median(a)
print(a)
print("The mean of your data set is", mean)
print("The median of your data set is", median)
