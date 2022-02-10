#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random

people = 25 # if people = 23, P roughly equals to 0.5
same = 0
trial = 10000

for i in range(trial):
    calendar = [0] * 365
    for x in range(people):
        birth = random.randint(1, 365)
        calendar[birth - 1] += 1
    if calendar.count(1) < people: same += 1

prob = same / trial
print(f'{prob:.3f}')
