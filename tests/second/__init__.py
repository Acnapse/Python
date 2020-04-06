# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import json

data={};dpi = 80
countryArray = ['ESP', 'ITA', 'USA', 'DEU']
width = 0.2
country = ''

file = "/Users/marinka2014/Desktop/Работа/task/data.json"
with open(file, "r") as read_file:
	records = json.load(read_file)['records']

for block in records:
	if country == block['countryterritoryCode']:
		cases.append(int(block['cases']))
	else:
		if country != '': 
			data[country] = cases
		country = block['countryterritoryCode']
		cases=[]
		cases.append(int(block['cases']))

dates=['01/04/2020', '31/03/2020','30/03/2020','29/03/2020','28/03/2020','27/03/2020','26/03/2020','25/03/2020','24/03/2020']

fig = plt.figure(dpi = dpi, figsize = (1200 / dpi, 560 / dpi) )
mpl.rcParams.update({'font.size': 13})


locs = np.arange(1, len(dates)+1)

ax = plt.axes()
ax.yaxis.grid(True, zorder = 1)

mas=[] 
for i in range(len(countryArray)):
	color_rectangle = np.random.rand(1, 3)
	mas.append(ax.bar(locs + i * width, data[countryArray[i]], width=width, label=countryArray[i], color=color_rectangle))

plt.xticks(locs + width*1.5, dates, rotation = 45)
plt.legend(loc='upper right')

for rects in mas:
	for rect in rects:
		height = rect.get_height()
		ax.annotate('{}'.format(height),
					xy=(rect.get_x() + rect.get_width() / 2, height),
					xytext=(0, 3), 
					textcoords="offset points",
					ha='center', va='bottom', size='8')

plt.savefig('second')
