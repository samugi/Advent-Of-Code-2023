import re

ENGINE_SCHEMATIC_DOCUMENT = "input.txt"

schematic_data = []


def get_is_adjacent(x, x1, x2):
  closest_point = min(abs(x1 - x), abs(x2 - x))

  return closest_point <= 1


def get_adjacent_numbers(x, y):
  row = schematic_data[y]
  number_iter = re.finditer("\d+", row)

  numbers = []
  for found in number_iter:
    is_adjacent = get_is_adjacent(x, found.start(), found.end() - 1)
    if is_adjacent:
      numbers.append(int(found.group()))

  return numbers


def search_adjacent_in_neighbors(x, y):
  adj_numbers = []

  if y > 0:
    adj_numbers.extend(get_adjacent_numbers(x, y - 1))
  if y < len(schematic_data) - 1:
    adj_numbers.extend(get_adjacent_numbers(x, y + 1))
  adj_numbers.extend(get_adjacent_numbers(x, y))
  
  return adj_numbers


def get_gear_ratio_sum(data):
  sum = 0

  for y in range(len(data)):
    row = data[y]
    gear_candidates = re.finditer("\*", row)
    for found in gear_candidates:
      numbers = search_adjacent_in_neighbors(found.start(), y)
      if len(numbers) == 2:
        sum += numbers[0] * numbers[1]
      
  return sum


# Read the engine schematic document
with open(ENGINE_SCHEMATIC_DOCUMENT, "r") as f:
  input = f.read()

  # Parse each line to load the engine's schematics
  for line in input.splitlines():
    schematic_data.append(line)
  
  res = get_gear_ratio_sum(schematic_data)

  print(f"Result: {res}")
