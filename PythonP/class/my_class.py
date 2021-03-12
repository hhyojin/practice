# class Unit:
#     def __init__(self, name, hp, damage): #생성자. self는 기본적으로 적어줘야 함
#         self.name=name #멤버변수 = 클래스 내에서 정의된 변수
#         self.hp=hp
#         self.damage=damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름: {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) #이렇게 멤버변수를 클래스 밖에서 사용할 수 있음

# #==========================================

# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True #외부애서 변수를 추가로 할당/확장 가능

# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# if wraith1.clocking == True: #여기에는 clocking 아런 변수 없음.
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

#공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage): #생성자. self는 기본적으로 적어줘야 함
        self.name=name #멤버변수 = 클래스 내에서 정의된 변수
        self.hp=hp
        self.damage=damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

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