import sys
from Levenshtein import distance


def sym_index_with_a_smudge(block, idx_above, initial_idx_above, smudges=0):
  idx_below = idx_above + 1
  if idx_below >= len(block) or idx_above < 0:
    if smudges == 1:
      return initial_idx_above
    return -1
  
  smudges += distance(block[idx_above], block[idx_below])
  if smudges <= 1:
    block = block[0: idx_above] + block[idx_below+1:]
    return sym_index_with_a_smudge(block, idx_above - 1, initial_idx_above, smudges)
  return -1


def get_block_sym_index(block):
  for i in range(len(block)):
    idx = sym_index_with_a_smudge(block, i, i)
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

    sym_idx_rows = get_block_sym_index(block_rows)
    sym_idx_cols = get_block_sym_index(block_cols)

    if sym_idx_rows > sym_idx_cols:
      score += 100 * (sym_idx_rows + 1)
    else:
      score += sym_idx_cols + 1
  
  print(f"score: {score}")
