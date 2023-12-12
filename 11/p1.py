import sys


with open(sys.argv[1]) as f:
  document = f.read().strip()
  lines    = document.split('\n')

  image = []
  for line in lines:
    image.append(list(line))

  ## expand space
  # expand rows
  image = [l if '#' in l else ['.' for _ in image[0]] for l in image for _ in range(1 if '#' in l else 2)]
  # rotate 90 degrees
  image = [[image[j][i] for j in range(len(image))] for i in range(len(image[0]))]
  # expand cols
  image = [l if '#' in l else ['.' for _ in image[0]] for l in image for _ in range(1 if '#' in l else 2)]
  # rotate back
  image = [[image[j][i] for j in range(len(image))] for i in range(len(image[0]))]

  # find galaxies and rows and columns with no galaxies (expansions)
  galaxies = []
  for i in range(len(image)):
    for j in range(len(image[i])):
      if image[i][j] == '#':
        galaxies.append((i, j))
  
  # find all galaxies pairs
  pairs = []
  for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
      pairs.append((galaxies[i], galaxies[j]))

  total_distance = 0
  for p in pairs:
    total_distance += abs(p[0][0] - p[1][0]) + abs(p[0][1] - p[1][1])
  print(total_distance)
