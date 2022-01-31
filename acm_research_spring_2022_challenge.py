# -*- coding: utf-8 -*-
"""ACM Research Spring 2022 Challenge.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_1ErrHwZJfJ73UswIT7RgDV2RbtKsOpf
"""

import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression


#read in the csv
url = 'https://raw.githubusercontent.com/umalik1910/ACM-Research-Coding-Challenge-S22/main/mushrooms.csv'
df = pd.read_csv(url)

#plot to see data is balanced
sns.countplot(x = 'class', data =df).set_title("Number of Poisonous and Edible Mushrooms")

#convert the data type of data frame, which is originally object type
df = df.astype('category')
for col in df.columns:
  df[col] = LabelEncoder().fit_transform(df[col])

#assign X
X = df.drop(['class'], axis = 1)
#assign Y
Y = df['class'].values

#do the split for test and training
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.20, train_size = 0.8, random_state = 0)

#run the model
model = LogisticRegression(solver='liblinear').fit(X_train, y_train)
print(model.score(X_test, y_test) * 100)