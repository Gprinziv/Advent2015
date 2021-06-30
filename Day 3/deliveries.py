with open("directions") as directions:
  dirs = directions.read()

cur = [0,0]
cur2 = [0,0]
step = 1
directions = {"<": (0,-1), ">": (0,1), "v": (1,1), "^": (1,-1)}
visited = {(0,0): 1}

for direction in dirs:
  coord, val = directions[direction]
  if step % 2 == 0:
    cur[coord] += val
    c = tuple(cur)
  else:
    cur2[coord] += val
    c = tuple(cur2)

  if c not in visited:
    visited[c] = 1
  else:
    visited[c] += 1
  
  step += 1

print(len(visited))