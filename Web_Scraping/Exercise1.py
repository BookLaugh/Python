# TASK: Get the names of all the authors on the first page.
# NOTE: Make sure pip install those libraries

import requests
import bs4

result = requests.get('https://quotes.toscrape.com/page/1/')
soup = bs4.BeautifulSoup(result.text,'lxml')

authors = set()
lst = soup.select('.author')

for name in lst:
    authors.add(name.text)

for index,name in enumerate(authors,1):
    print(index,name)
