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

  curr_node = 'AAA'
  move_index = 0
  steps = 0
  while curr_node != 'ZZZ':
    curr_options = network[curr_node]
    move = moves[move_index]
    
    # update information to reflect the move
    move_index = (move_index + 1) % len(moves)
    curr_node = curr_options[move_to_index[move]]
    steps += 1
  
  print(steps)
  