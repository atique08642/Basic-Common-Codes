def GCD(a,b):
    if a>b:
        smaller = b
    elif (b>a):
        smaller = a
    for i in range (1, smaller +1):
        if (a % i == 0 and b % i== 0):
            gcd = i
    return gcd
num1 = int(input())
num2 = int(input())
print(GCD(num1,num2))
