import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.imdb.com/chart/top/')
html = res.text
soup = BeautifulSoup(html, 'html.parser')
tbody = soup.find('tbody', {'class': 'lister-list'})
trs = tbody.findAll('tr')
with open("movies.csv", 'w') as f:
    for tr in trs:
        title = tr.find('td', {'class': 'titleColumn'})
        # print(title.a.string, title.span.string)
        year = title.span.string
        year = year.replace('-', '')
        rating = tr.find('td', {'class': 'ratingColumn'})
        # print(rating.strong.string)
        f.write(f"{title.a.string},{year},{rating.strong.string}")
        f.write('\n')
