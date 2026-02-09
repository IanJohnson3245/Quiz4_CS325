def div(a,b):
    if b == 0:
        return "Error"
    return a // b

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Result: ", div(num1, num2))