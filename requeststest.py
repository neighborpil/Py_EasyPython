import requests
r = requests.get('https://en.wikipedia.org/wiki/Main_Page')
html_doc = r.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc)

css_path = '#mp-otd>ul>li>a'
tags = soup.select(css_path)
for tag in tags:
    year = tag['title']
    desc = tag.parent.get_text().split('-', 1)[1]
    print('{}: {}'.format(year, desc))
    print()
