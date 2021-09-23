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

def b():
    outlook_gain_ratio = calculate_gain_ratio(data[0], outlooks)
    humidity_gain_ratio = calculate_gain_ratio(data[2], humidities)

    print(f"Outlook gain ratio: {outlook_gain_ratio}")
    print(f"Humidity gain ratio: {humidity_gain_ratio}")
    
def c():
    X=np.array(data[0:4]).T
    y=data[4] 
    clf=tree.DecisionTreeClassifier()
    clf=clf.fit(X,y)
    
    # [NOTE]: Only execute the below snippet once to plot.
    # dot_data = tree.export_graphviz(clf, out_file=None) 
    # graph = graphviz.Source(dot_data) 
    # dot_data = tree.export_graphviz(clf, out_file=None, 
    #     feature_names=['Outlook','Temp','Humidity','Windy'],
    #     class_names=["Don't Play","Play"],  
    #     filled=True, rounded=True,  
    #     special_characters=True)   
    # graph = graphviz.Source(dot_data)
    # graph.render("output","decision-tree")
    
    # [NOTE]: Predict on training set. 
    # for i in X:
    #     print(clf.predict([i]))
