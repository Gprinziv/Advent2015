def passgen(password):
  newpass = [ord(char) for char in oldpass]

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

  if newpass[3] < newpass[4]:
    newpass[3] += 1
  elif newpass[3] == newpass[4]:
    if (newpass[4] + 1) < newpass[5]:
      newpass[3] += 1
    elif (newpass[4] + 1) == newpass[5]:
      if (newpass[5] + 1) < newpass[6]:
        newpass[3] += 1
      elif (newpass[5] + 1) == newpass[6]:
        if newpass[6] <= newpass[7]:
          newpass[3] += 1
  if chr(newpass[3]) in "ghijklmno":
    newpass = newpass[:3] + [97, 97, 98, 99, 99]
  elif chr(newpass[3]) in "yz":
    newpass[2] += 1
    newpass = newpass[:3] + [97, 97, 98, 99, 99]

  newpass[4] = newpass[3]
  newpass[5] = newpass[3] + 1
  newpass[6] = newpass[3] + 2
  newpass[7] = newpass[3] + 2
  print(newpass)
  
  return "".join((chr(number) for number in newpass))  

#Also consider cases where one condition is met early:
  #If already one match, optimal tail configuration would be #####1123
  #If two match, optimal tail configuration would be ######123
  #If straight
    #If no match1 by digit 5, optimal tail configuration would be, #####11aa
    #If one match, optimal tail configuration is ######11  

oldpass = "cqjxjnds"
newpass = passgen(oldpass)

print(newpass)