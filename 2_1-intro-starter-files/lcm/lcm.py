# Uses python3
import sys

def lcm(a, b):
    return a*b // gcd(a,b)

def gcd(a, b):
    if b == 0:
        return a
    ap = a % b
    return gcd(b, ap)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

