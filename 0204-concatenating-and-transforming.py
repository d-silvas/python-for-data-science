import numpy as np
import pandas as pd

from pandas import Series, DataFrame

df_obj = pd.DataFrame(np.arange(36).reshape(6, 6))
print(df_obj)

print()

df_obj_2 = pd.DataFrame(np.arange(15).reshape(5, 3))
print(df_obj_2)

print()

print('--- CONCATENATING DATA ---')

print('Concatenate by adding new columns: along the row index values')
print(pd.concat([df_obj, df_obj_2], axis=1))

print()

print('Concatenate by adding new rows: along the column index values')
print(pd.concat([df_obj, df_obj_2]))

print()

print('--- TRANSFORMING DATA ---')
print('> Dropping data')

print()

print('Drop rows from a dataframe object')
print(df_obj.drop([0, 2]))

print()

print('Drop columns from a dataframe object')
print(df_obj.drop([0, 2], axis=1))

print()

print('> Adding data')

print()

print('Create new series obj with name')
series_obj = Series(np.arange(6))
series_obj.name = 'series_obj_name'
print(series_obj)

print()

print('Add a series to a dataframe as a column with join')
variable_added = DataFrame.join(df_obj, series_obj)
print(variable_added)

print()

print('Add using the append method')
print('Way 1: retain the original index values from variable_added')
added_datatable = variable_added.append(variable_added, ignore_index=False)
print(added_datatable)

print()

print('Way 2: regenerate indexes')
print(variable_added.append(variable_added, ignore_index=True))

print()

print('> Sorting data')

print()

print('Sort the dataframe by the values in column 5')
print(df_obj.sort_values(by=(5), ascending=[False]))
