inp = [[3,-3,-1,0], [0,3,0,0], [0,0,4,-2], [-3,0,0,2], [2,9,1,8]]

max1 = 0
max2 = 0
for i in range(100):
  for j in range(100-i):
    for k in range(100-i-j):
      l = 100-i-j-k
      capacity = max([0, inp[0][0]*i + inp[0][1]*j + inp[0][2]*k + inp[0][3]*l])
      durability = max([0, inp[1][0]*i + inp[1][1]*j + inp[1][2]*k + inp[1][3]*l])
      flavor = max([0, inp[2][0]*i + inp[2][1]*j + inp[2][2]*k + inp[2][3]*l])
      texture = max([0, inp[3][0]*i + inp[3][1]*j + inp[3][2]*k + inp[3][3]*l])
      calories = max([0, inp[4][0]*i + inp[4][1]*j + inp[4][2]*k + inp[4][3]*l])
      score = capacity * durability * flavor * texture

      max1 = score if score > max1 else max1
      max2 = score if calories == 500 and score > max2 else max2
print(max1)
print(max2)