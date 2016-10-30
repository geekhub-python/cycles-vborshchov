#!/usr/bin/env python3

start_number = 5
end_number = 14
product = 1

for x in range(start_number, end_number):
  product *= x


print("Product of 5 * 6 * 7 * ... * 13 is equal %s" % product)