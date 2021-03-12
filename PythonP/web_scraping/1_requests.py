#requests : 웹페이지의 문서정보를 가져오기 위한 라이브러리

import requests
res = requests.get("http://naver.com")
#print(res.status_code)
res.raise_for_status() #status_code로 일일이 확인할 필요 없이 이거 쓰면 문제 있으면 프로그램 종료시켜 줌.


print(len(res.text))

#페이지 내용을 html 파일로 만듦
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)