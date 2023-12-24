import sys


tracker = {}


def tilt_the_lever(lines, score=0, level=1):
  if not lines:
    return score

  l = lines.pop()
  for i in range(len(l)):
    # for each rolling stone add it to the tracker on its index
    if l[i] == 'O':
      stones_in_i = tracker.get(i) or 0
      tracker[i] = stones_in_i + 1
     # for each cubic stone get stones from the tracker and update score
    if l[i] == '#':
      rol_lev = level - 1
      stones_in_i = tracker.get(i) or 0
      for j in range(1, stones_in_i + 1):
        score += rol_lev
        rol_lev -= 1
      tracker[i] = 0
  return tilt_the_lever(lines, score, level + 1)


with open(sys.argv[1]) as f:
  document = f.read().strip()
  lines = document.split('\n')

  score = 0
  # make the bottom behave like other cubic stones
  lines.insert(0, '#' * len(lines[0]))
  score = tilt_the_lever(lines)

print(f"score: {score}")
