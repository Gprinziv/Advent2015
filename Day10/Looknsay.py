def looknsay(phrase):
  newphrase = ""
  ptr = 0
  count = 0

  while ptr < (len(phrase) - 1):
    if count == 0:
      curNum = phrase[ptr]
      count = 1
    
    if phrase[ptr + 1] == phrase[ptr]:
      count += 1
    else:
      newphrase += str(count) + curNum
      count = 0
    ptr += 1

  if count == 0:
    newphrase += "1" + phrase[-1]
  else:
    newphrase += str(count) + curNum


  return newphrase

INPUT = "1113122113"
LEN = 40
LEN2 = 50
for i in range(LEN2):
  INPUT = looknsay(INPUT)

print(len(INPUT))