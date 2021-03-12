

print("Python", "Java")
print("Python", "Java", sep=",")
print("Python", "Java", "JavaScript", sep=" vs ")
print("Python", "Java", sep=",", end="?") #문장의 끝 부분을 물음표로 변경하는 것
print("무엇이 더 재밌을까요?")

#===================================================================

# import sys
# print("Python", "Java", file=sys.stdout) #표준 출력
# print("Python", "Java", file=sys.stderr) #표준 에러로 처리

#===================================================================

# scores = {"수학": 0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     #print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") #ljust(8) 8개의 공간을 만들고 왼쪽 정렬 #rjsut(4) 4칸의 공간을 확보하고 오른쪽 정렬

#===================================================================

# for num in range(1, 21): #1~20
#     print("대기번호 : " + str(num).zfill(3)) #zfill(3) 3 크기만큼 공간을 만들고 나머지는 0으로 채움

#===================================================================

# answer = input("아무 값이나 입력하세요: ")
# print(type(answer))
# print("입력한 값은 " + answer + "입니다.")