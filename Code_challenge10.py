for x in range(1, 6):
    for y in range(x, 6):
        print(" ", end=" ")
    for z in range(1, x + 1):
        print("*",end=" ")
    for a in range(1, x + 1):
        print("*", end=" ")
    print()
for b in range(1, 6):
    for c in range(1, b + 1):
        print(" ", end=" ")
    for d in range(6, b, -1):
        print("^",end=" ")
    for e in range(6, b, -1):
        print("^", end=" ")
    print()
