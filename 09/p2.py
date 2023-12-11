import sys


def predict_prev(seq):
  if all(v == 0 for v in seq):
    return 0

  next_seq = [int(y) - int(x) for (x, y) in zip(seq, seq[1:])]

  return int(seq[0]) - predict_prev(next_seq)  


with open(sys.argv[1]) as f:
  document = f.read().strip()
  lines    = document.split('\n')

  result = 0
  for line in lines:
    seq = line.split()
    
    result += predict_prev(seq)
  
  print(result)
