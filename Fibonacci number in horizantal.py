limit = int(input())
firstNumber = 0
secondNumber = 1
for i in range (0,limit):
    temp = firstNumber + secondNumber
    firstNumber = secondNumber
    secondNumber = temp
    if firstNumber == secondNumber:
        print('0', secondNumber, temp, end=' ')
    else:
        print(temp,end=" ")