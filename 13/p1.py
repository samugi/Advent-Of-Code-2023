import sys


def sym_index(group, idx_above, initial_idx_above, matched_once=False):
  idx_below = idx_above + 1
  if (idx_below >= len(group) or idx_above < 0):
    if matched_once:
      return initial_idx_above
    return -1

  if group[idx_above] == group[idx_below]:
    group = group[0: idx_above] + group[idx_below+1:]
    return sym_index(group, idx_above - 1, initial_idx_above, True)
  return -1


def sym_info(block):
  for i in range(len(block)):
    idx = sym_index(block, i, i)
    if idx != -1:
      return idx
  return -1


with open(sys.argv[1]) as f:
  document = f.read().strip()
  blocks = document.split('\n\n')

  score = 0
  for block in blocks:
    lines = block.split('\n')
    block_rows = []
    for line in lines:
      block_rows.append(line)
    block_cols = ["".join(c) for c in zip(*block_rows)]

    sym_idx_rows = sym_info(block_rows)
    sym_idx_cols = sym_info(block_cols)

    if sym_idx_rows > sym_idx_cols:
      score += 100 * (sym_idx_rows + 1)
    else:
      score += sym_idx_cols + 1
  
  print(f"score: {score}")
