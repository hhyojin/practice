temp = int(input('지금 온도 설정'))

if temp >= 30:
    print('더움')
elif 10 <= temp < 30:
    print('좋은 날씨')
elif 0 <= temp and temp <10:
    print('쌀쌀')
else:
    print('노 외출')

    # || 나 & str은 사용 불가인듯

temp = 'A'

if temp == 'A' & temp =='B':
    print('더움')
elif 10 <= temp < 30:
    print('좋은 날씨')
elif 0 <= temp and temp <10:
    print('쌀쌀')
else:
    print('노 외출')