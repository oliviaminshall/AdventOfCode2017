f = open(r"Day5.txt","r")
input = f.read()
numbers = input.split("\n")
instruction = 0
i = 0
poistion = 0
counter = 0
while(i < len(numbers)):
    # get current instruction
    instruction = numbers[i]
    # increment current instruction by 1
    numbers[i] = int(instruction) + 1
    counter = counter + 1
    # follow instruction
    i = i + int(instruction)
print(counter)

# PART TWO

f = open(r"Day5.txt","r")
input = f.read()
numbers = input.split("\n")
instruction = 0
i = 0
poistion = 0
counter = 0
while(i < len(numbers)):
    # get current instruction
    instruction = numbers[i]
    # increment/decrease current instruction by 1
    if (int(instruction) < 3):
        numbers[i] = int(instruction) + 1
    else:
        numbers[i] = int(instruction) - 1
    counter = counter + 1
    # follow instruction
    i = i + int(instruction)
print(counter)
