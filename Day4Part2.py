# for each passphrase, for each word, check against each other word

f = open("Day4.txt","r")

counter = 0

for line in f:
    line = line.strip("\n")
    words = line.split(" ")
    un = list(set(words))
    for word in words:
        c = ''.join(sorted(word))
        words.remove(word)
        words.append(c)
    un = list(set(words))
    if(len(un) != len(words)):
        counter = counter + 1
print(counter)
