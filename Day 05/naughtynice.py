with open ("naughtynice") as nnstrings:
  strings = nnstrings.read().split("\n")

VOWELS = ["a", "e", "i", "o", "u"]
BAD_STRINGS = ["ab", "cd", "pq", "xy"]

def isnice(nnstring):
  for x in BAD_STRINGS:
    if x in nnstring:
      return False

  repeatFlag = False
  vcount = 0

  for i in range(len(nnstring) - 1):
    if nnstring[i] in VOWELS:
      vcount += 1
    if nnstring[i] == nnstring[i + 1]:
      repeatFlag = True
  if nnstring[-1] in VOWELS:
    vcount += 1
  return repeatFlag and vcount >= 3

def isnice2(nnstring):
  gapFlag = False
  repeatFlag = False

  for i in range(len(nnstring) - 2):
    if not repeatFlag and nnstring.count(nnstring[i:i+2]) >= 2:
      repeatFlag = True
    if not gapFlag and nnstring[i] == nnstring[i+2]:
      gapFlag = True

  return repeatFlag and gapFlag

totalNice = 0
for nnstring in strings:
  if isnice2(nnstring):
    totalNice += 1
print(totalNice)