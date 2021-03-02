def ArmstronInRange(lower, upper):
    for num in range(lower, upper + 1):
        order = len(str(num))
        sumnew = 0
        temp = num
        while temp > 0:
            remainder = temp % 10
            sumnew = sumnew + remainder ** order
            temp = temp // 10
        if sumnew == num:
            print(num)


lower, upper = [int(x) for x in input().split()]
ArmstronInRange(lower, upper)
