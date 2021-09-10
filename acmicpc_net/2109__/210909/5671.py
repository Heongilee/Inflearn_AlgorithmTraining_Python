import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    for line in sys.stdin:
        n, m = map(int, line.rstrip().split())
        cnt = 0
        
        for i in range(n, m + 1):
            esc = False
            chk = dict(zip(range(10), [0] * 10))
            while i > 0:
                rem = i % 10
                if chk[rem] >= 1:
                    esc = True
                    break
                chk[rem] += 1
                i = i // 10
            if not esc: cnt += 1
        print(cnt)