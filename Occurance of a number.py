def occurance (num,target):
    li = list(num)
    counter = 0
    for element in li:
        if element == target:
            counter += 1
    print(counter)


num = input()
target = input()
occurance(num,target)
