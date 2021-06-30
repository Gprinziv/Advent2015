with open("floors") as floors:
  elevator = floors.read()

curFloor = 0
instCount = 0

for button in elevator:
  if button == "(":
    curFloor += 1
    instCount += 1
  else:
    curFloor += -1
    instCount += 1
  if curFloor == -1:
    print(instCount)

print(curFloor)
print(instCount)