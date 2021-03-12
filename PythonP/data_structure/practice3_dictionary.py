#사전. 키밸류로 이루어짐

cabinet = {3: 'a', 100:'b'}
print(cabinet[3])
print(cabinet.get(3))
print(cabinet.get(5))
print(cabinet.get(5, '사용가능')) #5번키 값을 가져오고 없으면 2번째 파라미터를 출력


print(3 in cabinet) # key in variable
print(5 in cabinet)


cabinet = {'A-2': 'a', 'b-100':'b'}
print(cabinet['A-2'])

#추가
cabinet['A-2'] ='A'
cabinet['c-39'] = 'c'
print(cabinet)

#삭제
del cabinet['A-2']
print(cabinet)

#키만 출력
print(cabinet.keys())

#값만 출력
print(cabinet.values())

#키와 값 쌍으로 출력
print(cabinet.items())

#모든 값 삭제
print(cabinet.clear())