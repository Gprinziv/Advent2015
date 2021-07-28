with open("digilist") as digits:
  strings = digits.read().split("\n")

codeChars = 0
newCodeChars = 0
valueChars = 0
for item in strings:
  i = 0
  while i < len(item):
    if item[i] == "\"":
      codeChars += 1
      newCodeChars += 3
      i += 1
    elif item[i] == "\\":
      if item[i+1] == 'x':
        codeChars += 4
        newCodeChars += 5
        valueChars += 1
        i += 4
      else:
        codeChars += 2
        newCodeChars +=4
        valueChars += 1
        i += 2
    else:
      codeChars += 1
      newCodeChars += 1
      valueChars += 1
      i += 1

print("Charcters in code: " + str(codeChars))
print("Characters in string: " + str(valueChars))
print(codeChars - valueChars)
print("Characters in newly encoded string: " + str(newCodeChars))
print(newCodeChars - codeChars)