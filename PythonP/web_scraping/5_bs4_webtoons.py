import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # html 문서를 lxml parser를 통해 bs 객체로 만듦
# find : 조건에 해당하는 첫 번째 element / find_all : 조건에 해당하는 모든 element
# class 속성이 title인 모든 a element의 텍스트
cartoons = soup.find_all("a", attrs={"class":"title"})
for cartoon in cartoons:
    print(cartoon.get_text())

    