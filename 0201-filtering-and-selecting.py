import numpy as np
import pandas as pd

from pandas import Series, DataFrame

series_obj = Series(np.arange(8), index=[
    'row1',
    'row2',
    'row3',
    'row4',
    'row5',
    'row6',
    'row7',
    'row8',
])
print('Series object:')
print(series_obj)

print()

print(f'Select element by label index: {series_obj["row7"]}')
print(f'Select element by integer index:')
print(series_obj[[1, 7]])

print()

# Create DataFrame object of 36 random numbers
np.random.seed(25)
df_obj = DataFrame(
    np.random.rand(36).reshape((6, 6)),
    index=['row1', 'row2', 'row3', 'row4', 'row5', 'row6'],
    columns=['col1', 'col2', 'col3', 'col4', 'col5', 'col6']
)
print('DataFrame object:')
print(df_obj)

print()

print('Select specific rows and columns')
print(df_obj.loc[['row2', 'row5'], ['col5', 'col2']])

print()

print('Data slicing: selecting every row from 3 to 7')
print(series_obj['row3': 'row7'])

print()

print('Comparing with scalars:')
print('Runs a comparison element by element')
print(df_obj < 0.2)

print()

print('Filtering with scalars:')
print(series_obj[series_obj > 6])

print()

print('Setting values with scalars:')
series_obj['row1', 'row5', 'row8'] = 8
print(series_obj)
