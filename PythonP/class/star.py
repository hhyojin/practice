from random import randint

#일반유닛
class Unit:
    def __init__(self, name, hp, speed): #생성자. self는 기본적으로 적어줘야 함
        self.name=name #멤버변수 = 클래스 내에서 정의된 변수
        self.hp=hp
        self.speed=speed
        print('{0} 유닛이 생성되었습니다'.format(name))

    def move(self, location):
        print('지상유닛 이동')
        print('{0} : {1} 방향으로 이동합니다. 속도 {2}'\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, self.damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} 유닛은 파괴되었습니다.".format(self.name))


#공격유닛
class AttackUnit(Unit): #Unit 클래스를 상속 받아 만듦
    def __init__(self, name, hp, speed, damage): 
        Unit.__init__(self, name, hp, speed) #Unit 클래스의 초기화. name과 hp 설정 
        self.damage=damage

    def attack(self, location): #self는 기본적으로 적어줘야 함
        print("{0} : {1} 방향으로 적군을 공격. [공격력 {2}]".format(self.name, location, self.damage))

#마린
class Marine(AttackUnit):
    def __init__(self):
         AttackUnit.__init__(self, '마린', 40, 1, 5)

    def stimpck(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. HP 10 감소".format(self.name))
        else:
            print("{0} : 체력이 부족해 스팀팩을 사용하지 않습니다.".format(self.name))

#탱크
class Tank(AttackUnit):
    seize_developed = False #시즈모드 개발여부

    def __init__(self):
         AttackUnit.__init__(self, '탱크', 150, 1, 35)
         self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        #시즈 모드면 시즈모드 아니게, 시즈모드가 아니면 시즈모드로.
        if self.seize_mode == False:
            print('{0} : 시즈모드로 전환합니다'.format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print('{0} : 시즈모드를 해제합니다'.format(self.name))
            self.damage /= 2
            self.seize_mode = False


#공중 유닛. 수송 유닛이라 공격불가
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. 속도 {2}"\
            .format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print('공중유닛 이동')
        self.fly(self.name, location)

#레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, '레이스', 80, 20, 5)
        self.clocked = False #클로킹 모드 해제

    def clocking(self):
        if Tank.seize_developed == False:
            return
        
        if self.clocked == True:
            print('{0} : 클로킹 모드를 해제합니다'.format(self.name))
            self.clocked = False
        else:
            print('{0} : 클로킹 모드를 설정합니다'.format(self.name))
            self.seize_mode = True

def game_Start():
    print("알림: 새로운 게임을 시작합니다.")

def game_Over():
    print("Player: gg")
    print("Player 님이 게임에서 퇴장하셨습니다.")


#-------------게임 진행

game_Start()

m1= Marine()
m2= Marine()
m3= Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

#유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(w1)

#전군 이동
for unit in attack_units:
    unit.move('1시')

#시즈모드 개발
Tank.seize_developed = True
print('알림. 시즈모드 개발이 완료되었씁니다.')

#공격 준비
for unit in attack_units:
    if isinstance(unit, Marine): #이 변수가 특정 클래스의 인스턴스인지 확인하는 것
        unit.stimpck()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

#전군공격
for unit in attack_units:
    unit.attack('1시')

#전군피해
for unit in attack_units:
    unit.damaged(randint(5,21)) #데미지 범위는 5~ 20

#게임종료
game_Over()