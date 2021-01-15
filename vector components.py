import math
def components(magnitude, angle):
  """Example usage: components(60, math.pi/2).
  To enter pi, use math.pi.IndexError"""
  x = magnitude * math.cos(angle)
  y = magnitude * math.sin(angle)
  if abs(x) < 1e-14: #patch for floating point arithmetic
    x = 0
  if abs(y) < 1e-14:
    y = 0
  else:
    x, y = x, y 
  return x, y 

