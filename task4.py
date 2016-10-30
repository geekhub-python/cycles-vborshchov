#!/usr/bin/env python3

print('Lets find a number\n')

BASE_NUMBER = 2*3*3*4*5*6*7*8*9*10

for x in range(100):
  result = BASE_NUMBER*x + 1
  if result % 11 == 0:
    print(result)