# Uses python3
import sys

def get_fibonaccihuge(n, m):
    p = get_pisano_period(m)
    r = calc_fib(n%p)
    return r % m

def get_pisano_period(m):
    p=3
    f=[0,1,1]
    i=3
    while True:
        f.append((f[i - 1] + f[i - 2]) % m)
        if i != 3 and f[i]==1 and f[i-1]==1 and f[i-2]==0:
            p = len(f) - 3
            break
        i+=1
    return p


def calc_fib(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n,m))
