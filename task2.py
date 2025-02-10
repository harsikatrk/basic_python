n1    =int(input("Enter the starting value : ")) #to enter the starting value
n2    =int(input("Enter the ending value   : ")) #to enter the ending value
table =int(input("Enter the table          : ")) #to enter the table

if n1<n2:
    for i in range(n1,n2+1):  
        if(i%table==0): #main condition which divides if 0 returns the number else moves to next number
            print(i)  #to print the number


