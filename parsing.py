import requests 
import bs4
from fake_headers import Headers

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'Java', 'ИТ']
url = 'https://habr.com'
HEADERS = Headers(browser='chrome', os="win", headers=True).generate()

response = requests.get(url + '/ru/all', headers=HEADERS)
soup = bs4.BeautifulSoup(response.text, features='html.parser')
         
    
article = soup.find_all(class_='tm-articles-list__item')
for art in article:
    for key in KEYWORDS:
        if key in art.text:
            data = art.find(class_='tm-article-snippet__datetime-published').find('time').attrs['title']
            href = art.find(class_='tm-article-snippet__title-link').attrs['href']
            title = art.find(class_='tm-article-snippet__title').find('span').text
            print(f'Дата: {data}')
            print(f'Заголовок: {title}')
            print(f'Ссылка: {url + href}')
            print()