# after this we'll do 'asteroids' or 'heat shields'

# create a 2D list
width = 10
height = 8

stuff = [["."]*width for _ in range(height)]

# print the whole thing (not pretty)
print(stuff)

# print one row at a time
for row in stuff:
    print(row)


# print each item
for row in stuff:
    for item in row:
        print(item, end="")
    print()


# access using indexed loops
for row in range(height):
    for col in range(width):
        print(stuff[row][col], end="")
    print()
