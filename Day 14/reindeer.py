def part1():
  runTime = 2503

  with open("input") as f:
    rds = []
    for line in f.readlines():
      deer_raw = line.split()
      deer = [int(deer_raw[3]), int(deer_raw[6]), int(deer_raw[13])]
      rds.append(deer)

  for deer in rds:
    runs, remain = runTime // (deer[1] + deer[2]), runTime % (deer[1] + deer[2])
    if remain > deer[1]:
      distance = (runs + 1) * deer[1] * deer[0]
    else:
      distance = (runs * deer[1] + remain) * deer[0]
    print(distance)
  print (rds)

part1()

def part2():
  runTime=1000

  with open("input") as f:
    rds = []
    for line in f.readlines():
      deer_raw = line.split()
      deer = [int(deer_raw[3]), int(deer_raw[6]), int(deer_raw[13])]
      rds.append(deer)

  scores = []
  distances = []

  for deer in rds:
     

  #Rate, 