# 보고서 작성

# - X 주차 주간보고 -
# 부서:
# 이름:
# 업무 요약:

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램 작성

# 조건: 파일명은 '1주차.txt', '2주차.txt' ...로 만들어야 함.

import pickle

for i in range(1, 11):
    with open(str(i)+"주차.txt","w",encoding="utf-8") as file:
        # file.write("- " + str(i) + " 주차 주간보고 -")
        file.write("- {0} 주차 주간보고 -".format(i))
        file.write("\n부서: ")
        file.write("\n이름: ")
        file.write("\n업무요약: ")