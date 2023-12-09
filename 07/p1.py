import sys
import math

alphabet = {
  '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
  '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11,
  'Q': 12, 'K': 13, 'A': 14
}

type_to_pow = {
  'high_card': 0,
  'one_pair': 1,
  'two_pair': 2,
  'three_of_a_kind': 3,
  'full_house': 4,
  'four_of_a_kind': 5,
  'five_of_a_kind': 6,
}

def base13_to_base10(num):
  num = num.upper()
  res = 0
  for i, digit in enumerate(reversed(num)):
    res += alphabet[digit] * 13**i
  return res

def find_type(hand):
  # hand is a string like 'KK677'
  hand = sorted(hand, key=lambda x: alphabet[x], reverse=True)
  counts = {}
  for card in hand:
    if card not in counts:
      counts[card] = 0
    counts[card] += 1

  # counts is a dict like {'K': 2, '6': 2, '7': 1}
  if len(counts) == 1:
    return 'five_of_a_kind'
  elif len(counts) == 2:
    if 4 in counts.values():
      return ('four_of_a_kind')
    else:
      return ('full_house')
  elif len(counts) == 3:
    if 3 in counts.values():
      return ('three_of_a_kind')
    else:
      return ('two_pair')
  elif len(counts) == 4:
    return ('one_pair')
  else:
    return ('high_card')

def get_value(h):
    hand = h[0]

    b13  = base13_to_base10(hand)
    typ  = find_type(hand)
    poww = type_to_pow[typ]

    return b13 * 13 ** poww

with open(sys.argv[1]) as f:
  document = f.read().strip()
  lines    = document.split('\n')

  # (hand, bid) tuples like: [(32T3K, 765), (T55J5, 684), (KK677, 28)]
  hands = [tuple(h.split()) for h in lines]
  hands.sort(key = lambda x: get_value(x))

  res = 0
  for i, hand in enumerate(hands):
    print(f"rank: {i+1}: {hand[0]} {hand[1]}")
    res += (i+1) * int(hand[1])

  print(f"Result: {res}")
