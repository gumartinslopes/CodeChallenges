# Fibonacci sequence
# 1, 1, 2, 3, 5, 8


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2) 

for i in range(11):
    print(f'Fib of {i}: ', fib(i))