# Uses python3
a,b = input().split()
a = int(a)
b = int(b)
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

def LCM(a, b):
    lcm = (a*b)//GCD(a,b)
    return lcm

print(LCM(a,b))
