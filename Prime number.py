def prime(number):
    for i in range(2, number // 2):
        if number % i == 0:
            return ("not a prime no.")
    else:
        return ("prime no.")


number = int(input())
print(prime(number))
