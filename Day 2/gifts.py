from math import prod

with open("gifts") as gifts:
  dimensions = [[int(x) for x in gift.split("x")] for gift in gifts.read().split("\n")]

paper = 0
ribbon = 0

for gift in dimensions:
  gift.sort()
  ribbon += 2 * (gift[0] + gift[1]) + prod(gift)
  giftDim = [gift[0] * gift[1], gift[2] * gift[1], gift[0] * gift[2]]
  giftDim.sort()
  paper += giftDim[0] + 2 * sum(giftDim)

print(paper)
print(ribbon)