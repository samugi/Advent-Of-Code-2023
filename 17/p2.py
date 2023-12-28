import sys

from heapq import heappush, heappop

with open(sys.argv[1]) as f:
  matrix = [list(map(int, line.strip())) for line in f]

  # first element of the tuple is heat loss, the heap is sorted by heat loss
  # so the quickest way to reach a certain state (node, and direction) is
  # always at the top of the heap
  s = (0, 0, 0, 0, 0, 0)

  visited = set()
  q = [s]

  while(q):
    heat_loss, x, y, dx, dy, steps = heappop(q)
    if (x, y, dx, dy, steps) in visited:
      continue
    visited.add((x, y, dx, dy, steps))
    
    if x == len(matrix[0]) - 1 and y == len(matrix) - 1 and steps >= 4:
      print(f"min heat loss: {heat_loss} with last steps: {steps}")
      break

    # only consider the current direction if we haven't taken 10 steps yet
    if steps < 10:
      nx = x + dx
      ny = y + dy

      if 0 <= nx < len(matrix[0]) and 0 <= ny < len(matrix):
        nhl = heat_loss + matrix[ny][nx]
        heappush(q, (nhl, nx, ny, dx, dy, steps+1))

    if steps < 4 and (dx, dy) != (0, 0):
      continue

    for ndx, ndy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      # skip current (already done if applicable) and opposite (invalid) dirs
      if (dx, dy) == (ndx, ndy) or (dx, dy) == (-ndx, -ndy):
        continue

      nx = x + ndx
      ny = y + ndy

      if 0 <= nx < len(matrix[0]) and 0 <= ny < len(matrix):
        nhl = heat_loss + matrix[ny][nx]
        heappush(q, (nhl, nx, ny, ndx, ndy, 1))
