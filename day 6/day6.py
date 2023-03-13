with open("input.txt") as f:
    input = f.readlines()

positions = set() # contains the positions of the asteroids (in the form x,y)

for asteroid in input:
    asteroid = asteroid.strip().split(" ")
    
    xCord = float(asteroid[0])
    yCord = float(asteroid[1])
    speedX = float(asteroid[2])
    speedY = float(asteroid[3])

    # finds the position of the asteroid when the ship arrives
    xCord = xCord + (speedX * 3600)
    yCord = yCord + (speedY * 3600)

    positions.add((int(xCord), int(yCord)))
    
    # calculates the tragectory of the asteroids over the 60 seconds
    for second in range(59):
        xCord += speedX
        yCord += speedY
        positions.add((int(xCord), int(yCord)))

# finds the one position in the 100x100 grid which hasn't had an asteroid hit
for y in range(99):
    for x in range(99):
        if (x,y) not in positions:
            print(x, y)
            exit()