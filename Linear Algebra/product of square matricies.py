import itertools
def product(matrix1, matrix2):
"""Works only for square matricies. Example usage: product([[1,2,3], [4,5,6], [7,8,9]], [[1,2,3], [4,5,6], [7,8,9]])."""
  rows = []
  columns = []
  for row in matrix1:
    rows.append(row)
  for index in range(len(matrix2)):
    column = []
    for row in matrix2:
      column.append(row[index])
    columns.append(column)
  final_matrix = []
  for pair in itertools.product(rows, columns):
    row = []
    for pair2 in zip(pair[0], pair[1]):
      row.append(pair2[0] * pair2[1])
    final_matrix.append(sum(row))
  final_matrix2  = [final_matrix[i:i + len(matrix1)] for i in range(0, len(final_matrix), len(matrix1))]
  return final_matrix2
