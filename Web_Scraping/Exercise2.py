# TASK: Create a list of all the quotes on the first page.

import requests
import bs4

result = requests.get('https://quotes.toscrape.com/page/1/')
soup = bs4.BeautifulSoup(result.text,'lxml')

quotes = list()

lst = soup.select('.text')
for text in lst:
    quotes.append(text.text)
print(quotes)
