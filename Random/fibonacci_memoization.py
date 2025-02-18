import time

fibCall = {}

def fib_hashMemo(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in fibCall:
        print(f"n in fibCall ! {n}")
        return fibCall[n]
	
    fibCall[n] = fib_hashMemo(n-1) + fib_hashMemo(n-2)
    print(f'> Adding fibCall[{n}] : {fibCall[n]}')
    return fibCall[n]

def fib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
	
    return fib(n-1) + fib(n-2)

t1 = time.time()
result = fib_hashMemo(17)
t2 = time.time()
print(f"Hash fib result: {result}, difference in time = {t2 - t1}")

t3 = time.time()
result = fib(17)
t4 = time.time()

print(f"Normal fib result: {result}, difference in time = {t4- t3}")
