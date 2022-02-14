#!/usr/bin/env python3

import random

trial = 10000

die = []
die1 = []
die2 = []


for i in range(trial):
    d1 = random.randint(1,8)
    if 1 <= d1 <= 6: d1 = random.randint(1,8)
    die.append(d1)

for x in range(trial):
    d2 = random.randint(1,8)
    if 1 <= d2 <= 3: d2 = random.randint(1,8)
    die1.append(d2)

for z in range(1,9):
    for y in range(trial):
        d3 = random.randint(1,8)
        if 1 <= d3 <= z: d3 = random.randint(1,8)
        die2.append(d3)

jorg = sum(die) / trial
gastin = sum(die1) /trial
fullset = [sum(die2[i:i+trial]) / trial for i in range(0, trial * 7 +1, trial)]
print(jorg, gastin)
print()
print(f'{"All Possibility:"}')
print(f'{"Avg"}\t{fullset}')
