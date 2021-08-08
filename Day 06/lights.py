import numpy

with open ("lights") as lightInst:
  raw = lightInst.read().split("\n")
  insts = []
  for inst in raw:
    inst = inst.split(" ")
    insts.append([len(inst[-4]), int(inst[-3].split(",")[0]), int(inst[-1].split(",")[0]), int(inst[-3].split(",")[1]), int(inst[-1].split(",")[1])])


"""Part 1
blah = numpy.full([1000,1000], False)

for inst in insts:
  mask = numpy.full([inst[2] - inst[1] + 1, inst[4] - inst[3] + 1], False)
  print(numpy.logical_not(numpy.logical_or(blah[inst[1]:inst[2]+1, inst[3]:inst[4]+1], mask)))

  if inst[0] == 2:
    blah[inst[1]:inst[2]+1, inst[3]:inst[4]+1] = numpy.logical_not(mask)
    pass
  elif inst[0] == 3:
    #slice = mask
    blah[inst[1]:inst[2]+1, inst[3]:inst[4]+1] = mask
  else:
    #slice = NOR mask
    blah[inst[1]:inst[2]+1, inst[3]:inst[4]+1] = numpy.logical_not(numpy.logical_or(blah[inst[1]:inst[2]+1, inst[3]:inst[4]+1], mask))

print(numpy.count_nonzero(blah))
"""

"""Part 2"""
lights = numpy.full([1000,1000], 0, dtype=int)

for inst in insts:
  if inst[0] == 2:
    lights[inst[1]:inst[2]+1, inst[3]:inst[4]+1] += 1
  elif inst[0] == 3:
    lights[inst[1]:inst[2]+1, inst[3]:inst[4]+1] = numpy.where(lights[inst[1]:inst[2]+1, inst[3]:inst[4]+1] - 1 > 0, lights[inst[1]:inst[2]+1, inst[3]:inst[4]+1] - 1, 0)
  else:
    lights[inst[1]:inst[2]+1, inst[3]:inst[4]+1] += 2

print(numpy.sum(lights))