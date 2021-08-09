import re

with open("JSON") as json:
  rawdata = json.read()

#Part 1
data = re.split('{|}|:|,|\[|\]', rawdata)
total = 0
for item in data:
  try:
    total += int(item)
  except:
    pass
print(total)

#Part 2
ptr = 0
brackets = []
while True:
  if rawdata[ptr] == "{":
    brackets.append(ptr)
  elif rawdata[ptr] == "}":
    openBracket = brackets.pop()
    if ":\"red\"" in rawdata[openBracket:ptr]:
      rawdata = rawdata[:openBracket] + rawdata[ptr:]
      ptr = openBracket

  ptr += 1
  if ptr >= len(rawdata):
    break

data = re.split('{|}|:|,|\[|\]', rawdata)
total = 0
for item in data:
  try:
    total += int(item)
  except:
    pass
print(total)