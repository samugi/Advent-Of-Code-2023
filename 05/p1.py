import re
import math 

from AlmanacNode import AlmanacNode

ALMANAC_DOCUMENT = "input_t.txt"

seeds = []
almanac_nodes = []


def get_range_parameters(ranges):
  range_pattern = r"(\d+)\s(\d+)\s(\d+)"
  range_matcher = re.finditer(range_pattern, ranges)

  out_map = []

  for match in range_matcher:
    dest_start   = int(match.group(1))
    source_start = int(match.group(2))
    length       = int(match.group(3))

    out_map.append((source_start, dest_start, length))
  
  return out_map


def process_almanac(almanac):
  # load seeds
  seeds_pattern = r"seeds:\s+(\d+(?: [\d\s]+)*)"
  seeds_matcher = re.match(seeds_pattern, almanac)

  if seeds_matcher:
    seeds = [int(s) for s in seeds_matcher.group(1).split()]
    # strip seeds section away from the almanac
    almanac = almanac[seeds_matcher.end():]

  # load mappings
  mappings_pattern = r"((\w+)\-to\-(\w+)\s+map:(?:\n(\d+(?: [\d\s]+)*)))"
  mappings_matcher = re.finditer(mappings_pattern, almanac, re.MULTILINE)

  for match in mappings_matcher:
    source = match.group(2)
    dest   = match.group(3)
    ranges = match.group(4)

    range_parameters = get_range_parameters(ranges)
    # looks like we can just assume input-output pairs are in order
    # and there are no unneded maps, so we don't need a graph after all
    almanac_nodes.append(AlmanacNode(source, dest, range_parameters))

  # find closest location
  closest_location = float("inf")
  for seed in seeds:
    src = seed
    for node in almanac_nodes:
      src = node.calculate_dest(src)
    closest_location = min(closest_location, src)
  
  return closest_location

# Read the engine schematic document
with open(ALMANAC_DOCUMENT, "r") as f:
  input = f.read()
  total_score = 0

  closest = process_almanac(input)
  print(f"Closest: {closest}")
