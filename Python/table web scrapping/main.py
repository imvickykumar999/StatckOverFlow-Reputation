
import requests
from bs4 import BeautifulSoup as bs

link = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
req = requests.get(link)
soup = bs(req.content, 'html5lib')

table = soup.findAll('table', attrs = {'class':'wikitable sortable'})
print(table[0])

for i in table[0]:
    print(i.findAll('tr'))
