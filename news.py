import requests
from bs4 import BeautifulSoup as bs

headers_gadgets, links_gadgets, descs_gadgets, originals_gadgets = [], [], [], []
headers_internet, links_internet, descs_internet, originals_internet = [], [], [], []
headers_games, links_games, descs_games, originals_games = [], [], [], []


def refresh_gadgets():
	global headers_gadgets, links_gadgets, descs_gadgets, originals_gadgets
	headers_gadgets, links_gadgets, descs_gadgets, originals_gadgets = [], [], [], []
	site = requests.get('https://news.yandex.ru/gadgets.html')
	soup = bs(site.text, 'html.parser')
	code_headers = soup.find(class_='page-content').find_all(class_='link link_theme_black i-bem')

	for i in range(0, 8):
		links_gadgets.append('https://yandex.ru' + code_headers[i].get('href'))
		headers_gadgets.append(code_headers[i].contents[0])

	for i in range(0, 8):
		article_site = requests.get(links_gadgets[i])
		article_soup = bs(article_site.text, 'html.parser')
		descs_gadgets.append(article_soup.find(class_='doc__text').contents[0])
		originals_gadgets.append(article_soup.find(class_='doc__content').find('a').get('href'))


def refresh_internet():
	global headers_internet, links_internet, descs_internet, originals_internet
	headers_internet, links_internet, descs_internet, originals_internet = [], [], [], []
	site = requests.get('https://news.yandex.ru/internet.html')
	soup = bs(site.text, 'html.parser')
	code_headers = soup.find(class_='page-content').find_all(class_='link link_theme_black i-bem')

	for i in range(0, 8):
		links_internet.append('https://yandex.ru' + code_headers[i].get('href'))
		headers_internet.append(code_headers[i].contents[0])

	for i in range(0, 8):
		article_site = requests.get(links_internet[i])
		article_soup = bs(article_site.text, 'html.parser')
		descs_internet.append(article_soup.find(class_='doc__text').contents[0])
		originals_internet.append(article_soup.find(class_='doc__content').find('a').get('href'))


def refresh_games():
	global headers_games, links_games, descs_games, originals_games
	headers_games, links_games, descs_games, originals_games = [], [], [], []
	site = requests.get('https://yandex.ru/news/rubric/games')
	soup = bs(site.text, 'html.parser')
	code_headers = soup.find_all(class_='link link_theme_black i-bem')

	for i in range(0, 8):
		links_games.append('https://yandex.ru' + code_headers[i].get('href'))
		headers_games.append(code_headers[i].contents[0])

	for i in range(0, 8):
		article_site = requests.get(links_games[i])
		article_soup = bs(article_site.text, 'html.parser')
		try:
			descs_games.append(article_soup.find(class_='doc__content').find('div').contents[0])
		except:
			descs_games.append(article_soup.find(class_='news-story__content').find('span').contents[0])
		try:
			originals_games.append(article_soup.find(class_='doc__content').find('a').get('href'))
		except:
			originals_games.append(article_soup.find(class_='news-story__content').find('a').get('href'))


refresh_games()
refresh_gadgets()
refresh_internet()
print('news.py started!')
