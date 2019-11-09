"""Fibonacci Number"""

fibonacci_num = 0

def fibonacci_num(n):
    if n in (0, 1):
        return 1
    else:
        return fibonacci_num(n - 1) + fibonacci_num(n - 2)

print('fibonacci number')
print(fibonacci_num(9))
