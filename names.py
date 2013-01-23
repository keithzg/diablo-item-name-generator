#!/usr/bin/python

import random

adjectives =  [line.strip() for line in open('adjectives')]
nouns = [line.strip() for line in open('nouns')]
purposes = [line.strip() for line in open('purposes')]

first = random.choice(adjectives)
second = random.choice(nouns)
third = random.choice(purposes)

print first + " " + second + " of " + third

