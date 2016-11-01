#!/usr/bin/env python3

import re

for n in range(1000, 10000):
  matchObj = re.search('(?=5|6)', str(n))
  if not matchObj:
    print("%s, " % n, end='')