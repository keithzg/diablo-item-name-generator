#!/usr/bin/python

import random

adjective = ['magnificent', 'evil', 'cynical', 'broken', 'irritating', 'hearty', 'infernal', 'fluctuating', 'sacred', 'doomed', 'miserly', 'leeching', 'angelic', 'tumultuous', 'woeful', 'despairing', 'merciful', 'frail', 'flaming', 'pious', 'budget', 'crustaceous', 'brusque', 'choleric', 'irascible', 'saturnine', 'gruff', 'impetuous', 'feline', 'blighted', 'mischevious', 'malignant', 'gay', 'gainly', 'gangrenous', 'baleful', 'vicious', 'cursed']
noun = [ 'eye', 'helm', 'rod', 'bell', 'polearm', 'axe', 'bow', 'quiver', 'staff', 'blade', 'targe', 'scythe', 'halberd']
purpose = ['splendor', 'magnificence', 'keening', 'reaming', 'the monkey', 'spiritual awakening', 'frugality', 'the bear', 'the bat', 'the rhino', 'laceration', 'woe', 'despair', 'allotment', 'mercy', 'verisimilitude', 'piety', 'bludgeoning', 'gangrene', 'bane']

first = random.choice(adjective)
second = random.choice(noun)
third = random.choice(purpose)

print first + " " + second + " of " + third

