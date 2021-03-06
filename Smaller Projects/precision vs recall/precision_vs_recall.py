# -*- coding: utf-8 -*-
"""HW3_posted.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R4LpOb6UB_x5ZSZRv9mcfTHMNC8OHCfR

# COMP4220: Machine Learning, Fall 2021, Assignment 3

# **Due: October 22, 2021 - 11:59pm** 

> ## **Please submit one pdf file for all questions.**
"""

#importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')
wine = pd.read_csv("drive/My Drive/School/Machine Learning/Homework/HW3/wine.csv")
wine

"""## variables (based on physicochemical tests):
<ol>
 <li>fixed acidity</li>
 <li>volatile acidity</li>
 <li>citric acid</li>
 <li>residual sugar</li>
 <li>chlorides</li>
 <li>free sulfur dioxide</li>
 <li>total sulfur dioxide</li>
 <li>density</li>
 <li>pH</li>
 <li>sulphates</li>
 <li>alcohol</li>
 <li>quality (score between 0 and 10)</li>
</ol>

## Tips
> ### What might be an interesting thing to do is to set an arbitrary cutoff for your dependent variable (wine quality): 7 or higher getting classified as '1' and the remainder as '0'.
>### This allows you to practice working the ROC curve and the AUC value.
>### Without doing any kind of feature engineering or overfitting you should be able to get an AUC of .88

## 1. Since we want to classify the wine base on the quality so we want to look at the distribution of the wine quality
## Make a histogram plot for the quality column to see the distribution of the wine quality
"""

wine_quality = wine['quality']
plt.hist(wine_quality)

"""## 2. Show the number of null values using sum() method. If there are null values then remove them from the dataset"""

wine.isnull().sum()

wine.dropna()

"""## 3. Since we want to cutoff the dependent variable (wine quality)
## Change the quality column to 1 if the quality >= 7, and 0 if the quality is < 7
## Show the dataset after make the change
## Hint: the quality column should only have 0s and 1s after the change
"""

wine.loc[wine['quality'].astype(np.int) < 7, 'quality'] = 0

wine.loc[wine['quality'].astype(np.int) >= 7, 'quality'] = 1

"""## 4. Create y as the quality column and X as everything but the quality column"""

X = wine[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']]
y = wine['quality']

"""## 5. Split the dataset into the training and test set using "train_test_split".
## Split the training and test set into 70-30 ratio
"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
y_train_1 = (y_train == 1)
y_test_1 = (y_test == 1)

"""## 6. Apply Feature Scaling method for X_train and X_test with "StandardScaler" from "sklearn.preprocessing"
## Hint: use StandardScaler.fit_transform for "X_train" and use StandardScaler.transform for "X_test"
"""

from sklearn.preprocessing import StandardScaler

x = StandardScaler()
x.fit_transform(X_train)
x.transform(X_test)

"""## 7. Train the logistic regression model on the training set using (solver='lbfgs', random_state = 42, max_iter = 1000)"""

from sklearn.linear_model import LogisticRegression

log_reg = LogisticRegression(solver='lbfgs', random_state = 42, max_iter = 100)
log_reg.fit(X_train, y_train_1)

from sklearn.model_selection import cross_val_score
cross_val_score(log_reg, X_train, y_train_1, cv=3, scoring="accuracy")

"""## 8.Predict the results of x_test"""

from sklearn.model_selection import cross_val_predict
y_train_pred = cross_val_predict(log_reg, X_train, y_train_1, cv=3)
y_train_pred

"""## 9.Make the confusion matrix and show the result

"""

from sklearn.metrics import confusion_matrix
cnf_matrix = confusion_matrix(y_train_1, y_train_pred)
cnf_matrix

"""## 10. find the precision_score, recall_score, and f1_score and print them"""

from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import f1_score
print(precision_score(y_train_1, y_train_pred))
print(recall_score(y_train_1, y_train_pred))
print(f1_score(y_train_1, y_train_pred))

"""## 11. Use the precision_recall_curve() function to compute precision and recall for all possible thresholds
 
"""

from sklearn.metrics import precision_recall_curve
y_scores = cross_val_predict(log_reg, X_train, y_train_1, cv=7, method="decision_function")

precisions, recalls, thresholds = precision_recall_curve(y_train_1, y_scores)

"""## 12. Use Matplotlib to plot precision and recall as functions of the threshold value
### Remember to use legend method

"""

plt.plot(thresholds, precisions[:-1], "b", label="precisions")
plt.plot(thresholds, recalls[:-1], "g", label="recalls")
plt.xlabel("thresholds")
plt.legend(loc='upper right')
plt.grid()

"""## 13. Plot the precision vs recall plot

"""

plt.plot(recalls, precisions, "b")
plt.ylabel("precisions")
plt.xlabel("recalls")
plt.grid()

"""## 14. Plot the ROC Curve"""

from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(y_train_1, y_scores)
plt.plot(fpr, tpr, linewidth=2)
plt.plot([0,1], [0,1], 'k--')

from sklearn.metrics import roc_auc_score
roc_auc_score(y_train_1, y_scores)