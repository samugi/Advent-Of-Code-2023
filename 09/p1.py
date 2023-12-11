import sys


def predict_next(seq):
  if all(v == 0 for v in seq):
    return 0

  next_seq = [int(y) - int(x) for (x, y) in zip(seq, seq[1:])]

  return int(seq[-1]) + predict_next(next_seq)  


with open(sys.argv[1]) as f:
  document = f.read().strip()
  lines    = document.split('\n')

  result = 0
  for line in lines:
    seq = line.split()
    
    result += predict_next(seq)
  
  print(result)
