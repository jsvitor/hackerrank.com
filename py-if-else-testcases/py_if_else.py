#!/bin/python3

import math
import os
import random
import re
import sys
"""
  Task
  Given an integer, , perform the following conditional actions:

  If n is odd, print Weird
  If n is even and in the inclusive range of 2 to 5, print Not Weird
  If n is even and in the inclusive range of 6 to 20, print Weird
  If n is even and greater than 20, print Not Weird
"""


def is_weird(number):
    even = number % 2 == 0
    if not (even):
        return 'Weird'
    elif even and (2 < number < 5):
        return 'Not Weird'
    elif even and (6 < number <= 20):
        return 'Weird'
    elif even and number > 20:
        return 'Not Weird'


if __name__ == '__main__':
    n = int(input().strip())
    if 1 <= n <= 100:
        print(is_weird(n))
