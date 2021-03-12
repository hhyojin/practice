# score_file = open("score.txt","w",encoding="utf-8") #w=write 덮어쓰기
# print("수학: 0", file=score_file) #이건 자동으로 줄 바꿈 됨
# print("영어: 50", file=score_file)
# score_file.close()


# score_file = open("score.txt","a",encoding="utf-8") #a = append 덮지 않고 이어 쓰기
# score_file.write("과학:80")
# score_file.write("\n코딩:100") #이건 줄바꿈 안되므로 줄바꿈 해줘야 함
# score_file.close()

#전체 불러오기
# score_file = open("score.txt", "r",encoding="utf-8") #r = read
# print(score_file.read())
# score_file.close()

#한 줄 불러오기
# score_file = open("score.txt", "r",encoding="utf-8") #r = read
# print(score_file.readline()) #줄별로 읽고, 커서는 다음 줄로 이동
# print(score_file.readline()) #줄별로 읽고, 커서는 다음 줄로 이동
# print(score_file.readline(), end="") #커서 다음 줄로 이동 안 함
# print(score_file.readline()) 
# score_file.close()

# score_file = open("score.txt", "r",encoding="utf-8") #총 라인이 몇 줄인지 모를 때
# while  True:
#     line = score_file.readline()
#     if not line: #라인이 없는 경우
#         break
#     print(line, end="")
# score_file.close()

score_file = open("score.txt", "r",encoding="utf-8") 
lines = score_file.readlines() #list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
