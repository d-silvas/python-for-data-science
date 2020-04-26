import numpy as np
import pandas as pd

from pandas import Series, DataFrame

df_obj = DataFrame({
    'col1': [1, 1, 2, 2, 3, 3, 3],
    'col2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
    'col3': ['A', 'A', 'B', 'B', 'C', 'C', 'C']
})
print(df_obj)

print()

print('Check for duplicated rows')
print(df_obj.duplicated())

print()

print('Drop duplicate rows')
print(df_obj.drop_duplicates())

print()

df_obj = DataFrame({
    'col1': [1, 1, 2, 2, 3, 3, 3],
    'col2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
    'col3': ['A', 'A', 'B', 'B', 'C', 'D', 'C']
})
print('Drop the duplicates from column 3 (rows which have duplicated values in col 3)')
print(df_obj.drop_duplicates(['col3']))
