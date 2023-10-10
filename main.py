#make single replacements and count the number of unique answers.
def main():
  with open("input") as f:
    lines = [line.strip().split(" => ") for line in f.readlines()]
    replacements, molecule = lines[:-2], lines[-1][0]  

  newMoles = set()
  for replacement in replacements:
    i = 0
    while i < len(molecule):
      if replacement[0] == molecule[i:i+len(replacement[0])]:
        tempMole = molecule[:i] + replacement[1] + molecule[i+len(replacement[0]):]
        newMoles.add(tempMole)
      i += 1
  print(len(newMoles))

#Start at "e" and attempt to make the requisite string. OR start with the replacement string and attempt to reduce to "e".
def main2():
  with open("input") as f:
    lines = [line.strip().split(" => ") for line in f.readlines()]
    replacements = {}
    for val, key in lines[:-2]:
      replacements[key] = val
    count, molecule = 0, lines[-1][0]

    #This method has pitfalls. Need to be more intelligent. MNaybe split the string into a list to make it easier to index first.  
    #Find an Ar token, work backward until you see Rn, then go back once more and replace.
    i = 0
    while i < len(molecule):
      if molecule[i] == "A":
        j = i
        while molecule[j:j+2] != "Rn":
          print(molecule[j:j+2])
          j -= 1
        if molecule[j-1].islower():
          j-=2
        else:
          j-=1
        molecule = molecule[:j] + replacements[molecule[j:i+2]] + molecule[i+2:]
        count += 1
        print(molecule)
      i += 1

    """while len(molecule) > 1:
      for replacement in replacements:
        i = 0
        while i < len(molecule):
          if replacement[1] == molecule[i:i+len(replacement[1])]:
            molecule = molecule[:i] + replacement[0] + molecule[i+len(replacement[1]):]
            count += 1
            print(molecule)
          i += 1"""


main()
main2()