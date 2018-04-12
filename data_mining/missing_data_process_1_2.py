import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


input_path = "data/clean_Building_Permits.csv"
sf_permits = pd.DataFrame(pd.read_csv(input_path))
part_column = ['Number of Existing Stories', 'Number of Proposed Stories', 'Estimated Cost', 'Revised Cost']

# 用最高频率值来填补缺失值-2
def highest_freq_fill(part_column):
    top_data = {}
    for i in part_column:
        top_data[i] = sf_permits[[i]].apply(pd.value_counts).index[0] # class df
    print(top_data)
    sf_permits.fillna(top_data).drop(["Unnamed: 0"],axis=1).to_csv("data/Part_Building_Permits_2.csv")

#通过属性相关性填充缺失值-3
def property_relation_fill(data):
    x_1 = 'Number of Existing Stories'
    y_1 = 'Number of Proposed Stories'
    x_2 = 'Estimated Cost'
    y_2 = 'Revised Cost'

    for j in range(len(data)):
        if (data[y_1].isnull())[j] and (data[x_1].notnull())[j] :  # 如果为空即插值。
            data[y_1][j] = data[x_1][j]
    for j in range(len(data)):
        if (data[x_1].isnull())[j] and (data[y_1].notnull())[j] :  # 如果为空即插值。
            data[x_1][j] = data[y_1][j]

    for j in range(len(data)):
        if (data[y_2].isnull())[j] and (data[x_2].notnull())[j] :  # 如果为空即插值。
            data[y_2][j] = data[x_2][j]
    for j in range(len(data)):
        if (data[x_2].isnull())[j] and (data[y_2].notnull())[j] :  # 如果为空即插值。
            data[x_2][j] = data[y_2][j]
    print(data)
    data.drop(["Unnamed: 0"],axis=1).to_csv("data/Part_Building_Permits_3.csv")


if __name__ == '__main__':
    highest_freq_fill(part_column)
    # property_relation_fill(sf_permits)