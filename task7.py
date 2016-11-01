#!/usr/bin/env python3

print("\n")
days = int(input("Print number of days - "))
print("\n")

total_distance = 10
total_distance_for_7days = 0
deadline_day_number = 0

for n in range(2, days+1):
  n_day_distance = 10*1.1**(n-1)
  total_distance += n_day_distance
  # a)
  print('Distance for %s days is qual to %f' % (n, n_day_distance))
  # b)
  if n == 7:
    total_distance_for_7days = total_distance
  # c)
  print('Total distance for %s days is qual to %f' % (n, total_distance))
  # d)
  if total_distance < 80:
    deadline_day_number = n
  print('\n')

# b)
if total_distance_for_7days:
  print('Total distance for 7 days is qual to %f' % total_distance_for_7days)

# d)
if deadline_day_number:
  print("Last day number for 80 km is %s" % deadline_day_number)