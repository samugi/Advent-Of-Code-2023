import sys


TOTAL_CYCLES = 1e9

def tilt_left(line):
  matches = line.split("#") #re.findall("#?([\.O]+)#?", line)
  leftified = ["".join(sorted(m, reverse=True)) for m in matches]
  return "#".join(leftified)


def rotate_left(lines):
  rotated = [c for c in zip(*lines)]
  rotated = ["".join(c) for c in rotated]
  rotated.reverse()
  return rotated


def rotate_right(lines):
  rotated = [c for c in zip(*lines[::-1])]
  rotated = ["".join(c) for c in rotated]
  return rotated


def count_left(line, level=1, score=0):
  if not line:
    return score
  line, popped = line[:-1], line[-1]
  if popped == 'O':
    return count_left(line, level + 1, score + level)
  return count_left(line, level + 1, score)


def hash_state(lines):
  return "".join(lines)


loop_finder = {}
def find_loop_size(lines):
  lines = lines.copy()
  cycle = 0

  while True:
    cycle += 1
    for i in range(0, 4):
      # tilt left
      lines = [tilt_left(l) for l in lines]
      
      if i == 0:
        old_state_cycle = loop_finder.get(hash_state(lines))
        if old_state_cycle != None:
          return cycle - old_state_cycle, old_state_cycle
        loop_finder[hash_state(lines)] = cycle

      # rotate right
      lines = rotate_right(lines)


with open(sys.argv[1]) as f:
  document = f.read().strip()
  lines = document.split('\n')

  # position north side left, for easier counting
  lines = rotate_left(lines)

  loop_size, loop_start = find_loop_size(lines)
  loops_todo = int(loop_start + ((TOTAL_CYCLES - loop_start) % loop_size))

  # do loops_todo cycles
  for j in range(0, loops_todo):
    for i in range(0, 4):
      # tilt left
      lines = [tilt_left(l) for l in lines]
      # rotate right
      lines = rotate_right(lines)    

  weight = 0
  # north side still pointing left
  for l in lines:
    weight += count_left(l)
  print(f"final weight: {weight}")
