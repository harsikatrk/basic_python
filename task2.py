n1=int(input("Enter the starting value"))
n2=int(input("Enter the ending value"))
table=int(input("Enter the table"))

if n1<n2:
    for i in range(n1,n2+1):
        if(i%table==0):
            print(i)


