def palindrome(input2):
    temp = input2[::-1]

    if temp == input2:
        print("palindrome")
    else:
        print("Not a palindrome")


input1 = input()
palindrome(input1)