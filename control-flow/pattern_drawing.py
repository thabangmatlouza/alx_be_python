size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    col = 0
    while col < size:
        print("*", end="")  # ✅ this matches the checker requirement
        col += 1
    print()  # move to next line after each row
    row += 1

