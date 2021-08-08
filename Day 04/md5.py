import hashlib

hashStr = "iwrupvqb"
hashNum = 0

#I am not an elegant human being.
while True:
  curHash = hashlib.md5((hashStr + str(hashNum)).encode())
  if curHash.hexdigest()[:6] == "000000":
    break
  else:
    hashNum += 1
  if hashNum % 100000 == 0:
    print(hashNum)

print(hashNum)