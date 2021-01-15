import math
def magnitude(vector):
  """Returns magnitude of an n-dimensional vector.
  Example usage: magnitude([5,6,7])."""
  sum = 0
  for component in vector:
    sum += component ** 2
  magnitude = math.sqrt(sum)
  return magnitude
