import math

def main():
  bHP, bDmg, bArm = 100, 8, 2
  hp, dmg, arm = 100, 0, 0

  weapons = [8, 10, 25, 40, 74]
  armor = [0, 13, 31, 53, 75, 102]
  oneRing = [25, 50, 100]
  twoRings = [75, 125, 150]

  minCost = math.inf
  for i in range(len(weapons)):
    baseDmg = 4 + i
    atks0 = math.ceil(bHP / baseDmg - bArm)
    atks1 = [baseDmg + j for j in range(1,4)]
    atks2 = [baseDmg + j for j in range(3,6)]
    print(atks0)
    print(atks1)
    print(atks2)    

    #armorNeeded = int(bDmg - (100 / atksToKill)) + 1
    #minCost = min([minCost, armor[armorNeeded]])
    


main()