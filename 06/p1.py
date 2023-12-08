import sys
import math

with open(sys.argv[1]) as f:
  document = f.read().strip()
  lines    = document.split('\n')

  t = lines[0].split(":")[1].strip()
  d = lines[1].split(":")[1].strip()

  # (time, dist) tuples like: [(7, 9), (15, 40), (30, 200)]
  races = list(zip([int(x) for x in t.split()], [int(x) for x in d.split()]))
  
  # T1 = charging time
  # T2 = racing time
  # T = T1 + T2
  # D = V  * T2
  # V = T1
  # D = T1  * (T - T1)
  MULT = 1
  for race in races:
    T = race[0]
    D = race[1]
  
    T1 = abs((T - (T**2 - 4*D)**0.5) / 2)
    dist_from_ideal = abs(T1 - T/2)

    # TR is the right bound of the winning range
    TR = T1 + 2 * dist_from_ideal
    ideal_range = math.floor(TR) - math.floor(T1)

    # if T1 is an integer, we need to subtract 1 from the ideal range
    # to make sure we don't include T1 in the range that beats T1
    if T1 % 1 == 0:
      ideal_range -= 1
    
    MULT *= ideal_range
  
  print(MULT)
