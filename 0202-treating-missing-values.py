import numpy as np
import pandas as pd

from pandas import Series, DataFrame

missing = np.nan

series_obj = Series(['row1', 'row2', missing, 'row4', 'row5', 'row6', missing, 'row8'])
print(series_obj)

print()

print('isnull() method: describes a boolean that describes whether an element in a pandas object is a null value')
print(series_obj.isnull())

print()

np.random.seed(25) # so we get the same numbers as in the tut
df_obj = DataFrame(np.random.rand(36).reshape(6, 6))

print('Use .loc method to set some of the values to missing:')
df_obj.loc[3:5, 0] = missing
df_obj.loc[1:4, 5] = missing
print(df_obj)

print()

print('fillna() method: Fill missing values in a pandas object with numeric values that we can specify:')
filled_df = df_obj.fillna(0)
print(filled_df)

print()

print('We can specify columns and set different values, with a dictionary')
filled_df = df_obj.fillna({0: 0.1, 5: 1.25})
print(filled_df)

print()

print('Fill missing values with the last non-null element in the column series')
filled_df = df_obj.fillna(method='ffill')
print(filled_df)

print()

print('Count missing values, by column:')
# Remember: df_obj still has the missing values
print(df_obj.isnull().sum())

print()

print('Drop all of the rows that have any missing values:')
print(df_obj.dropna())

print()

print('Drop all of the columns that have any missing values:')
print(df_obj.dropna(axis=1))
