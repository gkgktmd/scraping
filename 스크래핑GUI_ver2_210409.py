from tkinter import *
import tkinter.ttk as ttk

root=Tk()
root.title('실시간 검색키워드 순위')
#root.geometry('400x350+100+100')

def searching():
    pass
#     if time_a.size()!=0:
#         time_a.delete(0,END)
#     else:
#         pass
#     if lst_box.size()!=0:
#         lst_box.delete(0,END)
#     else:
#         pass
#     from urllib.request import urlopen
#     from bs4 import BeautifulSoup
#     import datetime
#     import ssl
#     context = ssl._create_unverified_context()
#
#     keyword_sel=cmb1.get()
#     if keyword_sel=='자동차보험':
#         n_w_car = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%9E%90%EB%8F%99%EC%B0%A8%EB%B3%B4%ED%97%98'
#         # 네이버 웹 자동차보험 카워드
#
#         res = urlopen(n_w_car, context=context)
#         #res.raise_for_status()
#
#         soup = BeautifulSoup(res.read(), 'lxml')
#         rank = soup.findAll('div', attrs={'class': 'lnk_tit'})
#
#         time_a.insert(END,datetime.datetime.now())
#         for i, x in enumerate(rank):
#             lst_box.insert(END,f'{i + 1}순위: {x.get_text()}')
#
#     else:
#         n_w_dir = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%8B%A4%EC%9D%B4%EB%A0%89%ED%8A%B8%EC%9E%90%EB%8F%99%EC%B0%A8%EB%B3%B4%ED%97%98'
#         # 네이버 웹 자동차보험 카워드
#
#         res = urlopen(n_w_dir, context=context)
#         # res.raise_for_status()
#
#         soup = BeautifulSoup(res.read(), 'lxml')
#         rank = soup.findAll('div', attrs={'class': 'lnk_tit'})
#
#         time_a.insert(END, datetime.datetime.now())
#         for i, x in enumerate(rank):
#             lst_box.insert(END, f'{i + 1}순위: {x.get_text()}')

#인풋 프레임
basic=LabelFrame(root,text='포탈구분',padx=5,pady=5)
basic.pack(padx=5,pady=5,fill='both')

btn1=Button(basic,text='확인',width=10, command=searching)
btn1.pack(side='right',padx=5,pady=5)

keyword=['네이버','다음']
cmb1=ttk.Combobox(basic, state='readonly', values=keyword,width=50)
cmb1.current(0)
cmb1.pack(side='left',padx=5,pady=5)

#결과 출력 프레임(키워드: 자동차보험)
lst_frame_car=LabelFrame(root,text='키워드: 자동차보험',padx=7,pady=7)
lst_frame_car.pack(fill='both',padx=5,pady=5)

#------------------------------------

lst_frame_car_w=LabelFrame(lst_frame_car,text='웹',padx=5,pady=5)
lst_frame_car_w.pack(side='left',padx=5,pady=5)

scrollbar_car_w=Scrollbar(lst_frame_car_w)
scrollbar_car_w.pack(side='right',fill='y')

lst_box_car_w=Listbox(lst_frame_car_w, height=10, selectmode='extended',yscrollcommand=scrollbar_car_w.set,width=30)
lst_box_car_w.pack(side='left', fill='both',expand=True)
scrollbar_car_w.config(command=lst_box_car_w.yview)

#------------------------------------

lst_frame_car_m=LabelFrame(lst_frame_car,text='모바일',padx=5,pady=5)
lst_frame_car_m.pack(side='right',padx=5,pady=5)

scrollbar_car_m=Scrollbar(lst_frame_car_m)
scrollbar_car_m.pack(side='right',fill='y')

lst_box_car_m=Listbox(lst_frame_car_m, height=10, selectmode='extended',yscrollcommand=scrollbar_car_m.set,width=30)
lst_box_car_m.pack(side='left', fill='both',expand=True)
scrollbar_car_m.config(command=lst_box_car_m.yview)

#결과 출력 프레임(키워드: 다이렉트자동차보험)
lst_frame_dir=LabelFrame(root,text='키워드: 다이렉트자동차보험',padx=7,pady=7)
lst_frame_dir.pack(fill='both',padx=5,pady=5)

#------------------------------------

lst_frame_dir_w=LabelFrame(lst_frame_dir,text='웹',padx=5,pady=5)
lst_frame_dir_w.pack(side='left',padx=5,pady=5)

scrollbar_dir_w=Scrollbar(lst_frame_dir_w)
scrollbar_dir_w.pack(side='right',fill='y')

lst_box_dir_w=Listbox(lst_frame_dir_w, height=10, selectmode='extended',yscrollcommand=scrollbar_dir_w.set,width=30)
lst_box_dir_w.pack(side='left', fill='both',expand=True)
scrollbar_dir_w.config(command=lst_box_dir_w.yview)

#------------------------------------

lst_frame_dir_m=LabelFrame(lst_frame_dir,text='모바일',padx=5,pady=5)
lst_frame_dir_m.pack(side='right',padx=5,pady=5)

scrollbar_dir_m=Scrollbar(lst_frame_dir_m)
scrollbar_dir_m.pack(side='right',fill='y')

lst_box_dir_m=Listbox(lst_frame_dir_m, height=10, selectmode='extended',yscrollcommand=scrollbar_dir_m.set,width=30)
lst_box_dir_m.pack(side='left', fill='both',expand=True)
scrollbar_dir_m.config(command=lst_box_dir_m.yview)

#시간출력 프레임
time_out=LabelFrame(root,text='검색시간',padx=5,pady=5)
time_out.pack(fill='both',padx=5,pady=5)

time_a=Entry(time_out,width=20)
time_a.pack(fill='both',padx=5,pady=5)

#경고문구
warning=Label(root,text='*너무 자주 확인 하지 말 것!',fg='red')
warning.pack(side='left')

root.resizable(False,False)
root.mainloop()
