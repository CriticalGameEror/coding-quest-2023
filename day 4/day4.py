with open("input.txt") as f:
    input = f.readlines()

text = {} # the corresponding text of the packets assigned by their packet number

for packet in input:
    packet = packet.strip()
    if packet[:4] != "5555":
        continue
    number = int(packet[12:14]) # the packet number
    checkSum = int(packet[14:16], base=16) # the check sum number
    
    # works out the total value of each byte in the payload
    total = 0
    for x in range(0, len(packet[16:]), 2):
        total += int(packet[16+x:18+x], base=16)

    # checks to see if the packet conforms with the check sum number
    if total % 256 != checkSum:
        continue

    text[number] = bytearray.fromhex(str(packet[16:])) # adds the message

# gets the text output from the sorted packets
output = ""
for x in range(len(text)):
    output += text[x].decode()
print(output)