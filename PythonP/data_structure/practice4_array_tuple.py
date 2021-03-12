#리스트와 다르게 내용 수정 불가. 다만 속도는 리스트보다 빠름

menu = ('a','b')
print(menu[0])
print(menu[1])

name='rrrr'
age = 20
hobby = 'hobby'

#한번에 값 지정해주기 좋음
(name, age, hobby) = ('bb', 30, '자기')
print(name, age, hobby)