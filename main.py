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
#Currently need to handle red inside lists inside objects. It's still removing things it shouldn't be, apparently.
ptr = 0
brackets = []
lists = [0]
while True:
  if rawdata[ptr] == '[':
    lists.append(ptr)
  elif rawdata[ptr] == "]":
    lists.pop()
  elif rawdata[ptr] == "{":
    brackets.append(ptr)
  elif rawdata[ptr] == "}":
    openBracket = brackets.pop()
    if "\"red\"" in rawdata[openBracket:ptr] and openBracket > lists[-1]:
      rawdata = rawdata[:openBracket] + rawdata[ptr + 1:]
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