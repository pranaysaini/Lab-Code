try:
    a = int(input("Enter the number : "))
    print(a/20)
    print(a/0)

except (ArithmeticError, ValueError) :
    print("An error Occoured\n")
