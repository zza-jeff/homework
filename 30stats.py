#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

# import numbers into a new list as float
number = [float(sys.argv[i]) for i in range(1, len(sys.argv))]
count = len(number)

# sort the list, then get simple stats first
number.sort()
min = number[0]
max = number[count - 1]
mean = sum(number) / count

# odd count vs. even count
if count % 2 != 0: median = number[count // 2]
else: median = sum(number[count // 2 - 1:count // 2 + 1]) / 2

# use another list to calculate variance, then standard deviation
difference = [(number[i] - mean) ** 2 for i in range(count)]
var = sum(difference) / count
std = var ** 0.5

print("Count:", f'{count}')
print("Minimum:", f'{min}')
print("Maximum:", f'{max}')
print("Mean:", f'{mean:.3f}')
print("Std. dev:", f'{std:.3f}')
print("Median:", f'{median:.3f}')
