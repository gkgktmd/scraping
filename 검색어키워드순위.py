#import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import ssl

context = ssl._create_unverified_context()


url='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%9E%90%EB%8F%99%EC%B0%A8%EB%B3%B4%ED%97%98'
# 자동차보험 카워드 파워링크
#url='https://comic.naver.com/webtoon/weekday.nhn'
res=urlopen(url,context=context)

#res.raise_for_status()

soup=BeautifulSoup(res.read(),'lxml')
#res.text를 lxml(파서)를 통해서 Beautifulsoup객체로 만들어줌

rank=soup.findAll('div',attrs={'class':'lnk_tit'})
#rank1=soup.find('li',attrs={'class':'rank01'})
# li태그에서 속성이 class=rank01인것

#rank2=rank1.next_sibling.next_sibling
# next_sibling은 다음 형제관계로 넘어가는 것
print('기준시간:',datetime.datetime.now())
print('키워드: 자동차보험')
print('-'*50)
for i,x in enumerate(rank):
    print(f'{i+1}등: {x.get_text()}')
