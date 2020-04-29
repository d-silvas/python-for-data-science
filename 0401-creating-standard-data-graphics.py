import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams

from pandas import Series, DataFrame

# To see plots:
# https://stackoverflow.com/questions/8575062/how-to-show-matplotlib-plots-in-python
# https://stackoverflow.com/questions/34347145/pandas-plot-doesnt-show

print('-- CREATING A LINE CHART FROM A LIST OBJECT ---')
print()

print('> Plotting a line chart in matplotlib')
x = range(1, 10)
y = [1, 2, 3, 4, 0, 4, 3, 2, 1]
# plt.plot(x, y)
# plt.show()

print()

print('> Plotting a line chart from a pandas object')

print()

address = '.\\data\\mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

mpg = cars['mpg']
# mpg.plot()
# plt.show()

print()

# Line chart to plot 3 variables:
df = cars[['cyl', 'wt', 'mpg']]
# df.plot()
# plt.show()

##### BAR CHARTS #####

# From data:

# plt.bar(x, y)
# plt.show()

# From a dataframe:

# mpg.plot(kind='bar') # kind='barh' for horizontal bars
# plt.show()


##### PIE CHARTS #####

x = [1, 2, 3, 4, 0.5]
# plt.pie(x)
# plt.show()

# Save a plot
plt.pie(x)
plt.savefig('pie_chart.png')
plt.show()
