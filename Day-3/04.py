
n= int(input("Enter your number from 1 to 9 : "))

for i in range(1,n):

    for k in range(i):
        print("8", end=" ")
    
    for j in range((2*n-1)-2*i):  
        print("*",end=" ")

    print()
    
print("\n========================\n")