def fibonacci(n):
    num1, num2 = 0, 1
    print(num1)
    print(num2)
    for i in range(2, n+1):
        temp = num1
        num1 = num2
        num2 = temp + num1

        print(num2)


number = int(input())
fibonacci(number)
