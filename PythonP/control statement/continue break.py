absent = [2,5] #결석
no_book = [7]
for student in range(1, 11): # 1~10
    if student in absent:
        continue
    elif student in no_book:
        print("끝. {0} 따라와".format(student))
        break
    print("{0}, 읽어".format(student))
