import csv
import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}
url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename="시가총액.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # newline : 자동 줄 바꿈 없앰 / 한글 깨질 경우 encoding을 utf8에서 utf-8-sig로 수정
writer = csv.writer(f)

#탭으로 구분한 데이터를 리스트 형태로 반환
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t") 

writer.writerow(title)

for page in range(1, 5):
    res = requests.get(url + str(page), headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")

    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 의미 없는 데이터 skip
            continue
        data = [column.get_text().strip() for column in columns]
        #print(data)
        writer.writerow(data) # 데이터는 리스트 형태로 넣어줘야 함 
        