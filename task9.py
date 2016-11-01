#!/usr/bin/env python3

print("\n")
letter = input("Print a letter: ").lower()
print("\n")

for i in range(ord(letter)+1, ord(letter)+4):
  print(chr(ord('a') + i % ord('a') % 26))
  print('\n')