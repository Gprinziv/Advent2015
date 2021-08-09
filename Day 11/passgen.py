import time

def passgen(password):
  newpass = [ord(char) for char in oldpass]

  ptr = 0
  while ptr < len(newpass):
    if chr(newpass[ptr]) in "ilo":
      newpass[ptr] += 1
      newpass = newpass[:ptr + 1] + [97] * (len(newpass) - ptr - 1)
      break
    ptr += 1
    
  if newpass[-5] < newpass[-4]:
    newpass[-5] += 1
  elif newpass[-5] == newpass[-4]:
    if (newpass[-4] + 1) < newpass[-3]:
      newpass[-5] += 1
    elif (newpass[-4] + 1) == newpass[-3]:
      if (newpass[-3] + 1) < newpass[-2]:
        newpass[-5] += 1
      elif (newpass[-3] + 1) == newpass[-2]:
        if newpass[-2] <= newpass[-1]:
          newpass[-5] += 1
  if chr(newpass[-5]) in "ghijklmno":
    newpass = newpass[:3] + [97, 97, 98, 99, 99]
  elif chr(newpass[-5]) in "yz":
    newpass[-6] += 1
    newpass = newpass[:-5] + [97, 97, 98, 99, 99]

  newpass = newpass[:-4] + [newpass[-5], newpass[-5] + 1, newpass[-5] + 2, newpass[-5] + 2]
  print(newpass)
  
  return "".join((chr(number) for number in newpass))  

#Also consider cases where one condition is met early:
  #If already one match, optimal tail configuration would be #####1123
  #If two match, optimal tail configuration would be ######123
  #If straight
    #If no match1 by digit 5, optimal tail configuration would be, #####11aa
    #If one match, optimal tail configuration is ######11  

oldpass = "cqjxjnds"
starttime = time.time()
newpass = passgen(oldpass)
endtime = time.time()

print(newpass)
print(endtime - starttime)