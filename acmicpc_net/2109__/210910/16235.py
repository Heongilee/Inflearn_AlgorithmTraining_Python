import sys, heapq as hq
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

##############################################################################
# 1% TLE in Pypy3
#########################################################################
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
if __name__ == '__main__':
    N, M, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    nutrient = [[5] * N for _ in range(N)]
    # (위치 X, 위치 Y, 활성 나무 개수)
    tree = []
    # (나이, 사망여부)
    board = [[[] for _ in range(N)] for _ in range(N)]
    
    for _ in range(M):
        x, y, z = map(int, input().split())
        tree.append([x - 1, y - 1, len(board[x - 1][y - 1]) + 1])
        board[x - 1][y - 1].append([z, False])
    
    # K년 동안 반복시킬 루틴
    for _ in range(K):
        visited = [[False] * N for _ in range(N)]
        # 봄
        for i in range(len(tree)):
            x, y, cnt = tree[i][0], tree[i][1], tree[i][2]
            if not visited[x][y]:
                visited[x][y] = True
                L = len(board[x][y])
                board[x][y].sort()           # 나이 순으로 정렬

                myList = board[x][y]    # myList에는 (x, y)에 있는 나무의 (나이, 사망여부)가 들어있다.
                for j in range(L):
                    age, death = myList[j][0], myList[j][1]
                    if nutrient[x][y] < age:
                        board[x][y][j][1] = True    # myList[j][1] = True
                    else:
                        nutrient[x][y] -= age
                        board[x][y][j][0] += 1      # myList[j][0] += 1
        
        # 여름
        visited = [[False] * N for _ in range(N)]
        for i in range(len(tree)):
            x, y, cnt = tree[i][0], tree[i][1], tree[i][2]
            if not visited[x][y]:
                visited[x][y] = True

                myList = board[x][y]    # myList에는 (x, y)에 있는 나무의 (나이, 사망여부)가 들어있다.
                j = 0
                while j < len(board[x][y]):
                    age, death = myList[j][0], myList[j][1]

                    if death:
                        nutrient[x][y] += age // 2
                        tree[i][2] -= 1
                        board[x][y].pop(j)
                        continue
                    j += 1
                
        # 가을
        visited = [[False] * N for _ in range(N)]
        L = len(tree)
        for i in range(L):
            x, y, cnt = tree[i][0], tree[i][1], tree[i][2]
            if not visited[x][y]:
                visited[x][y] = True

                myList = board[x][y]    # myList에는 (x, y)에 있는 나무의 (나이, 사망여부)가 들어있다.
                for j in range(len(myList)):
                    age, death = myList[j][0], myList[j][1]
                    if age % 5 == 0:
                        for k in range(8):
                            xx = x + dx[k]
                            yy = y + dy[k]
                            if 0 <= xx < N and 0 <= yy < N:
                                if len(board[xx][yy]) >= 1:
                                    for l in range(len(tree)):
                                        if tree[l][0] == xx and tree[l][1] == yy:
                                            tree[l][2] += 1
                                            break
                                else:
                                    tree.append([xx, yy, 1])
                                board[xx][yy].append([1, False])

        # 겨울
        for r in range(N):
            for c in range(N):
                nutrient[r][c] += A[r][c] # 양분 추가지급 (by 로봇)
    print(sum([c for _, _, c in tree]))