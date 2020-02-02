import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190909',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

rank = 1
movies = soup.select('#old_content > table > tbody > tr')
for movie in movies:
	# print(movie)
	a_tag = movie.select_one('td.title > div > a')
	if a_tag is not None:
		title = a_tag.text
		star = movie.select_one('td.point').text
		print(rank, title, star)
		rank += 1