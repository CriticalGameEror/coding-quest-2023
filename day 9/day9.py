with open("input.txt") as f:
    input = f.readlines()

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

# sets the root node
first = input.pop(0)
root = Node(int(first, base=16))

maxHeight = 0
maxWidth = {} # stores each width as a layer and the number of nodes on that layer

# goes through each node in the input (except the first one)
for node in input:
    currentNode = root
    layer = 1 # the starting layer of the tree
    while True:
        if int(node, base=16) >= currentNode.value:
            if currentNode.right != None:
                currentNode = currentNode.right
                layer += 1
            else:
                currentNode.right = Node(int(node, base=16))
                # adds to the width of the current layer
                if layer in maxWidth:
                    maxWidth[layer] += 1
                else:
                    maxWidth[layer] = 1 
                break
        else:
            if currentNode.left != None:
                currentNode = currentNode.left
                layer += 1
            else:
                currentNode.left = Node(int(node, base=16))
                # adds to the width of the current layer
                if layer in maxWidth:
                    maxWidth[layer] += 1
                else:
                    maxWidth[layer] = 1 
                break
    # adds 1 to the current height as to include the node that was just added
    if layer+1 > maxHeight:
        maxHeight = layer+1

print(sorted(maxWidth.values())[-1] * maxHeight)