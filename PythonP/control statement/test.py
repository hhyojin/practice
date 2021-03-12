# 50명의 승객과 매칭 기회가 있을 때, 총 탑승승객 수를 구하시오

# 조건1: 승객별 운행 소요시간은 5~50분으로 랜덤
# 조건2: 소요시간 5~15분 사이의 승객만 매칭해야 함.
from random import *

# index = 1
# customer = 0

# while index <= 5 0:
#     time= randint(5, 50)
#     print("{0}번째 손님. (소요시간: {1}분)".format(index, time))
#     index += 1

#     if 5 <= time <= 15:
#         customer += 1

# print("총 탑승승객: {0}분".format(customer))

customer = 0
for i in range(1,51):
    time =randrange(5,51)
    if 5<= time <=15:
        print("{0}번째 손님. (소요시간: {1}분)".format(i, time))
        customer += 1

    else:
        print("{0}번째 손님. (소요시간: {1}분)".format(i, time))

print("총 탑승승객: {0}분".format(customer))