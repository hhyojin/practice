#일반유닛
class Unit:
    def __init__(self, name, hp): #생성자. self는 기본적으로 적어줘야 함
        self.name=name #멤버변수 = 클래스 내에서 정의된 변수
        self.hp=hp

#공격유닛
class AttackUnit(Unit): #Unit 클래스를 상속 받아 만듦
    def __init__(self, name, hp, damage): 
        Unit.__init__(self, name, hp) #Unit 클래스의 name과 hp 설정 
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
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

#새 유닛 생성
valkyrie = FlyableAttack("발키리",200,6,5)
valkyrie.fly(valkyrie.name, '3시')