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
        rating = tr.find('td', {'class': 'ratingColumn'})
        # print(rating.strong.string)
        # f.write(f"{title.a.string},{title.span.string},{rating.strong.string}")
        # f.write('\n')
        movie_id = title.a['href']
        movie_url = f'https://www.imdb.com/{movie_id}'
        res2 = requests.get(movie_url)
        html = res2.text
        soup2 = BeautifulSoup(html, 'html.parser')

        info = soup2.find('ul', {'role': 'presentation'})
        lis = info.findAll('li', {'role': 'presentation'})
        duration = lis[len(lis) -1].string.strip()
        div = soup2.find('div', {'class': 'ipc-chip-list'})
        genre = div.a.string.strip()
        release_date = soup2.find('li', {'data-testid': "title-details-releasedate"})
        release_date = release_date.find('a', {'class': 'ipc-metadata-list-item__list-content-item--link'}).string.strip()
        f.write(title.a.string.replace(',', '|') + ',' + title.span.string + ',' +
        rating.strong.string + ',' + duration + ',' + genre + ',' + release_date.replace(',', '|'))
        f.write('\n')
        print(title.span.string)
        print(rating.strong.string)
        print(duration)
        print(genre)
        print(release_date.replace(',','|'))



