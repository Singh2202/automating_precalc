def determinant(matrix):
  """Returns the determinant of a 2X2 or 3X3 matrix. Example usage: determinant([[6,5,2], [4,3,2], [4,3,2]]) or determinant([[5,6], [3,3]])."""
  if len(matrix) == 2:
    determinant = matrix[1][1]*matrix[0][0] - matrix[1][0]*matrix[0][1]
  elif len(matrix) == 3:
    c1 = matrix[0][0]
    c2 = matrix[0][1]
    c3 = matrix[0][2]
    determinant_1 = matrix[2][2]*matrix[1][1] - matrix[2][1]*matrix[1][2]
    determinant_2 = matrix[2][2]*matrix[1][0] - matrix[2][0]*matrix[1][2]
    determinant_3 =  matrix[2][1]*matrix[1][0] - matrix[2][0]*matrix[1][1]
    determinant = c1*determinant_1 - c2*determinant_2 + c3*determinant_3
  return determinant
