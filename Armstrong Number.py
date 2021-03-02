def armstrong(number):
    temp=number
    sum=0
    while(number>0):
        remainder=number%10
        sum=sum + remainder**3
        number=number//10
    if temp==sum:
        return ("Armstrong no is {}".format(sum));
    else:
        return ("{} is not a armstrong no.".format(temp))
number=int(input())
print(armstrong(number))

