#!/usr/bin/env python3

print('\n')
print('Muliplication table\n')

def table_line(a,b):
  result = a*b
  return "%s x %s = %s" % (a, b, result)

for i in range(1, 11):
  for j in range(1, 11):
    print(table_line(i, j))
