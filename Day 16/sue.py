import re

with open("input") as f:
  theSue = {}
  for line in f.readlines():
    theSue[line.split(":")[0]] = int(line.split(":")[1])

for sue in open("sues").readlines():
  factors = re.split(",|:", sue.strip("\n"))
  flag = True
  for i in range(1, len(factors), 2):
    if factors[i][1:] in ("cats", "trees"):
      if int(factors[i+1][1:]) in range(0, theSue[factors[i][1:]] + 1):
        flag = False
    elif factors[i][1:] in ("pomeranians", "goldfish"):
      if int(factors[i+1][1:]) not in range(0, theSue[factors[i][1:]]):
        flag = False
    else:
      if theSue[factors[i][1:]] != int(factors[i+1][1:]):
        flag = False
  if flag == True:
    print(factors[0])