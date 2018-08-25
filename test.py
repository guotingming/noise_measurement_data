import os
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from  read import csv_to_df
#names=os.listdir(r'measurement_data')
names=os.listdir(r'E:\nm\measurement_data')
print(names)
name=names[0]
name=name.split('.')
name=name[0]
name=name[:-1]
print(name)
filename_new=[]
for filename in names:
    name = filename
    name = name.split('.')
    name = name[0]
    name = name[:-1]
    filename_new.append(name)
t=np.array(filename_new)
t=np.unique(t)
t=t.tolist()
#print(filename_new)
#print(t[0])
#filename='measurement_data/'+t[0]+'1'+'.csv'
#print(filename)
List=['1','2','3','4']
filenames=[]
for l in List:
    filename='measurement_data/'+t[0]+l+'.csv'
    filenames.append(filename)
print(filenames)

data1=csv_to_df(filenames[0])
data2=csv_to_df(filenames[1])
data3=csv_to_df(filenames[3])
data4=csv_to_df(filenames[2])
#print(data1)
writer = pd.ExcelWriter(t[0]+'.xlsx')
data1.to_excel(writer, sheet_name='bias1')
data2.to_excel(writer, sheet_name='bias2')
data3.to_excel(writer, sheet_name='bias3')
data4.to_excel(writer, sheet_name='bias4')
writer.save()