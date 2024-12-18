for x in range(1, 5):
    for y in range(x, 4):
        print(" ", end=" ")
    for z in range(1, x+1):
        print("*", end=" ")
    for a in range(1, x):
        print("*", end=" ")
    print()

for b in range(1, 6):
    for c in range(b):
        print("  ",end="")
    for e in range(4-b):
        print("*",end=" ")
    for j in range(3-b):
        print("*",end=" ")
    print()
