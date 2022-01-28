#!/usr/bin/env python3

# Print out all the unique pairwise amino acid combinations
# AC is the same as CA
# Skip AA, CC etc.
# Also print out how many combinations there are

aa = 'ACDEFGHIKLMNPQRSTVWY'

first = ''
second = ''

for i in range(19):
    first = aa[i]
    for p in range(i+1, 20, 1):
        if not p == i: second = aa[p]
        print(first, second)

com = (1 + 19) * 19 / 2
print(f'{com:.0f}')
