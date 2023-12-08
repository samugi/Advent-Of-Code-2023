import re

GAMES_DOCUMENT = "input.txt"

RED_AVAILABLE   = 12
GREEN_AVAILABLE = 13
BLUE_AVAILABLE  = 14


def parse_game_data(string):
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

  return {
    "id"       : int(game_id),
    "possible" : max_reds   <= RED_AVAILABLE   and
                 max_greens <= GREEN_AVAILABLE and
                 max_blues  <= BLUE_AVAILABLE
  }

# Read the games document
with open(GAMES_DOCUMENT, "r") as f:
  input = f.read()
  ids_sum = 0

  # Parse each line to load valid game IDs
  for line in input.splitlines():
    game_data = parse_game_data(line)
    if game_data["possible"]:
      ids_sum += game_data["id"]

  print(f"Game IDs sum: {ids_sum}")
