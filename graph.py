import pandas as pd 
import matplotlib.pyplot as plt 
import requests
from bs4 import BeautifulSoup
#Find website to provide data for graph 
session = requests.Session()
response = session.get('https://www.thehivelaw.com/blog/how-often-do-planes-crash-statistics-how-many-planes-crash-a-year', headers={'User-Agent': 'Mozilla/5.0'})

print(response.status_code)


soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')
df = pd.read_html(str(table))[0][['Year', 'Total Accidents']]
print(df.info())

plt.plot(df['Total Accidents'], df['Year'], marker ='.', color='b')

plt.show()
# import website and if website blocked use requests function

