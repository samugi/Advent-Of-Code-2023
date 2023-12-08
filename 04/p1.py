import re
import math 

SCRATCH_CARDS_DOCUMENT = "input.txt"


def get_points(line):
  pattern = r"Card\s+\d+:\s+(\d+(?: [\d\s]+)*) \|\s+(\d+(?: [\d\s]+)*)"
  numbers = re.match(pattern, line)

  if numbers:
    winning_numbers = [int(num) for num in numbers.group(1).split()]
    my_numbers      = [int(num) for num in numbers.group(2).split()]

    # would use this if it were possible to "win many times with the same n"
    # matches = len([num for num in my_numbers if num in winning_numbers])
    matches = len(set(winning_numbers) & set(my_numbers))
    exp     = matches - 1 if matches > 0 else float('-inf')

    return int(2 ** exp)
  return 0

# Read the engine schematic document
with open(SCRATCH_CARDS_DOCUMENT, "r") as f:
  input = f.read()
  total_score = 0

  # Parse each line to load the engine's schematics
  for line in input.splitlines():
    total_score += get_points(line)

  print(f"Total score: {total_score}")
