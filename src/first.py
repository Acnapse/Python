import json
import matplotlib as mpl
import matplotlib.pyplot as plt

data={}
with open("/Users/marinka2014/Desktop/Работа/task_1/data.json", "r") as read_file:
    records = json.load(read_file)['records']
country = ''
cases= []
for block in records:
    if country == block['countryterritoryCode']:
        cases.append(int(block['cases']))
    else:
        if country != '': data[country] = cases
        country = block['countryterritoryCode']
        cases=[]
        cases.append(int(block['cases']))
        
dpi = 80
fig = plt.figure(dpi = dpi, figsize = (1024 / dpi, 600 / dpi) )
mpl.rcParams.update({'font.size': 13})

dates=['01/04/2020', '31/03/2020','30/03/2020','29/03/2020','28/03/2020','27/03/2020','26/03/2020','25/03/2020','24/03/2020']
for reg in data:
    plt.plot(dates, data[reg], linestyle = 'solid', label=reg)

plt.xticks(rotation = 45)
plt.title('Covid-19', fontsize=19)
plt.xlabel('Day', fontsize=16, color='brown')
plt.ylabel('Cases', fontsize=16, color='brown')
plt.legend(loc='upper right')
ax = plt.axes()
ax.grid(color="grey", which="major", axis='x', linestyle='-', linewidth=0.5)
ax.grid(color="grey", which="major", axis='y', linestyle='-', linewidth=0.5)

fig.set_facecolor('floralwhite')
plt.savefig('first')
