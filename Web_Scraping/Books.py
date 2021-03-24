# Goal: Find all books with 5 star and title
import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

five_star_titles = []
for page in range(1,51):
    scrape_url = base_url.format(1)
    result = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(result.text,'lxml')
    books = soup.select('.product_pod')

    for index,book in enumerate(books,1):
        if len(book.select('.star-rating.Five')) != 0: # length should be 2 cause there is a image and title
            print(index,book.select('a')[1]['title'])

# It will print all five stars titled books with it's index in that page
