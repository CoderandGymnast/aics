# Assignment solution:

from ..data import data
from ..apis import calculate_information_gain, calculate_gain_ratio
from sklearn import tree
import numpy as np
import graphviz 

outlooks = [[], []]
humidities = [[], []]
for i in range(len(data[0])):
    if data[1][i] <= 75:
        humidities[0].append(data[2][i])
        outlooks[0].append(data[0][i])
    else:
        humidities[1].append(data[2][i])
        outlooks[1].append(data[0][i])

def a():
    outlook_information_gain = calculate_information_gain(data[0], outlooks)
    humidity_information_gain = calculate_information_gain(data[2], humidities)

    print(f"Outlook information gain: {outlook_information_gain}")
    print(f"Humidty information gain: {humidity_information_gain}")