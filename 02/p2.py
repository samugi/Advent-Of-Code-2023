import re

GAMES_DOCUMENT = "input.txt"

RED_AVAILABLE   = 12
GREEN_AVAILABLE = 13
BLUE_AVAILABLE  = 14


def parse_game_data_calc_power(string):
  # Parse and remove the game ID
  game_id = re.search("^Game (\d+):", string).group(1)
  string  = string.split(":")[1].strip()

  max_reds   = 0
  max_blues  = 0
  max_greens = 0

  # Load the sets
  sets = string.split(";")
  for s in sets:
    search_red   = re.search("(\d+) red", s)
    search_green = re.search("(\d+) green", s)
    search_blue  = re.search("(\d+) blue", s)

    reds   = search_red and search_red.group(1) or 0
    greens = search_green and search_green.group(1) or 0
    blues  = search_blue and search_blue.group(1) or 0
   
    max_reds   = max(max_reds, int(reds))
    max_greens = max(max_greens, int(greens))
    max_blues  = max(max_blues, int(blues))

  return max_reds * max_greens * max_blues

# Read the games document
with open(GAMES_DOCUMENT, "r") as f:
  input = f.read()
  power_sum = 0

  # Parse each line to calculate the sum of the powers of the sets
  for line in input.splitlines():
    game_power = parse_game_data_calc_power(line)
    power_sum += game_power

  print(f"Game powers sum: {power_sum}")
