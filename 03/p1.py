import re

ENGINE_SCHEMATIC_DOCUMENT = "input.txt"

schematic_data = []


def get_neighbors(beginX, beginY, size):
  endX = beginX + size
  endY = beginY

  row_length = len(schematic_data[beginY])
 
  left_neighbor_idx  = beginX - 1 if beginX > 0 else beginX
  right_neighbor_idx = endX + 1 if endX < row_length - 1 else endX

  above = ""
  level = ""
  below = ""

  if beginY > 0:
    above = schematic_data[beginY - 1][left_neighbor_idx:right_neighbor_idx]
  if beginY < len(schematic_data) - 1:
    below = schematic_data[beginY + 1][left_neighbor_idx:right_neighbor_idx]
  level = schematic_data[beginY][left_neighbor_idx:right_neighbor_idx]

  return f"{above}{level}{below}"
  

def contain_symbol(neighbors):
  for n in neighbors:
    if re.match("[^\d\.]", n):
      return True

  return False


def get_part_numbers_sum(data):
  sum = 0

  for y in range(len(data)):
    row        = data[y]
    cur_number = "0"

    number_indices = re.finditer("\d+", row)
    for found in number_indices:
      num = found.group()
      if contain_symbol(get_neighbors(found.start(), y, len(num))):
        sum += int(num)
      
  return sum


# Read the engine schematic document
with open(ENGINE_SCHEMATIC_DOCUMENT, "r") as f:
  input = f.read()

  # Parse each line to load the engine's schematics
  for line in input.splitlines():
    schematic_data.append(line)
  
  res = get_part_numbers_sum(schematic_data)

  print(f"Result: {res}")
