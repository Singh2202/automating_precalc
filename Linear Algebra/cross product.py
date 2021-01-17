def cross_product(vector1, vector2):
  matrix = []
  row_1 = [1, 1, 1]
  row_2 = []
  row_3 = []
  for component in vector1:
    row_2.append(component)
  for component in vector2:
    row_3.append(component)
  matrix.extend((row_1, row_2, row_3))
  determinant_1 = str(matrix[2][2]*matrix[1][1] - matrix[2][1]*matrix[1][2])
  determinant_2 = str(-1*(matrix[2][2]*matrix[1][0] - matrix[2][0]*matrix[1][2]))
  determinant_3 = str(matrix[2][1]*matrix[1][0] - matrix[2][0]*matrix[1][1])
  cross_product = "< " + determinant_1 + "," + determinant_2 + "," + determinant_3 + " >"
  return cross_product
