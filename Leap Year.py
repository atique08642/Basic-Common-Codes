def LeapYear(year):
    if (year%4==0 and year%100!=0 or year%400==0):
        return True;
year=int(input())
if (LeapYear(year)==True):
    print("leap year")
else:
    print("not a leap year")