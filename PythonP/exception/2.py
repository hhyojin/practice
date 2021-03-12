#사용자 정의 예외처리
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print('한자리 숫자 나누기 전용 계산기')
    num1 = int(input('첫번째 숫자 입력: '))
    num2 = int(input('두번째 숫자 입력: '))

    #의도적으로 에러 발생
    if num1 >= 10 or num2 >= 10:
        raise ValueError

    if num1 == 5:
        raise BigNumberError('입력값 : {0}, {1}'.format(num1, num2))

    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

except ValueError:
    print('잘못된 숫자 입력. 한자리 숫자만 입력해')
except BigNumberError as err:
    print('에러')
    print(err)
finally:
    print('계산 끗')