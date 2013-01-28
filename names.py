#!/usr/bin/python

import random

adjectives =  [line.strip() for line in open('adjectives')]
nouns = [line.strip() for line in open('nouns')]
suffixes = [line.strip() for line in open('suffixes')]

first = random.choice(adjectives)
second = random.choice(nouns)
third = random.choice(suffixes)

print first + " " + second + " of " + third

