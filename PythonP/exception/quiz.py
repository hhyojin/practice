# 조건1 : 1보다 작거나 숫자가 아닌 입력값일 때는 ValueError
#     출력메시지: 잘못된 값

# 조건2: 대기 손님이 주문할 수 있는 양은 10마리
#     재고 소진 시 사용자 정의 에러 SoldOutError 발생 후 프로그램 종료
#     출력 메시지: 재고 소진

class SoldOutError(Exception):
    def __init__(self):
        pass

chicken = 10
waiting = 1

while(True):
    try:
        print('남은 치킨: {0}'.format(chicken))
        order = int(input('몇 마리 주문할래'))

        if order > chicken:
            print('재료 부족')

        elif order <= 0:
            raise ValueError

        else:
            print('대기번호 {0} : {1}마리 주문 완료'.format(waiting, order))
            waiting += 1
            chicken -= order
        
        if chicken == 0:
            raise SoldOutError
            
    
    except ValueError:
        print('잘못된 값')

    except SoldOutError:
        print('재고소진')
        break
