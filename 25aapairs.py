#!/usr/bin/env python3

# Print out all the unique pairwise amino acid combinations
# AC is the same as CA
# Skip AA, CC etc.
# Also print out how many combinations there are

aa = 'ACDEFGHIKLMNPQRSTVWY'
count = 0

first = ''
second = ''

for i in range(19):
    first = aa[i]
    for p in range(i+1, 20, 1):
        second = aa[p]
        print(first, second)
        count += 1

print(f'{count:.0f}')
