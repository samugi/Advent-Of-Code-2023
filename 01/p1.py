CALIBRATION_DOCUMENT = "input.txt"

# Parse the calibration data to extract the first and last digits from each
# line. Optimized to read the minimum amount of characters, instead of just
# replacing all non-digits and reading first and last, because we want to
# calibrate this trebuchet as fast as possible don't we?
def parse_calibration_data(string):
  length = len(string)

  left_digit = None
  right_digit = None

  for i in range(length):
    left = string[i]
    right = string[length - i - 1]

    # assign left and right digits
    left_digit = (
      left_digit if left_digit else (
        left if left.isdigit() else None
      )
    )

    right_digit = (
      right_digit if right_digit else (
        right if right.isdigit() else None
      )
    )

    if left_digit and right_digit:
      break

  return (left_digit, right_digit)


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
