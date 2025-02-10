n1=int(input("Enter first number  : ")) #to enter first number
n2=int(input("Enter second number : ")) #to enter second number
n3=int(input("Enter table: ")) #to enter the table
def my_Func(n1,n2,n3):  #function
    for i in range(n1,n2+1):
        if(i%n3==0):  #main condition which divides if 0 returns the number else moves to next number
            print(i)  #to print the number
my_Func(n1,n2,n3) #call the function