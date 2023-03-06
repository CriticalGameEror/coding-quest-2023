with open("input.txt") as f:
    input = f.readlines()

# seperates each entry into its own parts
for line in range(len(input)):
    input[line] = input[line].strip().split()

quantities = {} # contains the catagory of item and its respective quantity

# adds each quantity to the dictionary based on its category
for entry in input:
    if entry[2] in quantities:
        quantities[entry[2]] += int(entry[1])
    else:
        quantities[entry[2]] = int(entry[1])

# times the mod 100 of the quantities together to get the solution number
total = 1
for thing in quantities.values():
    total *= thing % 100

print(total)