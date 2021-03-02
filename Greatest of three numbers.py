def Greatest_three(x,y,z):
    if x>y and x>z:
        return x;
    elif y>x and y>z:
        return y;
    elif z>x and z>y:
        return z;
    else:
        return ("equal")

a,b,c = [int(x) for x in input().split()]
result= Greatest_three(a,b,c)
print(result)