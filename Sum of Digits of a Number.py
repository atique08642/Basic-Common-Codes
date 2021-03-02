def Sum_of_Digits(number):
    temp=number
    sum=0
    while(number>0):
        remainder=number%10
        sum=sum+remainder
        number=number//10
    return sum;
number=int(input())
print(Sum_of_Digits(number))

