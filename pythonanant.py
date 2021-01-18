def multiplyTwoNumbers(x, y):
    c = int(x) * int(y)
    return c


def addTwoNumbers(x, y):
    c = int(x) + int(y)
    return c


if __name__ == "__main__":
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    c = multiplyTwoNumbers(a, b)
    print(c)

    a = input("Enter first number: ")
    b = input("Enter second number: ")
    c = addTwoNumbers(a, b)
    print(c)
