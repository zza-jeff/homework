#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change


pt = 0 # Number of GC
st = len(dna)

for i in range(st):
    nc = dna[i]
    if nc == 'G' or nc == 'C':
        pt += 1

out = pt / st # Output

# Method 1 - Old-school
print('%.2f' % (out))

# Method 2 - format()
print('{:.2f}'.format(out))

# Method 3 - f-strings
print(f'{out:.2f}')
