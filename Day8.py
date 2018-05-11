import re
registers = {}
conditions = []
counter = 0
biggest = []

instructions = []
f = open("Day8.txt","r")

def replaceValue(c,i):
    instruction = re.match(r"([a-z]+)\s(inc|dec)\s([-0-9]+)", i, re.I)
    if instruction:
        reg = instruction.group(1)
        sum = instruction.group(2)
        amnt = int(instruction.group(3))
        if reg in registers:
            curr = registers.get(reg,"none")
            if sum == "inc":
                value = int(curr) + int(amnt)
            else:
                value = int(curr) - int(amnt)
            registers[reg] = value


def checkCondition(c,inst):
    match = re.match(r"([a-z]+)\s(<|>|==|!=|<=|>=)\s([-0-9]+)", c, re.I)
    if match:
        reg = match.group(1)
        comp = match.group(2)
        amnt = int(match.group(3))
        if reg in registers:
            curr = int(registers.get(reg,"none"))
            if comp == "==":
                if curr == amnt:
                    replaceValue(c,inst)
            if comp == ">":
                if curr > amnt:
                    replaceValue(c,inst)
            if comp == "<":
                if curr < amnt:
                    replaceValue(c,inst)
            if comp == "!=":
                if curr != amnt:
                    replaceValue(c,inst)
            if comp == "<=":
                if curr <= amnt:
                    replaceValue(c,inst)
            if comp == ">=":
                if curr >= amnt:
                    replaceValue(c,inst)

# Create the initial dictionary of registers
for line in f:
    line = line.strip("\n")
    match = re.match(r"(([a-z]+)\s(inc|dec)\s(-)?([0-9]+))\s(if)\s(([a-z]+)\s([>|<|!=|==|<=]+)\s(-)?([0-9]+))", line, re.I)
    if match:
        instruction = match.group(1)
        condition = match.group(7)
        registers[match.group(2)] = 0
    conditions.append(condition)
    instructions.append(instruction)


#for c in conditions:
#        chooseComp(c)

for i, inst in enumerate(instructions):
    match = re.match(r"([a-z]+)\s(inc|dec)\s(-)?([0-9]+)", inst, re.I)
    if match:
        reg = match.group(1)
        if reg in registers:
            c = conditions[i]
            checkCondition(c,inst)
    largest = max(registers, key=lambda i: registers[i])
    biggest.append(registers.get(largest,"none"))



largest = max(registers, key=lambda i: registers[i])
Day1 = registers.get(largest,"none")
print("day1:",Day1)
print("day2:",max(biggest))
