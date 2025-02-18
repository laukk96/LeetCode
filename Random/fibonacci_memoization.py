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


t1 = time.time()
result = fib_hashMemo(17)
t2 = time.time()

print(f"result: {result}, difference in time = {t2 - t1}")