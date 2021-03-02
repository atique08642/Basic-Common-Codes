def prime(a,b):
    for num in range (a,b+1):
        if num>1:
            for i in range(2, num // 2+1):
                if num % i == 0:
                    break;
            else:
                 print (num)


number1,number2 = [int(x) for x in input().split()]
(prime(number1,number2))
