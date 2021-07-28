import numpy
with open("circuits") as instructions:
  raw = instructions.read().split("\n")

#Takes an input from the circuit and determines if its a constant or a circuit, as well as if that circuit has a value yet.
def determine(thing):
  if thing.isalpha():
    if thing in registers.keys():
      return numpy.uint16(registers[thing])
    else:
      return False
  else:
    return numpy.uint16(thing)

registers = {}
ptr = 0
while(raw):
  if ptr >= len(raw):
    ptr = 0
  op = raw[ptr].split(" ")

  #SIGNAL
  if len(op) == 3:
    source = determine(op[0])
    if source is not False:
      registers[op[2]] = source
      raw.pop(ptr)
    else: ptr += 1
  #NOT
  elif len(op) == 4:
    source = determine(op[1])
    if source is not False:
      registers[op[3]] = numpy.invert(source)
      raw.pop(ptr)
    else: ptr += 1
  #OR
  elif op[1] == "AND":
    source1 = determine(op[0])
    source2 = determine(op[2])
    if source1 is not False and source2 is not False:
      registers[op[4]] = numpy.bitwise_and(source1, source2)
      raw.pop(ptr)
    else: ptr += 1
  #AND
  elif op[1] == "OR":
    source1 = determine(op[0])
    source2 = determine(op[2])    
    if source1 is not False and source2 is not False:
      registers[op[4]] = numpy.bitwise_or(source1, source2)
      raw.pop(ptr)
    else: ptr += 1
  #LSHIFT
  elif op[1] == "LSHIFT":
    source = determine(op[0])
    if source is not False:
      registers[op[4]] = numpy.left_shift(source, int(op[2]))
      raw.pop(ptr)
    else: ptr += 1
  #RSHIFT
  elif op[1] == "RSHIFT":
    source = determine(op[0])
    if source is not False:
      registers[op[4]] = numpy.right_shift(source, int(op[2]))
      raw.pop(ptr)
    else: ptr += 1

print(registers['a'])