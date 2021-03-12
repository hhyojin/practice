# import .. package_travel.thai #import에는 모듈이나 패키지만 가능. 함수나 클래스는 불가
# trip_to = package_travel.thai.ThaiPackage()
# trip_to.detail()

# from package_travel.thai import ThaiPackage #from import에는 함수나 클래스 가능
# trip_to = ThaiPackage()
# trip_to.detail()


from package_travel import *
# # trip_to = viet.VietPackage()
# # trip_to.detail()
# trip_to = thai.ThaiPackage()
# trip_to.detail()

#패키지, 모듈 위치 확인
# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thai))