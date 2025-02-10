
num1=int(input("Enter first number   :")) #to enter first number
num2=int(input("Enter second number :")) #to enter second number
value=input("Enter any operation +, -, *, /, % :")  # to enter the necessary operator

result=0  #initialize result to zero

if value == '+' :
    result=num1+num2  #addition 
    print("Addition of {}and {} is".format(num1,num2),result) #to print the result in desired form
elif value == '-':
    result=num1-num2 #subtraction
    print("Subtraction of {}and {} is".format(num1,num2),result) #to print the result in desired form
elif value == '*':
    result=num1*num2 #multiplication
    print("Multiplication of {}and {} is".format(num1,num2),result) #to print the result in desired form
elif value == '/':
    result = num1/num2 #division
    print("Division of {}and {} is".format(num1,num2),result) #to print the result in desired form
elif value =='%':
    result = num1%num2 #modulus
    print("Modulus of {}and {} is".format(num1,num2),result) #to print the result in desired form
else:
    print("no such operation!!!") #to print the result in desired form

