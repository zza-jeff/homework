#!/usr/bin/env python3

import random

trials = 10000

print(f'{"DC"}\t{"Normal"}\t{"Adv"}\t{"Disadv"}')

for dc in range(1,21):
    normal = 0
    adv = 0
    disadv = 0

    for i in range(trials):
        d1 = random.randint(1,20)
        d2 = random. randint(1,20)
        if d1 >= dc: normal += 1
        if max(d1, d2) >= dc: adv += 1
        if min(d1, d2) >= dc: disadv += 1
    print(f'{dc}\t{normal/trials:.4f}\t{adv/trials:.4f}\t{disadv/trials:.4f}')
