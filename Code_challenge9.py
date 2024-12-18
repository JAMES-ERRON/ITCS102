for x in range(1, 11):
    print("  " * (x - 1), end="")
    for y in range(x, 11):
        print("*", end=" ")
    print()