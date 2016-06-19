# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    s = 1
    while s <= n:
        if n <= 2 * s:
            summands.append(n)
            break
        else:
            summands.append(s)
            n-=s
        s += 1
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # n=20
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
