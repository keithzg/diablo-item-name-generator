#!/usr/bin/python

import random

adjective = ['magnificent', 'evil', 'cynical', 'broken', 'irritating', 'hearty', 'infernal', 'fluctuating', 'sacred', 'doomed', 'miserly', 'leeching']
noun = [ 'eye', 'helm', 'rod', 'bell', 'polearm', 'axe', 'bow', 'quiver', 'staff']
purpose = ['splendor', 'magnificence', 'keening', 'reaming', 'the monkey', 'spiritual awakening', 'frugality', 'of the bear', 'of the bat']

first = random.choice(adjective)
second = random.choice(noun)
third = random.choice(purpose)

print first + " " + second + " of " + third

