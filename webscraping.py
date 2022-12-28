import requests
result= requests.get("http://example.com/")
print(type(result))
print(result.text)

import bs4
soup=bs4.BeautifulSoup(result.text,'lxml')
print(soup)
print('\n')
print(soup.select('title'))
print('\n')
print(soup.select('title')[0].getText())
print('\n')
print(soup.select('p'))
print('\n')
print(type(soup.select('p')))
print('\n')
print(soup.select('p'))
print('\n')
print(soup.select('meta'))
print('\n')
print(soup.select('div'))



print('\nWeb Scraping:\n')

soup=bs4.BeautifulSoup(requests.get('https://books.toscrape.com/catalogue/category/books/travel_2/index.html').text,'lxml')
product=soup.select(".product_pod")
example=product[0]
print(example.select(".star-rating.Two"))

print(example.select("a"))
print(example.select("a")[1]['title'])



from PIL import Image
mac=Image.open('375px-Aerial_view_of_Apple_Park_dllu.jpg')
print(mac.show())
print(mac.format_description)