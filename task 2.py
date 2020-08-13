# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:22:20 2020

@author: princess
"""

#for training data &same code for test data
import pandas as pd
df =  pd.read_csv('C:/Users/princess/Desktop/task2/training.csv',  sep=';',skiprows=1, header=None)

#convert data frame to strings
df = df.applymap(str)
#convert data frame into list
myList=df.values.tolist()
#make a list of lists correctly separated
row=[]
data=[]
for l in myList:
    for string in l:
        row  +=string.split(',')
    data.append(row)

