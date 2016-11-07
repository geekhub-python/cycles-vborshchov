#!/usr/bin/env python3

import string
from random import *

def generate_password():
  result = ''
  for y in range(0,4):
    digit = "".join(choice(string.digits) for x in range(randint(0, 1)))
    letter =  choice(string.ascii_letters)
    result = result + letter + digit

  password = result + "".join(choice(string.ascii_uppercase) for x in range(randint(2, 12)))
  return(password)

print(generate_password())