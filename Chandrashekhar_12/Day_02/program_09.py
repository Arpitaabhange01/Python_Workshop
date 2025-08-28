#simple calculator
a=int(input("select\n 1.+\n 2.-\n 3.*\n 4./\n 5.none\n"))
if a==5:
    print("Thank You")

num1=float(input("Enter the first number:\n"))
num2=float(input("Enter the second number:\n "))

if a==1: 
    num=num1+num2
    print(num1,"+",num2,"=",num)
if a==2:
    num=num1-num2
    print(num1,"-",num2,"=",num) 

if a==3:
    num=num1*num2
    print(num1,"*",num2,"=",num)
if a==4:
    num=num1/num2
    print(num1,"/",num2,"=",num)
