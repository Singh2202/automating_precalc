three_by_three = [[], [], []]
c1 = three_by_three[0][0]
c2 = three_by_three[0][1]
c3 = three_by_three[0][2]
determinant_1 = three_by_three[2][2]*three_by_three[1][1] - three_by_three[2][1]*three_by_three[1][2]
determinant_2 = three_by_three[2][2]*three_by_three[1][0] - three_by_three[2][0]*three_by_three[1][2]
determinant_3 =  three_by_three[2][1]*three_by_three[1][0] - three_by_three[2][0]*three_by_three[1][1]
determinant = c1*determinant_1 - c2*determinant_2 + c3*determinant_3
print(determinant)
