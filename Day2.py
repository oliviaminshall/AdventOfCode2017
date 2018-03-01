file = open(r"C:\Users\OMINSHAL\OneDrive - Capgemini\CodeAdvent\Day2.txt","r")
input = file.read()
rows = input.split('\n')

#part 1
diff = 0
for row in rows:
    row = row.split('\t')
    split = [int(x) for x in row]
    s = min(split)
    b = max(split)
    diff = diff + (b - s)
print(diff)

#part 2
total = 0
for row in rows:
    row = row.split('\t')
    split = [int(x) for x in row]
    for item in split:
        for check in split:
            if check != item:
                if (check % item == 0):
                    total = total + (check / item)
print(total)