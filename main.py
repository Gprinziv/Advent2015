def findpass(password):
  newpass = [ord(char) for char in oldpass]
  #notValid = True

  #First pass: Check if any given inputs contain a forbidden letter. If they do, increment that letter and set remaining letters to "a". If you get to the end, increment everything by 1.
  ptr = 0
  while ptr < len(newpass):
    if newpass[ptr] in (ord("i"), ord("l"), ord("o")):
      newpass[ptr] += 1
      ptr += 1
      while ptr < len(newpass):
        newpass[ptr] = ord("a")
        ptr += 1
      break
    ptr += 1

  #If password digit 5 is less than password digit 4 and digit 4 is not g-o, y, or z, [4 = 5 = 6 - 1 = 7 - 2 = 8 - 2]
  #Else if it's the same, check down the line to make sure that the rest is ok
  #Else increment 4, then recheck from the top.

#Also consider for digits 1-4
  #If one match
  #If two match
  #If straight
  #If nothing



  """"
  while(notValid):
    ptr = -1
    while(ptr < 0):
      if newpass[ptr] == ord("z"):
        newpass[ptr] = ord("a")
        ptr -= 1
      elif newpass[ptr] in (ord("h"), ord("n"), ord("k")):
        newpass[ptr] += 2
        ptr = 0
      else:
        newpass[ptr] += 1
        ptr = 0
    #print("".join((chr(number) for number in newpass)))


    repeatCount = 0
    oneStraight = False
    while(ptr < len(newpass) - 1):
      if newpass[ptr] == newpass[ptr+1]:
        repeatCount += 1
        ptr += 1
      elif ptr + 2 < len(newpass):
        if newpass[ptr] == newpass[ptr+1] - 1 and newpass[ptr] == newpass[ptr+2] -2:
          oneStraight = True
      ptr += 1

    notValid = repeatCount < 2 or oneStraight == False

  newpass = [chr(number) for number in newpass]
  """
  return "".join((chr(number) for number in newpass))


oldpass = "cqjxjnds"
oldpass = "ocjppqrr"
newpass = findpass(oldpass)

print(newpass)

#I had an epiphany. The most compact successful password is one that goes "11233" Therefore, the first three characters only matter if they *already* fail/satisfy another condition