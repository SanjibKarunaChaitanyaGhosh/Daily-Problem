for i in range(1,10):
    for j in range(10-i):
        print("*",end=" ")
    print()

print("\n======================\n")

for i in range(1,10):
    for j in range(10-i,0,-2):
        print("*",end=" ")
    print()
    
print("\n========================\n")

for i in range (1,7):
    for j in range(i):
        print(" ", end=" ")

    for j in range(7-i):
        print("*", end=" ")

    print()