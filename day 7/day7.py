with open("input.txt") as f:
    input = f.readlines()

bounds = 20 # the size of the board

# sets the fruit spawns
fruitSpawn = input[1].strip().split(" ")
for x in range(len(fruitSpawn)):
    fruitSpawn[x] = fruitSpawn[x].split(",")
    fruitSpawn[x] = (int(fruitSpawn[x][0]), int(fruitSpawn[x][1]))

# sets the moves
moves = input[3].strip()

positions = [(0,0)] # the positions of the snake, the first index is always the head
points = 0
currentFruit = fruitSpawn.pop(0) # the first position of the fruit

# goes through each move
for move in moves:
    positions.append((0,0)) # placeholder position for a new part if it is needed
    
    # moves each part of the worm to its new position (except the head)
    for x in range(len(positions)-1, 0, -1):
        positions[x] = positions[x-1]
    
    # moves the head
    if move == "U":
        positions[0] = (positions[0][0], positions[0][1]-1)
    elif move == "D":
        positions[0] = (positions[0][0], positions[0][1]+1)
    elif move == "L":
        positions[0] = (positions[0][0]-1, positions[0][1])
    elif move == "R":
        positions[0] = (positions[0][0]+1, positions[0][1])
    
    # if it is out of bounds or collided with itself
    if positions[0][0] == bounds or positions[0][0] == -1:
        break
    if positions[0][1] == bounds or positions[0][1] == -1:
        break
    if positions[0] in positions[1:]:
        break

    if positions[0] == currentFruit:
        # adds the points and gets the next position of the fruit
        points += 100
        currentFruit = fruitSpawn.pop(0)
    else:
        positions.pop(-1) # removes the new part that would have been generated if no fruit is touched

    points += 1 # adds a point for a successful move

print(points)