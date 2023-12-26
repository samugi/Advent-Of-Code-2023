import sys
import re

hashy_hash = {}

def hash(s, h):
  h += ord(s)
  h *= 17
  h %= 256
  return h

def hash_label(label, h=0):
  for s in label:
    h = hash(s, h)
  return h

with open(sys.argv[1]) as f:
  document = f.read().strip()
  steps = document.split(',')
  score = 0
  
  test_dict = {}

  # load lenses in boxes
  for s in steps:
    m = re.match("([a-z]+)([=-])(\d+)?", s)
    if not m:
      raise Exception(f"bad step: {s}")
    
    label     = m.group(1)
    operation = m.group(2)
    focal_l   = m.group(3)

    label_hash = hash_label(label)
    dest_dict = hashy_hash[label_hash] if label_hash in hashy_hash else {}

    if operation == '=':
      dest_dict[label] = int(focal_l)
    elif operation == '-':
      if label in dest_dict:
        del dest_dict[label]
    else:
      raise Exception(f"bad operation: {operation}")
    hashy_hash[label_hash] = dest_dict
  
  # calc score
  for k, v in hashy_hash.items():
    pos = 0
    for _, vv in v.items():
      pos += 1
      score += (1 + k) * pos * vv

print(f"result: {score}")
