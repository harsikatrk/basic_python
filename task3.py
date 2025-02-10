ch = "yes"
while ch.lower() == "yes":
   print("Select operation\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Modulus") #to display the options
   choice = input("Enter choice(1/2/3/4/5):") #to enter the choice
   num1 = int(input("Enter first number  : ")) #to enter the first number
   num2 = int(input("Enter second number : ")) #to enter the second number

   if choice == '1':
      print(num1,"+",num2,"=", (num1 + num2)) #to print the addition operator
   elif choice == '2':
      print(num1,"-",num2,"=", (num1 - num2)) #to print the subtraction operator
   elif choice == '3':
      print(num1,"*",num2,"=", (num1 * num2)) #to print the multiplication operator
   elif choice == '4':
      print(num1,"/",num2,"=", (num1 / num2)) #to print the division operator
   elif choice == '5':
      print(num1,"%",num2,"=", (num1 % num2)) #to print the modulous operator
   else:
      print("Invalid input")
   ch = input("Continue? yes/no:")

   if ch== "no":
      break