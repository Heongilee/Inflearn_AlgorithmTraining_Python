N = 5
board = [[[] for _ in range(N)] for _ in range(N)]
board[0][0].append([1, 0, 0, False])
for b in board:
    print(b)
#################################################################
#
'''
a = [0, 0, 0, 0, 0]

b = a[:]
print(b) # [0, 0, 0, 0, 0]
b[0] = 1
print(a, b) # [0, 0, 0, 0, 0] [1, 0, 0, 0, 0]

'''
'''
res = ~int('0b0000', 2) + 1
print(bin(res))
'''
#################################################################
# set 자료구조 - 연산자
############################################################
'''
# res = solution(10, [5,4,3,2,1], [3,1,2,5,4])  # 10
# res = solution(9, [2, 4, 7, 8], [3, 6, 9])  # 8
# res = solution(4, [3, 1, 2], [2, 4, 3])     # 3
A = set([3, 1, 2])
B = set([2, 4, 3])

print("lost : ", A - B)
print("reserve : ", B - A)
'''


#################################################################
# 백준 풀 때 빠른 입력받기 팁
############################################################
'''
import sys
import time
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline
SIZE = 980000
if __name__ == '__main__':
    st = time.time()
    for _ in range(SIZE):
        t = input()
    en = time.time()

    print(f"time : {round(en - st, 10)}sec")
'''

#################################################################
# Swapping Algorithm without tmp
############################################################
'''
def solution(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

if __name__ == '__main__':
    a = 214748
    b = 356419

    print("Before:\t", a, b)
    a, b = solution(a, b)
    print("After:\t", a, b)
'''
#################################################################
# *, ** means
############################################################
'''
def f2(**kwargs):
    print(kwargs, type(kwargs))
    print(kwargs.keys())
    print(kwargs.values())

    for K, V in kwargs.items():
        print("Key :", K, ", Value :", V)

f2(K1 = "V1", K2 = "V2", K3 = "V3", K4 = "V4")
'''
#################################################################
# Priority Queue
############################################################
'''
from queue import PriorityQueue

if __name__ == '__main__':
    pq_infiniteSize = PriorityQueue()   # 사이즈가 무한대인 빈 우선순위 큐 생성
    pq_maximumSize = PriorityQueue(maxsize=5)   # 사이즈가 6인 빈 우선순위 큐 생성

    # TIP: 정렬기준을 바꾸고자 한다면 아래와 같이 데이터 구조를 저장해보자!
    # (우선순위, 값)
    pq_maximumSize.put((3, 'L'))
    pq_maximumSize.put((0, 'A'))
    pq_maximumSize.put((2, 'P'))
    pq_maximumSize.put((4, 'E'))
    pq_maximumSize.put((1, 'P'))

    # 출력문
    for i in range(5):
        t = pq_maximumSize.get()[1]
        print(t, end='')
    print()
'''
#################################################################
# 테스트케이스 작성
############################################################
'''
f = open("./acmicpc_net/tc1.txt", "w")
f.write("10000 10000\n")
for i in range(1, 10001):
    if i == 10000:
        data = "10000 1\n"
    else:
        data = str(i) + " " + str(i + 1) + "\n"
    # print(data)
    f.write(data)
f.close()
'''
##################################################################
# Test zone
#############################################################
# print(int(10e8))
'''
from random import randrange
f = open("./acmicpc_net/tc1.txt", "w")
n = 500000
k = 500

print(n, k)
f.write(str(n) + " " + str(k) + "\n")

for _ in range(n):
    t = randrange(0, 10)
    f.write(str(randrange(0, 10)))
    # print(t, end='')
print("complete")
f.close()
'''