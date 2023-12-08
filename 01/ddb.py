class DigitDecodingBuffer:
  def __init__(self, word, digit):
    self.word   = word
    self.digit  = digit
    self.cursor = 0
  
  def validateNextChar(self, char):
    if char == self.word[self.cursor]:
      self.cursor += 1
      if self.cursor == len(self.word):
        self.cursor = 0
        return self.digit
    else:
      self.cursor = 1 if char == self.word[0] else 0
    return 0
