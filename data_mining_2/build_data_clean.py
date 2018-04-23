#!/usr/bin/env Python
# coding=utf-8
import pandas as pd
import numpy as np
import sys

input_path = "Building_Permits.csv"
data = pd.DataFrame(pd.read_csv(input_path,encoding="utf-8"))
clean_data = data.dropna(axis = 1,how = "all") # remove null column
drop_index = []
for i in range(len(clean_data)):
    if str(clean_data['Permit Number'][i]).startswith('M'):
        drop_index.append(i)
clean_data = clean_data.drop(drop_index,axis =0)
clean_data.to_csv("clean_Building_Permits.csv",encoding = 'utf-8')
print(len(clean_data))
