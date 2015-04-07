# ID Hackathon 2015 - February 13, 2015
# Norihito Naka kevin john

import csv, time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Opening and reading int the CSV file
MY_FILE = open('data.csv')
reader = csv.reader(MY_FILE)


rows = [];
for line in reader:
	rows.append(line[1])

# Casting string list to double list
rows = map(float, rows)

total = sum(rows)
		
labels = 'Third Trimester', 'Second Trimester', 'First Trimester'
sizes = [rows[2]/total*100, rows[1]/total*100, rows[0]/total*100]
colors = ['yellowgreen', 'lightskyblue', 'lightcoral']
	#explode = (0, 0.1, 0) # only "explode" the 2nd slice (i.e. 'Hogs')

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')

plt.show()
