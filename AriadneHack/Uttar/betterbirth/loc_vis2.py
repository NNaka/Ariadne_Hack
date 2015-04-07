# ID Hackathon 2015 - February 13, 2015
# Norihito Naka kevin john

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
un='hcohen21'
k='op8hs13cd4'
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in(un, k)

# Opening and reading int the CSV file
MY_FILE = open('location.csv')
reader = csv.reader(MY_FILE)

name = [];
births = [];
pop = [];
mortality = [];

for line in reader:
	name.append(line[0])
	births.append(line[1])
	pop.append(line[2])	
	mortality.append(line[3])

# Casting string list to double list
births = map(float, births)
pop = map(float, pop)
mortality = map(float, mortality)

total = sum(births)
print name



pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 400)
pd.set_option('display.mpl_style', 'default')

data = []
for i in range(len(name)):
    # Create 1 data object per point, so every point is a different color
    mx = float(max(births))
    s = [ math.sqrt(float(births[i])/mx)*60.0 ]
    t = [ 'City: %s<br>Births: %s' % (name[i], births[i]) ]
    d = {'x':[pop[i]],\
         'y':[mortality[i]],\
         'marker': {'size':s, 'opacity':0.9, 'line':{'width':1}},\
         'type':'scatter','mode':'markers','text':t}
    data.append(d)

layout = {'showlegend':False,'hovermode':'closest', 'title':'',\
    'title':'India Birth Statistics by City<br>Bubble Size is Number of Births',\
    'xaxis':{ 'ticks':'','linecolor':'white','showgrid':False,'zeroline':False, 'title': 'Population', 'nticks':12 },
    'yaxis':{ 'ticks':'','linecolor':'white','showgrid':False,'zeroline':False, 'title': 'Mortality Rate (deaths per 1000 births)', 'nticks':12 }}

py.plot(data, layout=layout)
