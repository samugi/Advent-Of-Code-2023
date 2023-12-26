import sys
sys.setrecursionlimit(3500) 

def energize(matrix, from_x, from_y, to_x, to_y, visited={}):
  if to_x < 0 or to_x >= len(matrix[0]) or to_y < 0 or to_y >= len(matrix):
    return 0

  visit = 1

  # loop and visits detection / handling
  visiting_dir = f"{from_x},{from_y},{to_x},{to_y}"
  visiting_key = f"{to_x},{to_y}"
  if visiting_key in visited:
    visit = 0
    if visiting_dir in visited[visiting_key]:
      return 0
  else:
    visited[visiting_key] = {}
  visited[visiting_key][visiting_dir] = True
  
  cur_item = matrix[to_y][to_x]
  if cur_item == ".":
    # let this beam proceed in the same direction
    return visit + energize(matrix, to_x, to_y, to_x + (to_x - from_x), to_y + (to_y - from_y), visited)

  if cur_item == "/":
    # going right, deflect up
    if from_x < to_x:
      return visit + energize(matrix, to_x, to_y, to_x, to_y - 1, visited)
    # going left, deflect down
    elif from_x > to_x:
      return visit + energize(matrix, to_x, to_y, to_x, to_y + 1, visited)
    # going down, deflect left
    elif from_y < to_y:
      return visit + energize(matrix, to_x, to_y, to_x - 1, to_y, visited)
    # going up, deflect right
    else:
      return visit + energize(matrix, to_x, to_y, to_x + 1, to_y, visited)

  if cur_item == "\\":
    # going right, deflect down
    if from_x < to_x:
      return visit + energize(matrix, to_x, to_y, to_x, to_y + 1, visited)
    # going left, deflect up
    elif from_x > to_x:
      return visit + energize(matrix, to_x, to_y, to_x, to_y - 1, visited)
    # going down, deflect right
    elif from_y < to_y:
      return visit + energize(matrix, to_x, to_y, to_x + 1, to_y, visited)
    # going up, deflect left
    else:
      return visit + energize(matrix, to_x, to_y, to_x - 1, to_y, visited)

  if cur_item == "|":
    # going up or down, keep going
    if from_x == to_x:
      return visit + energize(matrix, to_x, to_y, to_x, to_y + (to_y - from_y), visited)
    # going left or right, split in 2 perpendicular beams that go up and down
    else:
      return visit + energize(matrix, to_x, to_y, to_x, to_y - 1, visited) + energize(matrix, to_x, to_y, to_x, to_y + 1, visited)
  
  if cur_item == "-":
    # going left or right, keep going
    if from_y == to_y:
      return visit + energize(matrix, to_x, to_y, to_x + (to_x - from_x), to_y, visited)
    # going up or down, split in 2 perpendicular beams that go left and right
    else:
      return visit + energize(matrix, to_x, to_y, to_x - 1, to_y, visited) + energize(matrix, to_x, to_y, to_x + 1, to_y, visited)


with open(sys.argv[1]) as f:
  document = f.read().strip()
  lines = document.split('\n')

  matrix = []
  for line in lines:
    matrix.append(list(line))
  
  energized = energize(matrix, -1, 0, 0, 0)

  print(f"energized: {energized}")
