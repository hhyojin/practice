#자료구조의 변경

menu = {'커피', '우유','주스'} #집합. 세트
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))