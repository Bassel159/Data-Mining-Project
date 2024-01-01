# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gmFDiBewhk63ED_wkn167FPalJdMuHn2
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

train=pd.read_csv('train.csv')

x_train = train.drop('smoking',axis=1)
y_train = train['smoking']

test=pd.read_csv('test.csv')

clf = RandomForestRegressor(3000,criterion="poisson",max_features="log2")

clf.fit(x_train , y_train)

y_predict = clf.predict(test)

id = test['id']

df = pd.DataFrame({'id':id,'smoking':y_predict})

df.to_csv('poisson35.csv',index = False)