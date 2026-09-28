for i in range(1,5):
    print(5*" * ")

print("\n=================\n")

for i in range(1,5):
    for j in range (1,5):
        print("*", end=" ")
    print()

print("\n=================\n")

for i in range(1,5):

    for j in range (5):
        if i==1 or i==4:
            print("*", end=" ")

    print()

print("\n=================\n")

for i in range(1,5):

    for j in range (5):
        if j==1 or j==4:
            print("*", end=" ")
        else:
            print(" ",end=" ")

    print()

print("\n=================\n")

for i in range(1,5):

    for j in range (5):
        if i==1 or i==4 or j==1 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
          
    print()

print("\n=================\n")

for i in range(1,5):

    for j in range (1,5):
        if i==1 or i==4:
            print("*", end=" ")
        elif j==1 or j==4:
            print("*", end=" ")
        else:
            print(" ",end=" ")
        
    print()