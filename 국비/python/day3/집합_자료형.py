# 집합 자료형은 어떻게 만들까?

s1 = set([1, 2, 3])
print(s1)

print()

s2 = set("Hello")
print(s2)

print()
#------------------------------------------------------------------------------------
# 집합 자료형의 특징

s1 = set([1, 2, 3])
l1 = list(s1)
print(l1)
print(l1[0])

print()

t1 = tuple(s1)
print(t1)
print(t1[0])

print()
#------------------------------------------------------------------------------------
# 교집합, 합집합, 차집합 구하기

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)
print(s1.intersection(s2))

print()

# 합집합 구하기

print(s1 | s2)
print(s1.union(s2))

print()

# 차집합 구하기

print(s1 - s2)
print(s2 - s1)
print(s1.difference(s2))
print(s2.difference(s1))

print()
#------------------------------------------------------------------------------------
# 집합 자료형 관련 함수

# 값 1개 추가하기 - add

s1 = set([1, 2, 3])
s1.add(4)
print(s1)

print()

# 값 여러 개 추가하기 - update

s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

print()

# 특정 값 제거하기 - remove

s1 = set([1, 2, 3])
s1.remove(2)
print(s1)















