def sum(a,b):
    sum=0
    for i in range (a,b+1):
        sum=sum+i
    return sum

a,b=[int(a) for a in input().split()]
result=sum(a,b)
print(result)