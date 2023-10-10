import math

def divisors(n):
  for i in range(1, int(math.sqrt(n) + 1)):
    if n % i == 0:
      yield i
      yield int(n/i)

def divisors2(n):
  for i in range(1, int(math.sqrt(n) + 1)):
    if n % i == 0:
      if int(n/i) <= 50:
        yield i
      if i <= 50:
        yield int(n/i)

def main():
  goal = 36000000 / 10
  i = 0

  while True:
    if sum(set(divisors(i))) >= goal:
      print(f"found it at {i}!")
      return
    if i % 200000 == 0:
      print(i)
    i += 1

def main2():
  goal = 36000000
  i = 0

  while True:
    if sum(set(divisors2(i))) * 11 >= goal:
      print(f"found it at {i}!")
      return
    if i % 200000 == 0:
      print(i)
    i += 1

main2()