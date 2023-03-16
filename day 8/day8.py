with open("input.txt") as f:
    input = f.readlines()

distances = {}

for node in range(len(input)):
    nodeList = input[node].strip().split(" ")
    distances[node] = []
    for item in nodeList:
        distances[node].append(int(item))

def recursion(currentDistance, currentNode, nextNode, visited):
    currentDistance += distances[currentNode][nextNode]
    visited += 1
    if visited == len(distances)-1:
        return (currentDistance + distances[nextNode][0])
    else:
        distance = -1
        for x in range(1, len(distances)):
            temp = recursion(currentDistance, nextNode, x, visited)
            if distance == -1 or temp < distance:
                distance = temp
        return distance



shortestDistance = -1
for x in range(1, len(distances)):
    temp = recursion(0, 0, x, 0)
    if shortestDistance == -1 or temp < shortestDistance:
        shortestDistance = temp

print(shortestDistance)


