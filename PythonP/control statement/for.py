# for waiting_no in [0,1,2,3,4]:
#     print ("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(5): # 0~4
#     print ("대기번호1 : {0}".format(waiting_no))

# for waiting_no in range(1,6): # 1~5
#     print ("대기번호1 : {0}".format(waiting_no))




#출석번호 1, 2, 3, 4 앞에 100 붙이기로 함. 101, 102, 103
# student = [1,2,3,4,5]
# print(student)
# student = [i+100 for i in student]
# print(student)


#학생 이름을 길이로 변환
# student = ["a","bb","ccc", "dddd"]
# student = [len(i) for i in student]
# print(student)


#학생 이름을 대문자로 변환
student = ["a","bb","ccc", "dddd"]
student = [i.upper() for i in student]
print(student)