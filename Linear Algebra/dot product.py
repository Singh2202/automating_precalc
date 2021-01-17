def dot_product(vector1, vector2):
  dot_product = 0
  for pair in zip(vector1, vector2):
    dot_product += pair[0] * pair[1]
  return dot_product
