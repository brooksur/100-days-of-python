def prime_checker(number):
    for n in range(2, number):
        if (number % n == 0):
            return print("It's not a prime number.")

    return print("It's a prime number.")


n = int(input())
prime_checker(number=n)
