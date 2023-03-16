# a non working solution with prims algorithm

with open("input.txt") as f:
    input = f.readlines()

distances = {}

for node in range(len(input)):
    nodeList = input[node].strip().split(" ")
    distances[node] = []
    for item in nodeList:
        distances[node].append(int(item))
    
tree = {} # contains the nodes currently in the tree and what they are connected to
total = 0

currentNode = 0
while len(tree) != len(distances):
    highest = [-1,-1]
    for node in range(len(distances[currentNode])):
        if distances[currentNode][node] < highest[1] or highest[0] == -1:
            if node not in tree and node != currentNode:
                highest = [node, distances[currentNode][node]]
    tree[currentNode] = highest[0]
    if highest[1] != -1:
        total += highest[1]
        currentNode = highest[0]


total += distances[currentNode][0]

print(tree)
print(total)