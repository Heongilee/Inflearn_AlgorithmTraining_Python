import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    line = input().rstrip()
    maxV = ''
    minV = ''
    lt, rt = 0, 0
    while lt < len(line):
        flag = False
        while rt < len(line) and line[rt] != 'K':
            rt += 1
        if rt >= len(line):
            minV += str(10 ** (rt - lt - 1))
            maxV += ('1' * (rt - lt))
        elif line[rt] == 'K':
            maxV += str(5 * (10 ** (rt - lt)))
            if lt == rt:
                minV += '5'
            else:
                minV += str(10 ** (rt - lt - 1)) + '5'
        rt += 1
        lt = rt
    print(maxV)
    print(minV)
    

####################################################################################
# 내 풀이 (1) : TLE
###############################################################################
'''
sys.setrecursionlimit(10 ** 6)
INF = int(10e9)
def DFS(v):
    global maxV, minV
    i = 1
    if i + v > L:
        esc = False
        j = 0
        number = ''
        for item in sack:
            myString = myInput[j:j + item]
            if len(myString) >= 2:
                for k in range(len(myString) - 1):
                    if (myString[k] == 'K' and myString[k + 1] == 'M') or (myString[k] == 'K' and myString[k + 1] == 'K'):
                        esc = True
                        break
                if esc: break

            t = str((5 if myString[-1] == 'K' else 1) * (10 ** (item - 1)))
            number += t
            j += item
        if esc: return
        number = int(number)
        # print(sack, number)
        # 최대 최소 계산
        minV = number if number < minV else minV
        maxV = number if number > minV else maxV
        return

    while i + v <= L:
        sack.append(i)
        DFS(v + i)
        sack.pop()
        i += 1

if __name__ == '__main__':
    myInput = input().rstrip()
    L = len(myInput)
    sack = []
    minV, maxV = INF, 0

    DFS(0)
    print(maxV)
    print(minV)
'''