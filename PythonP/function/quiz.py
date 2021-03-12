# 표준체중을 구하시오,

# 남자: 키(m) x 키(m) x 22
# 여자: 키(m) x 키(m) x 21


# 조건: 표준체중은 별도의 함수 내에서 계산
#     함수명: std_weight
#     전달값: 키(height), 성별(gender)

# 조건2: 표준 체중은 소수점 두자리까지 표시

# (출력예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.


# def std_weight(height, gender):
#     weight = 0
#     height_m = height * 0.01
#     height_m = round((height_m ** 2),2)
#     if gender =="여자" :
#         weight = round(height_m * 21,2)
#     else :
#         weight = round(height_m * 22,2)

#     print ("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))


# std_weight(164, "남자")

#==================================================

def std_weight(height, gender):
    if gender =="여자" :
        return height * height * 21
    else :
        return height * height * 22

height = 175
gender ="남자"

weight = round(std_weight(height / 100, gender),2)

print ("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))