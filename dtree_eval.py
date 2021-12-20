'''
    TEMPLATE FOR MACHINE LEARNING HOMEWORK
    AUTHOR Eric Eaton, Chris Clingerman
'''

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Arial"

from sklearn import tree
from sklearn.metrics import accuracy_score

numOfFoldsPerTrial = 10

def evaluatePerformance(numTrials=100):
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
    filename = 'data/SPECTF.dat'
    data = np.loadtxt(filename, delimiter=',')
    X = data[:, 1:]
    y = np.array([data[:, 0]]).T
    n,d = X.shape
    
    # # create list to hold data
    # treeAccuracies = []
    # stumpAccuracies = []
    # dt3Accuracies = []
    
    '''Hold accuracies for all training set sizes: 10%, 20%,...100%.'''
    numPercents=10
    dudtAccs=np.zeros([numPercents,numOfFoldsPerTrial*numTrials])
    stumpAccs=np.zeros([numPercents,numOfFoldsPerTrial*numTrials])
    dt2Accs=np.zeros([numPercents,numOfFoldsPerTrial*numTrials])
    dt3Accs=np.zeros([numPercents,numOfFoldsPerTrial*numTrials])

    # perform 100 trials
    for x in range(0, numTrials):
        # shuffle the data
        idx = np.arange(n)
        np.random.seed(13)
        np.random.shuffle(idx)
        X = X[idx]
        y = y[idx]

        # split the data randomly into 10 folds
        folds = []    
        intervalDivider = len(X)/numOfFoldsPerTrial
        for fold in range(0, numOfFoldsPerTrial):
            # designate a new testing range
            Xtest = X[fold * intervalDivider:(fold + 1) * intervalDivider,:]
            ytest = y[fold * intervalDivider:(fold + 1) * intervalDivider,:]
            Xtrain = X[:(fold * intervalDivider),:]
            ytrain = y[:(fold * intervalDivider),:]
            Xtrain = Xtrain.tolist()
            ytrain = ytrain.tolist()

            # complete the training data set so that it contains all
            # data except for the current test fold
            for dataRow in range((fold + 1) * intervalDivider, len(X)):
                Xtrain.append(X[dataRow])
                ytrain.append(y[dataRow])
               
            Xtrain=np.array(Xtrain)    
            ytrain=np.array(ytrain)
            
            count=x*numOfFoldsPerTrial+fold
            
            r=len(Xtrain)/numPercents
            for P in range(1,numPercents+1):
                
                '''1. Split P % of training set.'''
                if P == numPercents:
                    x_train=Xtrain[:]
                    y_train=ytrain[:]
                else:
                    x_train=Xtrain[:r*P,:]
                    y_train=ytrain[:r*P,:]
                    
                
                '''2. Build models.'''
                dudt = tree.DecisionTreeClassifier()
                dudt.fit(x_train,y_train)
                stump= tree.DecisionTreeClassifier(max_depth=1)
                stump.fit(x_train,y_train)
                dt2= tree.DecisionTreeClassifier(max_depth=2)
                dt2.fit(x_train,y_train)
                dt3= tree.DecisionTreeClassifier(max_depth=3)
                dt3.fit(x_train,y_train)
                
                '''3. Evaluate on testing set.'''
                dudtAccs[P-1][count]=accuracy_score(ytest,dudt.predict(Xtest))
                stumpAccs[P-1][count]=accuracy_score(ytest,stump.predict(Xtest))
                dt2Accs[P-1][count]=accuracy_score(ytest,dt2.predict(Xtest))
                dt3Accs[P-1][count]=accuracy_score(ytest,dt3.predict(Xtest))
                
            # # train the decision tree
            # clf = tree.DecisionTreeClassifier()
            # clf = clf.fit(Xtrain,ytrain)

            # # train the 1-level decision tree
            # oneLevel = tree.DecisionTreeClassifier(max_depth=1)
            # oneLevel = oneLevel.fit(Xtrain,ytrain)

            # # train the 3-level decision tree
            # threeLevel = tree.DecisionTreeClassifier(max_depth=3)
            # threeLevel = threeLevel.fit(Xtrain,ytrain)

            # # output predictions on the remaining data
            # y_pred_tree = clf.predict(Xtest)
            # y_pred_stump = oneLevel.predict(Xtest)
            # y_pred_dt3 = threeLevel.predict(Xtest)

            # # compute the training accuracy of the model and save to the 
            # # list of all accuracies
            # treeAccuracies.append(accuracy_score(ytest, y_pred_tree))
            # stumpAccuracies.append(accuracy_score(ytest, y_pred_stump))
            # dt3Accuracies.append(accuracy_score(ytest, y_pred_dt3)) 
    
    # # Update these statistics based on the results of your experiment
    # meanDecisionTreeAccuracy = np.mean(treeAccuracies)
    # stddevDecisionTreeAccuracy = np.std(treeAccuracies)
    # meanDecisionStumpAccuracy = np.mean(stumpAccuracies)
    # stddevDecisionStumpAccuracy = np.std(stumpAccuracies)
    # meanDT3Accuracy = np.mean(dt3Accuracies)
    # stddevDT3Accuracy = np.std(dt3Accuracies)

    # make certain that the return value matches the API specification
    # stats = np.zeros((3,2))
    # stats[0,0] = meanDecisionTreeAccuracy
    # stats[0,1] = stddevDecisionTreeAccuracy
    # stats[1,0] = meanDecisionStumpAccuracy
    # stats[1,1] = stddevDecisionStumpAccuracy
    # stats[2,0] = meanDT3Accuracy
    # stats[2,1] = stddevDT3Accuracy
    # return stats
    dudtMeans=np.mean(dudtAccs,axis=1)
    dudtStds=np.std(dudtAccs,axis=1)
    stumpMeans=np.mean(stumpAccs,axis=1)
    stumpStds=np.std(stumpAccs,axis=1)
    dt2Means=np.mean(dt2Accs,axis=1)
    dt2Stds=np.mean(dt2Accs,axis=1)
    dt3Means=np.mean(dt3Accs,axis=1)
    dt3Stds=np.mean(dt3Accs,axis=1)
    
    x=range(10,110,10)
    
    '''https://matplotlib.org/1.2.1/examples/pylab_examples/errorbar_demo.html'''
    
    fig, axs = plt.subplots(nrows=2, ncols=2, sharex=True)
    ax = axs[0,0]
    ax.errorbar(x, dudtMeans, yerr=dudtStds)
    ax.set_title("Depth-unlimited decision tree")
    
    ax = axs[0,1]
    ax.errorbar(x, stumpMeans, yerr=stumpStds)
    ax.set_title("Decision stump")
   
    ax = axs[1,0]
    ax.errorbar(x, dt2Means, yerr=dt2Stds)
    ax.set_title("2-leval decision tree")
    
    ax = axs[1,1]
    ax.errorbar(x, dt3Means, yerr=dt3Stds)
    ax.set_title("3-leval decision tree")
    
    fig.suptitle('Learning Curve')
    plt.show()


# Do not modify from HERE...
if __name__ == "__main__":
    
    evaluatePerformance()
    # stats = evaluatePerformance()
    # print "Decision Tree Accuracy = ", stats[0,0], " (", stats[0,1], ")"
    # print "Decision Stump Accuracy = ", stats[1,0], " (", stats[1,1], ")"
    # print "3-level Decision Tree = ", stats[2,0], " (", stats[2,1], ")"
# ...to HERE.
