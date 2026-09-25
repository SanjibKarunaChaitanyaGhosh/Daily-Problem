for i in range(1,6):

    for j in range(i):
        print(j*"b",end=" ")

    for k in range(1,6-i):
        print("*",end=" ")

    print()


for i in range(1,6):
    
    print(i*"b",end=" ")

    for k in range(1,6-i):
        print("*",end=" ")

    print()
