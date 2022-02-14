#!/usr/bin/env python3

import random

trial = 10000

die = [random.randint(1,20) + random.randint(1,20) for i in range(trial)]

damage = sum(die) / trial
print(damage)
