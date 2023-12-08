class AlmanacNode:
  def __init__(self, src, dest, ranges):
    self.src_name  = src
    self.dest_name = dest
    self.ranges    = ranges

  def get_src(self):
    return self.src

  def get_dest(self):
    return self.dest

  def get_ranges(self):
    return self.ranges

  def calculate_dest(self, source_value):
    for range in self.ranges:
      source_start, dest_start, length = range

      source_offset = source_value - source_start

      if source_value >= source_start and source_value <= source_start + length:
        return dest_start + source_offset

    return source_value
