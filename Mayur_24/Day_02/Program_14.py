# 14. Swap two numbers without using a variable
x = float(input("Enter first number to swap: "))
y = float(input("Enter second number: "))
print("Before swapping: x =", x, ", y =", y)
x, y = y, x
print("After swapping: x =", x, ", y =", y)
