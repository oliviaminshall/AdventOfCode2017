file = open(r"C:\Users\OMINSHAL\OneDrive - Capgemini\CodeAdvent\Puzzle.txt","r")
digits = file.read()
match = 0

length = len(digits)
half = int(length/2)

counter = 0
for i, digit in enumerate(digits):
    thiselem = digits[int(counter) % length]
    nextelem = digits[(int(counter)+1) % length]
    if thiselem == nextelem:
        match = int(match) + int(thiselem)
    counter = int(counter) + 1
print(match)

