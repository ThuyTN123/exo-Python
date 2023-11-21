
n1 = int(input("Enter a number1: "))
if n1 < 0:
    print("Invalid number. Please input a valid number.")
else:
    gt = 1
    if n1 == 0 or n1 == 1:
        gt = 1
    else:
        for i in range(1, n1 + 1):
            gt *= i

    print(f"The factorial of {n1} is: {gt}")


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number2: "))
if n < 0:
    print("Invalid number. Please input a valid number.")
else:
    fac = factorial(n)

print(f"The factorial of {n} is: {fac}")


