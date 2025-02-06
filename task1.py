
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
result=0

value=input("enter any operation +, -, *, /, % :")

if value == '+' :
    result=num1+num2
    print("Addition of {}and {} is".format(num1,num2),result)
elif value == '-':
    result=num1-num2
    print("Subtraction of {}and {} is".format(num1,num2),result)
elif value == '*':
    result=num1*num2
    print("Multiplication of {}and {} is".format(num1,num2),result)
elif value == '/':
    result = num1/num2
    print("Division of {}and {} is".format(num1,num2),result)
elif value =='%':
    result = num1%num2
    print("Modulus of {}and {} is".format(num1,num2),result)
else:
    print("no such operation!!!")

