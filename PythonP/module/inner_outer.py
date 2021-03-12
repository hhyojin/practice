#내장함수
#import 필요 없음
#input, dir

#dir: 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random
# print(dir())
# import pickle
# print(dir())
# print(dir(random))

# lst = [1,2,3]
# print(dir(lst))

# name = 'jim'
# print(dir(name))

#list of built in functions

#외장함수: 직접 import 해서 써야 하는 것. list of python modules
#glob: 경로 내의 폴더/파일 조회
# import glob
# print(glob.glob("*.py"))

#os: 운영체제에서 제공하는 기본 기능
import os
# print(os.getcwd()) #현재 디렉토리 표시

# folder = "sample_dir"

# if os.path.exists(folder):
#     print('이미 존재하는 폴더')
#     os.rmdir(folder)
#     print(folder, '폴더를 삭제하였습니다')
# else:
#     os.makedirs(folder) #폴더생성
#     print(folder, '폴더를 생성하였습니다')

# print(os.listdir()) #glob과 비슷한 기능

import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
# print('오늘 날짜는', datetime.date.today())

today = datetime.date.today()
td = datetime.timedelta(days=100) #100일 뒤 날짜
print('오늘로부터 100일 뒤: ', today+td)