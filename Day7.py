twrs = []
pns = []
ws = []
runday1 = False
wTotal = 0
day1 = ''
invalid = False

class Tower:
    def __init__(self, name, weight, towers):
        self.name = name
        self.towers = towers
        self.weight = int(weight)

class Weight:
    def __init__(self,pn,weight):
        self.pn = pn
        self.weight = int(weight)

def checkTower(twr):
    # if there are sub towers
    if len(twr.towers) > 0:
        # check to see if sub tower has any sub-towers
        for e in twr.towers:
            for i, t in enumerate(twrs):
                f = e.replace(",","")
                # find tower with the matching name
                if f == t.name:
                    # remove tower as it has now been checked
                    checkTower(twrs[i])
            twr.towers.remove(e)
    else:
        # no sub towers - remove program name from pn list
        for p in pns:
            if p == twr.name:
                pns.remove(p)

#day2 function
#def checkSubTower


def findInvalidTwr(twr,wTotal,pn):
    counter = 0
    # check subtowers all have same weight
    for e in twr.towers:
        f = e.replace(",","")
        # add the totals of the subweights
        for i, t in enumerate(twrs):
            if f == t.name:
                checkSubTower(t,t.weight)


def init():
    f = open("Day7.txt","r")
    for line in f:
        line = line.strip("\n").split(" ")
        # add to list of tower objects
        twr = Tower(line[0],line[1][1:-1],line[3:])
        twrs.append(twr)
        # create list of 'to check' progam names
        pns.append(line[0])

init()
# loop through each tower obj
while len(pns) > 1:
    for t in twrs:
        checkTower(t)
    if len(pns) == 1:
        print ("Day1:",pns)
        day1 = pns[0]

init()
for t in twrs:
    if t.name == day1:
        # set the towers weight
        wTotal = t.weight
        pn = t.name
        findInvalidTwr(t,wTotal,pn)
#print(ws)
for i, w in enumerate(ws):
    occ = ws.count(w)
    for t in twrs:
        if len(t.towers) == 0:
            twrs = [x for x in twrs if x != t]
    if occ == 1:
        name = t.name
        for i, n in enumerate(twrs):
            if n.name == name:
                wTotal = n.weight
        #        checkSubTower(twrs[i],wTotal)
    #    checkSubTower(t)

# create list of tower objs - done
# loop through list calling checkTower - done
# checkTower = if sub towers, call check towers
