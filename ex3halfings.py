#!/usr/bin/env python3

import random

trials = 10000
die = 0
revive = 0
stabilize = 0

print(f'{"Die"}\t{"Stable"}\t{"Revive"}')

for x in range(trials):
    health = 0
    fail = 0
    success = 0
    for i in range(3):
        d = random.randint(1,20)
        if d == 1: d = random.randint(1,20)
        if d == 20: health += 1
        elif 1 < d < 10: success += 1
        elif 10 <= d < 20: fail += 1
    if health == 1: revive += 1
    if fail == 3 and health == 0: die += 1
    if success == 3 and health == 0: stabilize += 1

print(f'{die/trials:.4f}\t{stabilize/trials:.4f}\t{revive/trials:.4f}')
