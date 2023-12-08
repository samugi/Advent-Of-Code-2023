import re
import math 

SCRATCH_CARDS_DOCUMENT = "input.txt"

scratchcards = [1] * 219

def do_play_game(line):
  pattern = r"Card\s+(\d+):\s+(\d+(?: [\d\s]+)*) \|\s+(\d+(?: [\d\s]+)*)"
  numbers = re.match(pattern, line)

  if numbers:
    # -1 because the card number is 1-based, but the list is 0-based
    card_number     = int(numbers.group(1)) - 1
    winning_numbers = [int(num) for num in numbers.group(2).split()]
    my_numbers      = [int(num) for num in numbers.group(3).split()]

    score = len(set(winning_numbers) & set(my_numbers))
    # the following <score> cards are incremented by the current card score
    # multiplied by the n. of copies of the current card (scratchcards[card_number])
    for i in range(score):
      index = card_number + i + 1
      if index < len(scratchcards):
        scratchcards[index] = scratchcards[index] + scratchcards[card_number]

# Read the engine schematic document
with open(SCRATCH_CARDS_DOCUMENT, "r") as f:
  input = f.read()
  total_score = 0

  # Parse each line to load the engine's schematics
  for line in input.splitlines():
    do_play_game(line)

  total_score = sum(scratchcards)

  print(f"Total score: {total_score}")
