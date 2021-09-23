'''
[NOTE]: 
- This file only contains solution for exercise "1.4" of "PART II: PROGRAMMING EXERCISES". 
"1.1 - 1.3" is implemented in "hw1_skeleton/dtree_eval".

- Overall ideal of this solution: 
 + 1 Trial. 
 + 10-fold Cross Validation. 
 + Added data increases from 10% to 100% of the original dataset. 
'''

'''
[REFERENCE]: 
- https://scikit-learn.org/stable/auto_examples/model_selection/plot_learning_curve.html
- https://github.com/scikit-learn/scikit-learn/blob/main/examples/model_selection/plot_learning_curve.py
- https://scikit-learn.org/stable/modules/learning_curve.html
'''

"""
========================
Plotting Learning Curves
========================
In the first column, first row the learning curve of a naive Bayes classifier
is shown for the digits dataset. Note that the training score and the
cross-validation score are both not very good at the end. However, the shape
of the curve can be found in more complex datasets very often: the training
score is very high at the beginning and decreases and the cross-validation
score is very low at the beginning and increases. In the second column, first
row we see the learning curve of an SVM with RBF kernel. We can see clearly
that the training score is still around the maximum and the validation score
could be increased with more training samples. The plots in the second row
show the times required by the models to train with various sizes of training
dataset. The plots in the third row show how much time was required to train
the models for each training sizes.
"""
print(__doc__)

from sys import getsizeof
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"]="arial"
#plt.rcParams["font.weight"]=""
#plt.rcParams["font.style"]=""
plt.rcParams["font.size"]="9"
from sklearn import tree
from sklearn.model_selection import learning_curve
from sklearn.model_selection import KFold


def plot_learning_curve(estimator, title, X, y, axes=None, ylim=None, cv=None,
                        n_jobs=None, train_sizes=np.linspace(.1, 1.0, 5)):
    """
    Generate 3 plots: the test and training learning curve, the training
    samples vs fit times curve, the fit times vs score curve.
    Parameters
    ----------
    estimator : estimator instance
        An estimator instance implementing `fit` and `predict` methods which
        will be cloned for each validation.
    title : str
        Title for the chart.
    X : array-like of shape (n_samples, n_features)
        Training vector, where ``n_samples`` is the number of samples and
        ``n_features`` is the number of features.
    y : array-like of shape (n_samples) or (n_samples, n_features)
        Target relative to ``X`` for classification or regression;
        None for unsupervised learning.
    axes : array-like of shape (3,), default=None
        Axes to use for plotting the curves.
    ylim : tuple of shape (2,), default=None
        Defines minimum and maximum y-values plotted, e.g. (ymin, ymax).
    cv : int, cross-validation generator or an iterable, default=None
        Determines the cross-validation splitting strategy.
        Possible inputs for cv are:
          - None, to use the default 5-fold cross-validation,
          - integer, to specify the number of folds.
          - :term:`CV splitter`,
          - An iterable yielding (train, test) splits as arrays of indices.
        For integer/None inputs, if ``y`` is binary or multiclass,
        :class:`StratifiedKFold` used. If the estimator is not a classifier
        or if ``y`` is neither binary nor multiclass, :class:`KFold` is used.
        Refer :ref:`User Guide <cross_validation>` for the various
        cross-validators that can be used here.
    n_jobs : int or None, default=None
        Number of jobs to run in parallel.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.
    train_sizes : array-like of shape (n_ticks,)
        Relative or absolute numbers of training examples that will be used to
        generate the learning curve. If the ``dtype`` is float, it is regarded
        as a fraction of the maximum size of the training set (that is
        determined by the selected validation method), i.e. it has to be within
        (0, 1]. Otherwise it is interpreted as absolute sizes of the training
        sets. Note that for classification the number of samples usually have
        to be big enough to contain at least one sample from each class.
        (default: np.linspace(0.1, 1.0, 5))
    """


    axes.set_title(title)
    if ylim is not None:
        axes.set_ylim(*ylim)
    axes.set_xlabel("Training examples")
    axes.set_ylabel("Score")

    train_sizes, train_scores, test_scores, fit_times, _ = \
        learning_curve(estimator, X, y, cv=cv, n_jobs=n_jobs,
                       train_sizes=train_sizes,
                       return_times=True)
    
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    
    # Plot learning curve
    axes.grid()
    axes.fill_between(train_sizes, train_scores_mean - train_scores_std,
                         train_scores_mean + train_scores_std, alpha=0.1,
                         color="r")
    axes.fill_between(train_sizes, test_scores_mean - test_scores_std,
                         test_scores_mean + test_scores_std, alpha=0.1,
                         color="g")
    axes.plot(train_sizes, train_scores_mean, 'o-', color="r",
                 label="Training score")
    axes.plot(train_sizes, test_scores_mean, 'o-', color="g",
                 label="Cross-validation score")
    axes.legend(loc="best")
    return [test_scores_mean,test_scores_std]

def main():
    filename="II/hw1_skeleton/data/SPECTF.dat" # [NOTE]: Must use relative path from "main.bat" file to be able to execute.  
    data = np.loadtxt(filename, delimiter=',')
    X = data[:, 1:]
    n,d = X.shape
    y = np.array([data[:, 0]]).reshape(n,)

    numFolds=10
    numSegments=10
    
    cv=KFold(n_splits=numFolds) # [NOTE]: By default, shuffle is "False". 
    
    _, axes = plt.subplots(2, 3, figsize=(20, 5))
    
   
    for i in range(2):
        for j in range(3):
            level= 3*i+j+1
            if level==6:
                break
            title = f"Level-{level} Decision Tree"
            estimator = tree.DecisionTreeClassifier(max_depth=level)
            [testScoreMean, testScoreStd]=plot_learning_curve(estimator, title, X, y, axes[i,j],cv=cv,train_sizes=np.linspace(.1,1.0,numSegments))
    
    
    title = "Learning Curves (Basic Decision Tree)"
    estimator = tree.DecisionTreeClassifier()
    [testScoreMean, testScoreStd]=plot_learning_curve(estimator, title, X, y, axes[1,2],cv=cv,train_sizes=np.linspace(.1,1.0,10))
    plt.show()

