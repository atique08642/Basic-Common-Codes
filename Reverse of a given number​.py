def reverse_of_Number(number):
    temp=number
    reverse=0
    while(number>0):
        remainder=number%10
        reverse=(reverse*10) + remainder
        number=number//10
    return reverse;
number=int(input())
print(reverse_of_Number(number))

