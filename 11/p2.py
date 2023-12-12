import sys


EXPANSION = 1000000
expanded_rows = {}
expanded_cols = {}

def count_expanded_rows_in_range(start, end):
  count = 0
  for i in range(start, end + 1):
    if expanded_rows[i]:
      count += 1
  return count

def count_expanded_cols_in_range(start, end):
  count = 0
  for i in range(start, end + 1):
    if expanded_cols[i]:
      count += 1
  return count

with open(sys.argv[1]) as f:
  document = f.read().strip()
  lines    = document.split('\n')

  image = []
  for line in lines:
    image.append(list(line))

  expanded_rows = {n: True for n in range(len(image))}
  expanded_cols = {n: True for n in range(len(image[0]))}

  # find galaxies and rows and columns with no galaxies (expansions)
  galaxies = []
  for i in range(len(image)):
    for j in range(len(image[i])):
      if image[i][j] == '#':
        galaxies.append((i, j))
        expanded_rows[i] = False
        expanded_cols[j] = False
  
  # find all galaxies pairs
  pairs = []
  for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
      pairs.append((galaxies[i], galaxies[j]))

  total_distance = 0
  for p in pairs:
    exp_r = count_expanded_rows_in_range(min(p[0][0], p[1][0]), max(p[0][0], p[1][0]))
    exp_c = count_expanded_cols_in_range(min(p[0][1], p[1][1]), max(p[0][1], p[1][1]))
    total_distance += (
      abs(p[0][0] - p[1][0]) + abs(p[0][1] - p[1][1]) +
      (exp_r * EXPANSION) - exp_r +
      (exp_c * EXPANSION) - exp_c
    )
  print(total_distance)
