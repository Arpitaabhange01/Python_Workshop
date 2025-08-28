# 3. Swap two numbers using a temporary variable
a = float(input("Enter first number to swap : "))
b = float(input("Enter second number: "))
print("Before swapping: a =", a, ", b =", b)
temp = a
a = b
b = temp
print("After swapping: a =", a, ", b =", b)
