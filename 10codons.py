#!/usr/bin/env python3

# Define Variables
dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'
s = len(dna)


# Loop
for i in range(0,s,3):
    print(dna[i:i+3])

print('End of Reading Frame')
