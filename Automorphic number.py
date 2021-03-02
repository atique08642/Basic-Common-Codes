def automorphic(n):
    square = n * n
    while n:
        if (n%10 != square%10):
            return False
        n //= 10
        square //= 10
    return True



number = int(input())
if automorphic(number):
    print("automorphic")
else:
    print("is NOT AUTOMORPHIC")