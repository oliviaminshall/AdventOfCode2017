file = open(r"C:\Users\OMINSHAL\OneDrive - Capgemini\CodeAdvent\Puzzle.txt","r")
digits = file.read()
answerone = 0
answertwo = 0
length = len(digits)
half = int(length/2)

#part 1
counter = 0
for i, digit in enumerate(digits):
    thiselem = digits[int(counter) % length]
    nextelem = digits[(int(counter) + 1) % length]
    if thiselem == nextelem:
        answerone = int(answerone) + int(thiselem)
    counter = int(counter) + 1
print(answerone)

#part 2
counter = 0
for i, digit in enumerate(digits):
    thiselem = digits[int(counter) % length]
    nextelem = digits[(int(counter) + half) % length]
    if thiselem == nextelem:
        answertwo = int(answertwo) + int(thiselem)
    counter = int(counter) + 1
print(answertwo)