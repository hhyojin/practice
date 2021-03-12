from selenium import webdriver

browser = webdriver.Chrome("D:/dev/VsProject/PythonP/web_scraping/chromedriver.exe") # 크롬 드라이버가 다른 경로에 있는 경우에는 해당 경로를 () 안에 입력해주면 됨
browser.get("https://www.naver.com/")