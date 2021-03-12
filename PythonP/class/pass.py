#일반유닛
class Unit:
    def __init__(self, name, hp, speed): #생성자. self는 기본적으로 적어줘야 함
        self.name=name #멤버변수 = 클래스 내에서 정의된 변수
        self.hp=hp
        self.speed=speed

    def move(self, location):
        print('지상유닛 이동')
        print('{0} : {1} 방향으로 이동합니다. 속도 {2}'\
            .format(self.name, location, self.speed))

#공격유닛
class AttackUnit(Unit): #Unit 클래스를 상속 받아 만듦
    def __init__(self, name, hp, speed, damage): 
        Unit.__init__(self, name, hp, speed) #Unit 클래스의 초기화. name과 hp 설정 
        self.damage=damage

    def attack(self, location): #self는 기본적으로 적어줘야 함
        print("{0} : {1} 방향으로 적군을 공격. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, self.damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} 유닛은 파괴되었습니다.".format(self.name))

#공중 유닛. 수송 유닛이라 공격불가
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. 속도 {2}"\
            .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttack(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print('공중유닛 이동')
        self.fly(self.name, location)

#======================================= pass ======================================
#아무것도 안 하고 넘어감. 일단은 완성한 걸로 간주함.
#건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass 

supply_depot = BuildingUnit('서플라이 디폿', 500, '7시') #생성자에 pass 넣었으므로 일단 오류는 안 남

def game_start():
    print('새로운 게임을 시작합니다')

def game_over():
    pass

game_start()
game_over()

