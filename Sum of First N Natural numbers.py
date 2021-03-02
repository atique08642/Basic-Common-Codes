def sum(number):
    counter=0
    for i in range (0,number+1):
        counter+=i
    return counter

number=int(input())
result=sum(number)
print(result)