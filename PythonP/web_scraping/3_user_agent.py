import requests

url= "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status() #status_code로 일일이 확인할 필요 없이 이거 쓰면 문제 있으면 프로그램 종료시켜 줌.

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)