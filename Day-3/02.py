for i in range(1,10,2): # i=5

    for j in range(i):       # j=0,1,2,3,4
        print("*", end=" ")

    for k in range(10,0,-2): # 10,8,6,4,2
            print("8", end=" ")

    print()

print("\n=============================\n")

for i in range(1,10,2): # i=1,2

    for j in range(i):
        print("*", end=" ")

    for k in range(10-i,0,-2): # k=7,5,3,1
            print("8", end=" ")

    print()

print("\n=============================\n")

for i in range(1,10,2): # i=1,2

    for k in range(10-i,0,-2): # k=7,5,3,1
            print("8", end=" ")

    for j in range(i):
            print("*", end=" ")

    print()

print("\n=============================\n")

for i in range(1,10,2): # i=1,2

    for k in range(10-i,0,-2): # k=7,5,3,1
            print(" ", end=" ")

    for j in range(i):
            print("*", end=" ")

    print()