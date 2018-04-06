# for each passphrase, for each word, check against each other word

f = open("Day4.txt","r")
counter = 0

for line in f:
    d = []
    line = line.strip("\n")
    words = line.split(" ")
    for word in words:
        b = sorted(word)
        c = ''.join(b)
        d.append(c)
    un = list(set(d))
    if(len(un) == len(words)):
        counter = counter + 1
print(counter)
