import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # html 문서를 lxml parser를 통해 bs 객체로 만듦
# print(soup.title) # title 태그
# print(soup.title.get_text()) # title 태그의 텍스트만
# print(soup.a) # soup 객체에서 첫번째로 발견된 a 태그 가져옴
# print(soup.a.attrs) # a 태그의 속성 정보 출력
# print(soup.a["href"]) # a 태그의 특정 속성 출력 

#print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class가 Nbtn_upload인 a element
#print(soup.find(attrs={"class":"Nbtn_upload"})) # class가 Nbtn_upload인 element

#print(soup.find("li", attrs={"class":"rank01"})) # class가 Nbtn_upload인 element
rank1 = soup.find("li", attrs={"class":"rank01"})
#print(rank1.a.get_text()) # rank1 중 a 태그만 선택
## 형제 next_sibling / previous_sibling / find_next_sibling / find_previous_sibling / find_next_siblings
# print(rank1.next_sibling)
# rank2= rank1.next_sibling.next_sibling
# rank3= rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# rank1 = rank2.find_previous_sibling("li")
# print(rank1)
# rank2 = rank1.find_next_sibling("li")
# print(rank2)
# print(rank1.find_next_siblings("li"))

## 부모 parent
#print(rank1.parent)

webtoon = soup.find("a", text="소녀의 세계-2부 45화") # text가 저 내용인 a 태그
print(webtoon)