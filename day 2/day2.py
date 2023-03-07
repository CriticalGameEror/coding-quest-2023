with open("input.txt") as f:
    input = f.readlines()

numbers = [] # list of valid numbers

for line in input:
    binary = bin(int(line.strip()))[2:] # converts the number to binary and strips the first two characters
    
    # finds if there is an even number of 1s
    if len(str(binary).replace("0", "")) % 2 == 0:
        if len(binary) == 16:
            binary = binary[1:]
        numbers.append(int(binary, base=2))

# adds all the numbers
total = 0
for number in numbers:
    total += number

# finds the average (rounded to nearest int)
total = round(total/len(numbers))
print(total)