class ThaiPackage: #패키지: 모듈을 모아놓은 집합
    def detail(self):
        print('태국패키지. 야시장 투어 50만원')

#모듈 내부에서 쓰는 건지 외부에서 쓰는 건지 판별 가능
if __name__ == "__main__":
    print('thai 모듈을 직접 실행') 
    print('이 문장은 모듈을 직접 실행할 때만 실행') 
    trip_to = ThaiPackage()
    trip_to.detail()

else:
    print('Thai 외부에서 모듈 실행')