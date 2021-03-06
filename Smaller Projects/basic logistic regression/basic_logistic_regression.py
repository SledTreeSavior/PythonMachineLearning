# -*- coding: utf-8 -*-
"""MLMT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VlghGdnHVm2dtbSfOnaorwbCBLalGeie
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from scipy.special import expit

#generate a toy dataset
n_samples = 100
np.random.seed(0)
X = np.random.normal(size=n_samples)
y = (X > 0).astype(float)
X += .2 * np.random.normal(size=n_samples)

print(X.shape)
print(y.shape)
X = X.reshape(-1, 1)
print(X.shape)

plt.scatter(X, y)
plt.title('Dataset Before Logistic Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.xlim(-4,4)
plt.show()

from sklearn.linear_model import LogisticRegression

log_reg_smallC = LogisticRegression(C=0.1)
log_reg_smallC.fit(X, y)
log_reg_largeC = LogisticRegression(C=(10**5))
log_reg_largeC.fit(X, y)

from sklearn.model_selection import cross_val_predict
y_train_pred_smallC = cross_val_predict(log_reg_smallC, X, y)
y_train_pred_largeC = cross_val_predict(log_reg_largeC, X, y)
smallC_expit = expit(y_train_pred_smallC)
largeC_expit = expit(y_train_pred_largeC)

xExpit = np.linspace(-4, 4)
yExpit = expit(xExpit)

plt.subplot(1, 2, 1)
plt.plot(X, y, "g.", label="Raw Data")
plt.plot(X, y_train_pred_smallC, "r.", label="Trained Data")
plt.plot(xExpit, yExpit, "b-", label="Expit Line")
plt.title('Logistic Regression: C=0.1 v.s. Raw Data')
plt.xlabel('X')
plt.ylabel('y')
plt.legend(loc='upper left')

plt.subplot(1, 2, 2)
plt.plot(X, y, "g.", label="Raw Data")
plt.plot(X, y_train_pred_largeC, "r.", label="Trained Data")
plt.plot(xExpit, yExpit, "b-", label="Expit Line")
plt.title('Logistic Regression: C=10**5 v.s. Raw Data')
plt.xlabel('X')
plt.ylabel('y')
plt.legend(loc='upper left')

plt.subplots_adjust(left=-1.5,
                    bottom=0.1, 
                    right=1, 
                    top=0.9, 
                    wspace=0.1, 
                    hspace=0.4)

#in the left graph, you can see that the trained data differs from the raw data,
#especially on the bottom of the graph before 0
#the expit line shows the desired transition from 0 --> 1 as reflected by the data

#in the right graph, you can see that the trained data differs from the raw data,
#this graph's data differs on the bottom to a lesser degress than the left graph.
#unlike the left graph, this graph also differs from the raw data
  #on the top of the graph, with positive X values
#the expit line once again shows the desired transition from 0 --> againt the 
    #trained and raw data

#Documentation Definition for C in Logistic Regression:
#Cfloat, default=1.0
#Inverse of regularization strength; must be a positive float. Like in support vector machines, smaller values specify stronger regularization.
#
#The documentation's description of the C value in logistic regression is reflected by the 
#graphs above. This is because the graph with the lower C value seems to implement
#stronger regularization. This is shown in the greater distance between the raw data points 
#and the trained data points as compared to the graph with a greater C value.