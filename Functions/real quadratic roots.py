import math
def quadratic_roots(a,b,c):
 solution_1 = (-1*b + math.sqrt(b**2 - 4*a*c))/(2*a)
 solution_2 = (-1*b - math.sqrt(b**2 - 4*a*c))/(2*a)
 if solution_1 == solution_2:
   return solution_1
 else:
   return solution_1, solution_2
