def oepn_account():
    print("새로운 계좌가 생성되었습니다.")

oepn_account()


def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance+money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

def withdraw_night(balance, money): #저녁 출금으로 인한 수수료
    commission = 100 #수수료
    return commission, balance-money-commission #튜플형식으로 리턴

balance = 0
balance = deposit(balance, 1000)
# print(balance)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이고 잔액은 {1}원입니다.".format(commission, balance))