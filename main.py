import re

with open("input") as f:
  theSue = {}
  for line in f.readlines():
    theSue[line.split(":")[0]] = int(line.split(":")[1])
  
for sue in open("sues").readlines():
  factors = re.split(",|:", sue.strip("\n"))
  flag = True
  print(factors[0])
  for i in range(1, len(factors), 2):
    print(f"{factors[i]}: {factors[i+1][1:]} (expected: {theSue[factors[i][1:]]})")
    if theSue[factors[i][1:]] != factors[i+1][1:]:
      print("false!")
      flag = False
    if flag == True:
      print(factors[0])