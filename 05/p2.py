import sys

document = open(sys.argv[1]).read().strip()
lines    = document.split('\n')
blocks   = document.split('\n\n')
seeds, *mappings = blocks

seeds = [int(x) for x in seeds.split(':')[1].split()]

class Processor:
  def __init__(self, mappings):
    mappings = mappings.split('\n')[1:]
    self.mappings = [tuple([int(x) for x in mapping.split()]) for mapping in mappings]
    
  # here rng is a (start, end) tuple 
  def process(self, rng):
    res = []
    for (m_dest, m_src, m_size) in self.mappings:
      m_src_end = m_src + m_size

      remaining = []
      while rng:
        (rng_s, rng_e) = rng.pop()

        # intersect to determine what gets transformed and what remains the same
        inters = (max(rng_s, m_src), min(rng_e, m_src_end))
        left = (rng_s, min(rng_e, m_src))
        right = (max(rng_s, m_src_end), rng_e)

        if left[1] > left[0]:
          remaining.append(left)
        if right[1] > right[0]:
          remaining.append(right)
        if inters[1] > inters[0]:
          # transform to append it relative to the dest
          offset_l = inters[0] - m_src
          offset_r = inters[1] - m_src
          res.append((m_dest + offset_l, m_dest + offset_r))
      rng = remaining
      
    return res + remaining
         

# load the processors, one for each mapping
processors = [Processor(m) for m in mappings]
processed = []

for (seed_start, seed_size) in list(zip(seeds[::2], seeds[1::2])):
  seed_end = seed_start + seed_size
  result = [(seed_start, seed_end)]

  for p in processors:
    result = p.process(result)

  processed.append(min(result)[0])
print(min(processed))
