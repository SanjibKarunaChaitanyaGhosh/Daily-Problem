for i in range(1,6):

    for j in range(i):
        print(j*"b",end=" ")

    for k in range(1,6-i):
        print("*",end=" ")

    print()


def ReversePyramid(n):

    for i in range(1,n):
        
        print(i*" ",end=" ")

        for k in range(1,n-i):
            print("*",end=" ")

        print()

n=int(input("Enter any number : "))
ReversePyramid(n)
