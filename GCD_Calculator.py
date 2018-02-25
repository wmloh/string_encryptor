def gcd(a,b):
    if a == 0 and b == 0:
        return 0
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        k = min(a,b)
        m = max(a,b)
        l = k
        k = m % k
        return gcd(k,l)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_i(i):
    x, y = 0, 1
    for k in range(i):
        x, y = y, x + y
    return x
