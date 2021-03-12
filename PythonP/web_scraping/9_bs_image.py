import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}



for year in range(2015, 2020): # 2015 ~ 2019년까지

    url = "https://search.daum.net/search?w=tot&q={0}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for index, image in enumerate(images):
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url

        print(image_url)
        image_res = requests.get(image_url, headers=headers)
        image_res.raise_for_status()

        with open("movie_{0}_{1}.jpg".format(year, index+1), "wb") as f:
            f.write(image_res.content)

        if index >=4: # 상위 5개 이미지까지만 다운로드
            break
        