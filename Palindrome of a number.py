def palindrome(number):
    temp=number
    reverse=0
    while(number>0):
        remainder=number%10
        reverse=(reverse*10) + remainder
        number=number//10
    if temp==reverse:
        return ("Palindrome");
    else:
        return ("not a palindrome")
number=int(input())
print(palindrome(number))

