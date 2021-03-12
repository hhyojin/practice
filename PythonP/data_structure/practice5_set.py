#집합 (set)
# 중복 안 됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)

java = {'A','B', 'C'}
python = set(['A', '가'])

#교집합 (java와 python 모두 할 수 있는)
print(java & python)
print(java.intersection(python))

#합집합 (java를 할 수 있거나 python을 할 수 있는)
print(java | python)
print(java.union(python))

#차집합 (java는 할 수 있지만 python은 할 줄 모르는)
print(java - python)
print(java.difference(python))

#python 할 줄 아는 사람 늘어남
python.add('D')
print(python)

#java 까먹음
java.remove('B')
print(java)