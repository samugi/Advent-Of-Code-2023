import sys
import re


directions_coords = {
  'U': (-1,  0),
  'R': ( 0,  1),
  'D': ( 1,  0),
  'L': ( 0, -1),
}

directions_opts = {
  'U': ['|', '7', 'F'],
  'D': ['|', 'L', 'J'],
  'R': ['-', '7', 'J'],
  'L': ['-', 'F', 'L'],
}

allowed_directions = {
  '|': {
    'U': directions_opts['U'],
    'D': directions_opts['D'],
  },
  '-': {
    'L': directions_opts['L'],
    'R': directions_opts['R'],
  },
  'L': {
    'U': directions_opts['U'],
    'R': directions_opts['R'],
  },
  'J': {
    'U': directions_opts['U'],
    'L': directions_opts['L'],
  },
  '7': {
    'D': directions_opts['D'],
    'L': directions_opts['L'],
  },
  'F': {
    'D': directions_opts['D'],
    'R': directions_opts['R'],
  },
  'S': {
    'U': directions_opts['U'],
    'D': directions_opts['D'],
    'L': directions_opts['L'],
    'R': directions_opts['R'],
  },
}


def next_pos(curr, prev, sketch, avoid=None):
  for d in directions_coords:
    x, y = directions_coords[d]

    next_candidate = (curr[0] + x, curr[1] + y)

    if next_candidate == prev or next_candidate == avoid:
      continue

    allowed_from_here = allowed_directions[sketch[curr[0]][curr[1]]]

    allowed_d = d in allowed_from_here and allowed_from_here[d] or []
    if sketch[curr[0] + x][curr[1] + y] in allowed_d:
      prev = curr
      curr = next_candidate
      break

  return curr, prev

visited = {}

def replace_with_symbol(sketch, s):
  upwards    = sketch[s[0] - 1][s[1]]
  downwards  = sketch[s[0] + 1][s[1]]
  leftwards  = sketch[s[0]][s[1] - 1]
  rightwards = sketch[s[0]][s[1] + 1]

  if upwards in directions_opts['U'] and downwards in directions_opts['D']:
    sketch[s[0]][s[1]] = '|'
  elif leftwards in directions_opts['L'] and rightwards in directions_opts['R']:
    sketch[s[0]][s[1]] = '-'
  elif upwards in directions_opts['U'] and rightwards in directions_opts['R']:
    sketch[s[0]][s[1]] = 'L'
  elif upwards in directions_opts['U'] and leftwards in directions_opts['L']:
    sketch[s[0]][s[1]] = 'J'
  elif downwards in directions_opts['D'] and leftwards in directions_opts['L']:
    sketch[s[0]][s[1]] = '7'
  elif downwards in directions_opts['D'] and rightwards in directions_opts['R']:
    sketch[s[0]][s[1]] = 'F'
  else:
    raise Exception(f"Could not replace {s} with a symbol")
    

with open(sys.argv[1]) as f:
  document = f.read().strip()
  lines    = document.split('\n')

  # wrap in dots (.) to make it easier to navigate
  lines.insert(0, '.' * len(lines[0]))
  lines = ['.' + l + '.' for l in lines]
  lines.append('.' * len(lines[0]))

  # insert the input in a 2D array
  sketch = []
  for line in lines:
    sketch.append(list(line))

  # find the starting point
  s, curr1, curr2 = None, None, None
  prev1, prev2 = (-1, -1), (-1, -1)
  for i in range(len(sketch)):
    for j in range(len(sketch[i])):
      if sketch[i][j] == 'S':
        curr1 = (i, j)
        curr2 = (i, j)
        s = (i, j)
        break

  # add starting point to visited
  visited[curr1] = True

  # visit the first position on both directions
  curr1, prev1 = next_pos(curr1, prev1, sketch)
  visited[curr1] = True
  curr2, prev2 = next_pos(curr2, prev2, sketch, curr1)
  visited[curr2] = True
  steps = 1

  # reuse p1 alg
  while not (curr1 == curr2 and sketch[curr1[0]][curr1[1]] != 'S'):
    # move curr1
    curr1, prev1 = next_pos(curr1, prev1, sketch)
    visited[curr1] = True
 
    # move curr2
    curr2, prev2 = next_pos(curr2, prev2, sketch)
    visited[curr2] = True
 
    steps += 1

  # replace `S` with the right symbol
  replace_with_symbol(sketch, s)

  # Count number of "enclosed" spaces
  enclosed = 0
  for i in range(len(sketch)):
    inside = False
    for j in range(len(sketch[i])):
      cursor = sketch[i][j]

      if (i, j) in visited:
        if cursor == "|":
          inside = not inside

        else:
          visit_buff += cursor
          if re.match(".*F\-*J", visit_buff) or re.match(".*L\-*7", visit_buff):
            inside = not inside
            visit_buff = ""

        continue

      else:
        visit_buff = ""

      if (i, j) not in visited and inside:
        enclosed += 1

  print(f"enclosed spaces: {enclosed}")
