import sys

def hash(s, cur_val):
  cur_val += ord(s)
  cur_val *= 17
  cur_val %= 256
  return cur_val

def get_updated_cur_val(step, cur_val=0):
  for s in step:
    cur_val = hash(s, cur_val)
  return cur_val

with open(sys.argv[1]) as f:
  document = f.read().strip()
  steps = document.split(',')
  score = 0
  for s in steps:
    score += get_updated_cur_val(s)

print(f"result: {score}")
