import sys
from functools import cache

@cache
def count_permutations(line, seq):
  if not seq:
    return 0 if '#' in line else 1
  if not line:
    return 1 if not seq else 0

  n_p = line.count('#')
  n_d = line.count('?')
  if n_p + n_d < sum(seq):
    return 0

  if line[0] == '.': 
    return count_permutations(line[1:], seq)

  # find the first block of #s
  first_block = ""
  for c in line:
    if c == "#":
      first_block += '#'
    else:
      break

  if first_block:
    first_block_size = len(first_block)
    first_block_next_char = line[first_block_size] if first_block_size < len(line) else None

    # if first block is "complete"
    if first_block_next_char == '.':
      # check it for inequality against the seq first el
      if first_block_size != seq[0]:
        return 0

      else:
        line = line[first_block_size + 1:]
        seq = seq[1:]

    # if first block is incomplete
    elif first_block_next_char == '?':
      if first_block_size > seq[0]:
        return 0

    # else: first block is also the last
    else:
      if len(seq) > 1 or first_block_size != seq[0]:
        return 0
      return 1

  # line and seq might have been trimmed above, so check again
  if not line:
    if not seq:
      return 1
    return 0

  first_unk = line.find('?')
  if first_unk != -1:
    line_d = line[:first_unk] + '.' + line[first_unk+1:]
    line_p = line[:first_unk] + '#' + line[first_unk+1:]
    res_w = count_permutations(line_d, seq)
    res_b = count_permutations(line_p, seq)
    return res_w + res_b
  else:
    return count_permutations(line, seq)


def solve(p, lines):
  count = 0
  for i in range(len(lines)):
    l = lines[i]
    record_line = l.split(' ')[0]
    seq_line = l.split(' ')[1]

    if p == '1':
      multiplier = 1
    else:
      multiplier = 5

    record_line = '?'.join([record_line]*multiplier)
    seq_line = ','.join([seq_line]*multiplier)
    count += count_permutations(record_line, eval(seq_line))

  return count

with open(sys.argv[1]) as f:
  document = f.read().strip()
  lines = document.split('\n')
  part = sys.argv[2] if len(sys.argv) > 2 else '2'
  multiplier = 1
  count = solve(part, lines)
  print(f"part {part}: {count}")
