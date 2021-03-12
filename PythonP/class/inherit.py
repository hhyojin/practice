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

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)