gun=10

# def checkpoint(soldiers):
#     gun = gun-soldiers
#     print("남은 총 개수: {0}".format(gun))


# def checkpoint(soldiers):
#     global gun #전역변수 gun을 쓰겠다는 의미.
#     gun = gun-soldiers
#     print("남은 총 개수: {0}".format(gun))

# checkpoint(2)


def checkpoint(gun, soldiers):
    gun = gun-soldiers #이 gun은 이제 지역변수임. 그러므로 전역변수에 변경된 gun을 리턴해줘야 함
    print("함수 내 남은 총 개수: {0}".format(gun))
    return gun


gun=checkpoint(gun, 2)
print("남은 총 개수: {0}".format(gun))