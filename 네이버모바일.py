from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
context = ssl._create_unverified_context()

#네이버 모바일
n_m_car='https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query=%EC%9E%90%EB%8F%99%EC%B0%A8%EB%B3%B4%ED%97%98'

n_m_dir='https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query=%EB%8B%A4%EC%9D%B4%EB%A0%89%ED%8A%B8%EC%9E%90%EB%8F%99%EC%B0%A8%EB%B3%B4%ED%97%98'

res_n_m_car = urlopen(n_m_car, context=context)
res_n_m_dir = urlopen(n_m_dir, context=context)

soup_n_m_car = BeautifulSoup(res_n_m_car.read(), 'lxml')
rank_n_m_car = soup_n_m_car.findAll('span', attrs={'class': 'tit'})

soup_n_m_dir = BeautifulSoup(res_n_m_dir.read(), 'lxml')
rank_n_m_dir = soup_n_m_dir.findAll('span', attrs={'class': 'tit'})

for i, x in enumerate(rank_n_m_car):
    if 'DB' in x.get_text():
        print(f'★{i + 1}순위: {x.get_text()}★')
    else:
        print(f'{i + 1}순위: {x.get_text()}')

for i, x in enumerate(rank_n_m_dir):
    if 'DB' in x.get_text():
        print(f'★{i + 1}순위: {x.get_text()}★')
    else:
        print(f'{i + 1}순위: {x.get_text()}')