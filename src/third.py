from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt

resp = urlopen('https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases') # скачиваем файл
html = resp.read().decode('utf8') 
soup = BeautifulSoup(html, 'html.parser')
data_x = [];data_y = []

for tag in soup.find_all('p'):
     if tag.contents[0].string == 'The deaths have been reported from': break
lst = [i for i in re.split(r'\W+', tag.contents[1]) if i]

country = '';num = 0
for i in lst:
    if i.isdigit():
        if num == 0: num = int(i)
        else: num = int(str(num) + i)  
    else: 
        if num != 0: 
            data_x.append(num)
            data_y.append(country)
            num = 0;country = ''
        country += i if country == '' else ' ' + i
    if len(data_x) > 10: break
plt.figure(figsize=(8,13))

plt.figure(dpi = dpi, figsize = (800 / dpi, 500 / dpi) )

explode = [0.1] * len(data_x)
color_rectangle = np.random.rand(11, 3)
plt.pie(data_x, explode = explode, autopct = '%1.1f%%', shadow=True, colors = color_rectangle)
plt.legend(
    bbox_to_anchor = (1, 0.45, 0.25, 0.25),
    loc = 'lower left', labels = data_y)
plt.title('The deaths have been reported from')
plt.savefig('third')
