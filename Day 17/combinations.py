import itertools

with open("input") as f:
    containers = [int(x) for x in f.readlines()]
liters = 150

combos = 0
for i in range(len(containers)):
    combo = list(itertools.combinations(containers, i))
    breakFlag = False #part 2
    for item in combo:
        if sum(item) == liters:
            combos += 1
            breakFlag = True
    if breakFlag == True: #part 2
        break
print(combos)