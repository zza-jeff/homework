#!/usr/bin/env python3

import random

trials = 10000

print(f'{"DC"}\t{"Ring"}\t{"Cloak"}')

for dc in range(1,21):
    ring = 0
    cloak = 0

    for x in range(trials):
        d = random.randint(1,20)
        d += 5
        if d >= dc: ring += 1

    for y in range(trials):
        d1 = random.randint(1,20)
        d2 = random. randint(1,20)
        if max(d1, d2) >= dc: cloak += 1
    print(f'{dc}\t{ring/trials:.4f}\t{cloak/trials:.4f}')
