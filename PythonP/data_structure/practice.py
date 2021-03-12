

site = "http://google.com"

url  = site.replace("http://", "")
print('site: ' + url)

url = url[:url.find(".")]
print('url: ' + url)

password = url[:3] + str(len(url)) + str(url.count('e')) +"!"
print(password)

print(f"{site}의 비밀번호는 {password}입니다")
print("{0}의 비밀번호는 {1}입니다.".format(site, password))