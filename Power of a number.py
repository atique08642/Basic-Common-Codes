def power(base, exponent):
    temp = 1
    for i in range(1, exponent+1):
        temp = temp * base
    print(temp)


base, exponent = [int(x) for x in input().split()]
power(base,exponent)
