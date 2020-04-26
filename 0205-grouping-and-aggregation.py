import numpy as np
import pandas as pd

from pandas import Series, DataFrame

print('Read data from csv and print first 5 records')
address = '.\\data\\mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
print(cars.head())

print()

print('Group by the cylinder column')
cars_groups = cars.groupby(cars['cyl'])
print('Generate and print the means for each value of the groups that have previously been generated')
print(cars_groups.mean())