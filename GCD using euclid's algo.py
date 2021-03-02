def GCD(a,b):
    if b == 0:
        return a
    else:
        return GCD(b,a%b)
number1 = int(input())
number2 = int(input())
print(GCD(number1,number2))