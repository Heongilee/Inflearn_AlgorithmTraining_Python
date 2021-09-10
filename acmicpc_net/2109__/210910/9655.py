import sys
sys.stdin = open("./acmicpc_net/input.txt", "rt")
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    quo, rem = divmod(n, 3)
    
    if quo % 2 == 0:
        if rem == 1:
            print("SK")
        else:
            print("CY")
    else:
        if rem == 1:
            print("CY")
        else:
            print("SK")