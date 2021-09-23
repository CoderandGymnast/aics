'''
    TEMPLATE FOR MACHINE LEARNING HOMEWORK
    AUTHOR Eric Eaton, Chris Clingerman
'''

import sys
import os

from pandas.core import api

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import numpy as np
import matplotlib.pyplot as plt

from sklearn import tree
from sklearn.metrics import accuracy_score

from apis import split

def trainAndTest(XTrain,yTrain,XTest,yTest,level):
    '''
    Train & test the specified data with Decision Tree. 
    
    Params:
      level: decision tree depth,e.g., 1 (Decision stump), 3,...
    
    Return: 
      Accuracy.
    '''
    
    clf = tree.DecisionTreeClassifier(max_depth=level)
    clf = clf.fit(XTrain,yTrain)

    yPred = clf.predict(XTest)

    return accuracy_score(yTest, yPred)

def processPair(XTrain,yTrain,XTest,yTest):
    ''''
    Process each of the 10 pairs in each trial. 
    '''
    
    accuracies=np.empty([3,])
    accuracies[0]=trainAndTest(XTrain,yTrain,XTest,yTest,None)
    accuracies[1]=trainAndTest(XTrain,yTrain,XTest,yTest,1)
    accuracies[2]=trainAndTest(XTrain,yTrain,XTest,yTest,3)
    return accuracies


def processTrial(X,y,numFolds):
    '''
    Process each trial.
    '''
    accuracies=np.array([]).reshape(0,3)
    for i in range(1,numFolds+1): # [NOTE]: Process 10 pairs. 
        [XTrain,XTest]=split(X,numFolds,i)
        [yTrain,yTest]=split(y,numFolds,i) 
        acc=processPair(XTrain,yTrain,XTest,yTest)
        accuracies=np.concatenate((accuracies,[acc]),axis=0)
    return accuracies

def evaluatePerformance():
    '''
    Evaluate the performance of decision trees,
    averaged over 1,000 trials of 10-fold cross validation
    
    Return:
      a matrix giving the performance that will contain the following entries:
      stats[0,0] = mean accuracy of decision tree
      stats[0,1] = std deviation of decision tree accuracy
      stats[1,0] = mean accuracy of decision stump
      stats[1,1] = std deviation of decision stump
      stats[2,0] = mean accuracy of 3-level decision tree
      stats[2,1] = std deviation of 3-level decision tree
      
    ** Note that your implementation must follow this API**
    '''
    
    # Load Data
    # filename = 'data/SPECTF.dat' # Relative path from this file.
    filename="II/hw1_skeleton/data/SPECTF.dat" # [NOTE]: Must use relative path from "main.bat" file to be able to execute.  
    data = np.loadtxt(filename, delimiter=',')
    X = data[:, 1:]
    y = np.array([data[:, 0]]).T
    n,d = X.shape
    
    numTrials=100
    numFolds=10

    accuracies=np.array([]).reshape(0,3)
    for c in range(numTrials):
        # shuffle the data
        idx = np.arange(n)
        np.random.seed(13)
        np.random.shuffle(idx)
        X = X[idx]
        y = y[idx]
    
        acc=processTrial(X,y,numFolds)
        accuracies=np.concatenate((accuracies,acc),axis=0)
    
    accuracies=accuracies.T
    meanAccuracies=np.sum(accuracies,axis=1)/(numTrials*numFolds)
    stdDevs=np.std(accuracies,axis=1)
    
    meanDecisionTreeAccuracy = meanAccuracies[0]
    stddevDecisionTreeAccuracy = stdDevs[0] 
    meanDecisionStumpAccuracy = meanAccuracies[1] 
    stddevDecisionStumpAccuracy = stdDevs[1] 
    meanDT3Accuracy = meanAccuracies[2] 
    stddevDT3Accuracy = stdDevs[2] 
    


    # make certain that the return value matches the API specification
    stats = np.zeros((3,2))
    stats[0,0] = meanDecisionTreeAccuracy
    stats[0,1] = stddevDecisionTreeAccuracy
    stats[1,0] = meanDecisionStumpAccuracy
    stats[1,1] = stddevDecisionStumpAccuracy
    stats[2,0] = meanDT3Accuracy
    stats[2,1] = stddevDT3Accuracy
    return stats

def main():
    stats = evaluatePerformance()
    print(f"Decision Tree Accuracy = {stats[0,0]} ({stats[0,1]})")
    print(f"Decision Stump Accuracy = {stats[1,0]} ({stats[1,1]})")
    print(f"3-level Decision Tree = {stats[2,0]} ({stats[2,1]})")

# Do not modify from HERE...
if __name__ == "__main__":
    main() 
# ...to HERE.
