from ddb import DigitDecodingBuffer

CALIBRATION_DOCUMENT = "input.txt"

word_to_int = {
  "one"   : 1,
  "two"   : 2,
  "three" : 3,
  "four"  : 4,
  "five"  : 5,
  "six"   : 6,
  "seven" : 7,
  "eight" : 8,
  "nine"  : 9,
}


def find_first_digit_occurrence(encoded, reverse=False):
  ddbs = []
  if reverse:
    encoded = encoded[::-1]

  for word in word_to_int.keys():
    if reverse:
      search = word[::-1]
    else:
      search = word
    ddbs.append(DigitDecodingBuffer(search, word_to_int[word]))
  
  for char in encoded:
    if char.isdigit():
      found = char
      break
    for ddb in ddbs:
      found = ddb.validateNextChar(char)
      if found > 0:
        break
    if found > 0:
      break

  return found


def parse_calibration_data(string):
  found_digit_left = find_first_digit_occurrence(string)
  found_digit_right = find_first_digit_occurrence(string, True)
  return (found_digit_left, found_digit_right)


# Read the calibration document
with open(CALIBRATION_DOCUMENT, "r") as f:
  input = f.read()
  calibration_value = 0

  # Parse each line to load calibration values
  for line in input.splitlines():
    calibration_data = parse_calibration_data(line)
    partial_calibration_value = int(f"{calibration_data[0]}{calibration_data[1]}")
    calibration_value += partial_calibration_value

  print(f"Calibration value: {calibration_value}")
