import math
def magnitude(vector):
  """Returns magnitude of an n-dimensional vector.
  Example usage: magnitude([5,6,7])."""
  total = 0
  for component in vector:
    total += component ** 2
  magnitude = math.sqrt(total)
  return magnitude
