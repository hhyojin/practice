#pickle = 프로그램에서 사용하는 데이터를 파일 형태로 저장하는 것
#파일명을 pickle.py로 저장하면 오류 나니 파일 이름 다르게 지정할 것

import pickle
profile_file=open("profile.pickle","wb") #w=write, b=binary. 인코딩은 지정해 줄 필요 없음
profile ={"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
print("담기: " + str(profile))
pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
profile_file.close()

profile_file=open("profile.pickle","rb")
profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
print("읽기: " + str(profile))
profile_file.close()

#with : 파일 open close를 편하게 해줌
with open("profile.pickle","rb") as profile_file: #profile.pickle 파일을 열어서 profile_file에 담음
    print("with: " + str(pickle.load(profile_file))) #따로 close할 필요 없이 with문 탈출하며 자동 종료


with open("study.txt","w",encoding="utf-8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt","r",encoding="utf-8") as study_file:
    print(study_file.read())