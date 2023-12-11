import sys
import math
import re

move_to_index = {
  'L': 0,
  'R': 1,
}

with open(sys.argv[1]) as f:
  document = f.read().strip()
  lines    = document.split('\n')

  moves   = list(lines[0])
  pattern = "^(\w{3})\s=\s\((\w{3}),\s(\w{3})\)"
  network = { x: (y, z) for (x, y, z) in [re.match(pattern, s).groups() for s in lines[2:]]}

  curr_nodes = []
  found_dest = []
  move_index = 0
  steps = 0

  for node_name in network.keys():
    if node_name[-1:] == 'A':
      curr_nodes.append(node_name)

  while len(found_dest) < len(curr_nodes):

    for n in curr_nodes:
      if n[-1:] == 'Z':
        found_dest.append(steps)

    curr_options = [(L, R) for (L, R) in [network[cn] for cn in curr_nodes]]
    move = moves[move_index]
    
    # update information to reflect the move
    move_index = (move_index + 1) % len(moves)
    curr_nodes = [opts[move_to_index[move]] for opts in curr_options]
    steps += 1

  # works because distance from start to end is same as from end to end
  # (paths loop from/to the same end once they reach it)
  print(math.lcm(*found_dest))
  