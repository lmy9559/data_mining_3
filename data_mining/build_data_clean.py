import pandas as pd
import numpy as np

input_path = "data/Building_Permits.csv"
data = pd.DataFrame(pd.read_csv(input_path))
clean_data = data.dropna(axis = 1,how = "all")
drop_index = []
for i in range(len(clean_data)):
    if str(clean_data['Permit Number'][i]).startswith('M'):
        drop_index.append(i)
clean_data = clean_data.drop(drop_index,axis =0)
clean_data.to_csv("data/clean_Building_Permits.csv")
print(len(clean_data))