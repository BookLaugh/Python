import requests
import bs4

result = requests.get("https://en.wikipedia.org/wiki/Bill_Gates")

soup = bs4.BeautifulSoup(result.text,"lxml")
txt = soup.select('.thumbimage')[0]
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Paul_Allen_and_Bill_Gates_at_Lakeside_School_in_1970.jpg/220px-Paul_Allen_and_Bill_Gates_at_Lakeside_School_in_1970.jpg')
f = open('C:\\Users\\ULAN\\Desktop\\Python\\Bill_gates_image.jpg','wb')
f.write(image_link.content)
f.close()

txt2 = soup.select('img')[2]
image_link2 = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Bill_Gates_2018.jpg/220px-Bill_Gates_2018.jpg')
f = open('C:\\Users\\ULAN\\Desktop\\Python\\Bill_Gates.jpg','wb')
f.write(image_link2.content)
f.close()
