for i in range(1,10):
    print(i,"*")

print("\n=====================\n")

for i in range(1,10):
    print(i*"*")

print("\n=====================\n")

for i in range(1,5):
    for i in range(i):
        print("*", end=" ")
    for j in range(5):
        print("8", end=" ")
    print()

print("\n=====================\n")

for i in range(1,5):
    for k in range(i):
        print("*", end=" ")
    for j in range(5-i):
        print("8", end=" ")
    print()

print("\n=====================\n")

for i in range(0,5):
    for k in range(i):
        print("*", end=" ")
    for j in range(5-i):
        print("8", end=" ")
    print()

print("\n=====================\n")

for i in range(0,5):
    for k in range(i):
        print(" ", end=" ")
    for j in range(5-i):
        print("8", end=" ")
    print()