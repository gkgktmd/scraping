from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import requests
context = ssl._create_unverified_context()


d_w_car = 'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%9E%90%EB%8F%99%EC%B0%A8%EB%B3%B4%ED%97%98'
        # 다음 웹 자동차보험 키워드
d_w_dir='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%8B%A4%EC%9D%B4%EB%A0%89%ED%8A%B8%EC%9E%90%EB%8F%99%EC%B0%A8%EB%B3%B4%ED%97%98'

#res_d_w_car = urlopen(d_w_car, context=context)
res_d_w_dir = urlopen(d_w_dir, context=context)
res_d_w_car = requests.get(d_w_car, verify=False)
res_d_w_car_a=res_d_w_car.text

soup_d_w_car = BeautifulSoup(res_d_w_car_a, 'lxml')
rank_d_w_car = soup_d_w_car.findAll('div', attrs={'class': 'wrap_tit'})

soup_d_w_dir = BeautifulSoup(res_d_w_dir.read(), 'lxml')
rank_d_w_dir = soup_d_w_dir.findAll('div', attrs={'class': 'lnk_tit'})

print(rank_d_w_car.get)