from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
context = ssl._create_unverified_context()


d_w_car = 'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%9E%90%EB%8F%99%EC%B0%A8%EB%B3%B4%ED%97%98'
        # 다음 웹 자동차보험 키워드
d_w_dir='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%8B%A4%EC%9D%B4%EB%A0%89%ED%8A%B8%EC%9E%90%EB%8F%99%EC%B0%A8%EB%B3%B4%ED%97%98'

res_d_w_car = urlopen(d_w_car, context=context)
res_d_w_dir = urlopen(d_w_dir, context=context)

soup_d_w_car = BeautifulSoup(res_d_w_car.read(), 'lxml')
rank_d_w_car = soup_d_w_car.findAll('a', attrs={'class': 'f_link_bu'})

soup_d_w_dir = BeautifulSoup(res_d_w_dir.read(), 'lxml')
rank_d_w_dir = soup_d_w_dir.findAll('div', attrs={'class': 'lnk_tit'})

for i, x in enumerate(rank_d_w_car):
    if 'DB' in x.get_text():
        print(f'★{i + 1}순위: {x.get_text()}★')
    else:
        print(f'{i + 1}순위: {x.get_text()}')

for i, x in enumerate(rank_d_w_dir):
    if 'DB' in x.get_text():
        print(f'★{i + 1}순위: {x.get_text()}★')
    else:
        print(f'{i + 1}순위: {x.get_text()}')
