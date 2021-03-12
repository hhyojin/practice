#일반유닛
class Unit:
    def __init__(self):
        print('Unit 생성자')


class Flyable:
    def __init__(self):
        print('Flyable 생성자')

#공중 공격 유닛 클래스
class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super를 통해 초기화 할 때는 () 붙이고 self 없음
        #super().__init__()  
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()
#super로 상속 받으면 첫번째 부모 클래스만 상속 받음.
#그러므로 다중상속인 경우는 부모 클래스별로 초기화 해야 함