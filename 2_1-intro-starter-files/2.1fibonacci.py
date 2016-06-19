#fibonacci numbers naive algorithm

def fibRecurs(n):
    if n<=1:
        return n
    else:
        return fibRecurs(n-1) + fibRecurs(n-2)

def fibBetter(n):
    f=[0,1]
    for i in range(2,n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]


print(fibBetter(1000))
