import requests
from bs4 import BeautifulSoup

page_url = "https://search.yahoo.co.jp/image/search?p=%E9%BD%8B%E8%97%A4%E9%A3%9B%E9%B3%A5&ei=UTF-8&mfb=P059&ts=7832&aq=-1&fr=top_ga1_sa"

r = requests.get(page_url)

soup = BeautifulSoup(r.text,features="html.parser")

soup.find_all("img", attrs={"alt":"「齋藤飛鳥」の画像検索結果"})