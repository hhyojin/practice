# customer ="토르"
# index = 5
# while index >=1 :
#     print("{0}, 커피 준비됨. {1}번 남음".format(customer, index))
#     index -=1
#     if index ==0:
#         print("커피 폐기됨")

# customer ="토르"
# index = 1
# while True :
#     print("{0}, 커피 준비됨. {1}번 호출".format(customer, index))
#     index +=1

customer ="토르"
person = "Unknown"

while person != customer :
    print("{0}, 커피 준비됨. ".format(customer))
    person = input("이름 뭐임? ")
