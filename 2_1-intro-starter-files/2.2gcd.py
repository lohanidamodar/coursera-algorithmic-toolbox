def naiveGCD(a,b):
    d=0
    for i in range(1,a+b):
        if a%i==0 and b%i==0:
            d=i
    return d

def efficientGCD(a,b):
    if b==0:
        return a
    ap = a%b
    return efficientGCD(b,ap)

print(efficientGCD(357,234))
