# 19. Simple calculator (add, sub, multi, div)
print("Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    Result=num1 + num2
    print("Result:", Result )
elif operation == '-':
    Result=num1 - num2
    print("Result:", Result)
elif operation == '*':
    Result=num1 * num2
    print("Result:", Result)
elif operation == '/':
    if num2 != 0:
        Result=num1 / num2
        print("Result:", Result)
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operation!")
print("Thank You")
