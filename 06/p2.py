import sys
import math
import re

with open(sys.argv[1]) as f:
  document = f.read().strip()
  lines    = document.split('\n')

  t = lines[0].split(":")[1].strip()
  d = lines[1].split(":")[1].strip()

  t = re.sub(r'(\s+)', r'', t)
  d = re.sub(r'(\s+)', r'', d)

  # (time, dist) tuples like: [(7, 9), (15, 40), (30, 200)]
  races = list(zip([int(x) for x in t.split()], [int(x) for x in d.split()]))
  
  # same as p1
  MULT = 1
  for race in races:
    T = race[0]
    D = race[1]
  
    T1 = abs((T - (T**2 - 4*D)**0.5) / 2)
    TR = T1 + 2 * abs(T1 - T/2)
    ideal_range = math.floor(TR) - math.floor(T1)

    if T1 % 1 == 0:
      ideal_range -= 1
    MULT *= ideal_range
  
  print(MULT)
