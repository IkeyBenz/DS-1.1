import pandas as pd
import numpy as np

f = open('../Datasets/titanic.csv', 'r')

data = pd.read_csv(f)

dataframe = pd.DataFrame(data)

print(dataframe)