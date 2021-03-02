def greatest(x,y):
    if x>y:
        return x;
    elif x<y:
        return y;
    else:
        return ("equal")


a,b=[int(x) for x in input().split()]
result=greatest(a,b)
print(result)