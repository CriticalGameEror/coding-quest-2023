with open("input.txt") as f:
    input = f.readlines()

coords = set() # stores x and y in tuples

for line in input:
    line = line.strip().split()
    for y in range(int(line[1]), int(line[1]) + int(line[3])): # loops from the current Y cord to the height
        for x in range(int(line[0]), int(line[0])+int(line[2])): # loops for the current X cord to the width
            # if the cords are already in the set, then remove them
            if (x,y) in coords:
                coords.remove((x,y))
            # otherwise add it
            else:
                coords.add((x,y))

# loops for the size of the screen (50x10)
for y in range(10):
    for x in range(50):
        # if the coords are in the set then print a symbol
        if (x,y) in coords:
            print("#", end="")
        # otherwise print a space
        else:
            print(" ", end="")
    print()