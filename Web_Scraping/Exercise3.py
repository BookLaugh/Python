'''
TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right from the home page 
(e.g Love,Inspirational,Life, etc...). HINT: Keep in mind there are also tags underneath each quote, try to find a class only present in the top right tags, 
perhaps check the span.
'''

import requests
import bs4

result = requests.get('https://quotes.toscrape.com/page/1/')
soup = bs4.BeautifulSoup(result.text,'lxml')

lst = soup.select('.tag-item')
print("This is top 10 tags:")
for index,tag in enumerate(lst):
    print(f'{index}.{tag.text}')
