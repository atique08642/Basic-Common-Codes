def fibonaccirec(n):
    if n <= 1:
        return n
    else:
        return fibonaccirec(n - 1) + fibonaccirec(n - 2)


number = int(input())
print(fibonaccirec(number))


