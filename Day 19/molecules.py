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

#Start at "e" and attempt to make the requisite string. OR start with the replacement string and attempt to reduce to "e". There needs to be some sort of math.
#See how the actual replacements function.
def main2():
  with open("input") as f:
    lines = [line.strip().split(" => ") for line in f.readlines()]
    replacements = {}
    for val, key in lines[:-2]:
      replacements[key] = val
    count, molecule = 0, lines[-1][0]

main()
main2()