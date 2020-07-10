a=[23, 12, 36, 53, 19]
my_str = "Hello_world!!"

# 인덱스 범위의 원소들을 리스트 형태로 출력.
print(a[:3])    # 0~2번 인덱스까지 리스트 형태로 출력.
print(a[1:4])    # 1~3번 인덱스까지 리스트 형태로 출력.

# 리스트의 길이를 구해주는 함수
print(len(a))

# 리스트 순회
for i in range(len(a)):
    print(a[i], end=' ')
print() # \n

for e in a:
    if(e % 2 != 0):
        print(e, end=' ')
print() # \n

# enumerate(리스트) -> 리스트 원소를 인덱스 번호와 Tuple 형태로 x에 담긴다.
for x in enumerate(a):
    # x에 (0, 23), (1, 12), (2, 36), (3, 53), (4, 19) 이렇게 들어감
    # 소괄호로 묶인다는건 튜플(Tuple)이라는 뜻이다.
    # print(x, end=' ')
    
    # Tuple도 리스트와 똑같이 접근하기 때문에, 다음처럼 출력할 수 있다.
    print("(", x[0], ",", x[1], ")", end='')
print()

for index, value in enumerate(a):
    print("(", index, ", ", value, ")", end='')
print()
####################################################################################
# Tuple 이란??
b=(1, 2, 3, 4, 5)   # 튜플 자료구조로 담긴다.
print(b[0])
# b[0] = 7      # TypeError: 'tuple' object does not support item assignment
# print(b[0])   # 에러 발생.

# TIP : 튜플과 리스트의 차이점
# 1. 튜플은 값을 변경할 수 없다. b[0] = 7   -> 안됨.
####################################################################################
# if all과 if any
if all(60>x for x in a):
    #모든 원소가 60보다 작아야 참이 되고, 이 조건으로 분기된다.
    print("a리스트의 원소들이 전부 60보다 작습니다!")
else:
    # 원소 중 하나가 참이 되지 않을 경우, 참이 되지 않아 else로 분기됨.
    print("a리스트의 원소들 중 하나가 60보다 큽니다!")
    
if any(15>x for x in a):
    # 리스트 a의 원소 중 하나라도 15보다 작은 값이 존재하면 이 조건으로 분기 됨.
    print("YES")
else:
    # 원소 중 한 개라도 15보다 작은 값이 없을 경우, 이 조건으로 분기 됨.
    print("NO")

