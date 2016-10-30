#!/usr/bin/env python3

print('ABC\n')

for i in range(ord('a'), ord('z')+1):
  if (i-2) % 5 == 0:
    print('\n')
  print(chr(i), end="")


print('\n')