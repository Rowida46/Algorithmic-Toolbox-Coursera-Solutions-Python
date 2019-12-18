# Uses python3
n = int(input())
def FibonacciLastDigit(n):
    a = 0
    b = 1
    for i in range(n):
        a,b = b % 10, a+b % 10
    return a

print(FibonacciLastDigit(n))
