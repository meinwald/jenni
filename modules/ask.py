#!/usr/bin/env python
"""
ask.py - Ask Module
Copyright 2011, Michael Yanovich, yanovich.net
Licensed under the Eiffel Forum License 2.

More info:
 * Jenni: https://github.com/myano/jenni/
 * Phenny: http://inamidst.com/phenny/
"""

import random

random.seed()


def ask(jenni, input):
    """.ask <item1> or <item2> or <item3> - Randomly picks from a set of items seperated by ' or '."""

    choices = input.group(2)

    if choices == None:
        jenni.reply("There is no spoon! Please try a valid question.")
    elif choices.lower() == "what is the answer to life, the universe, and everything?":
        jenni.reply("42")
    else:
        list_choices = choices.split(" or ")
        if len(list_choices) == 1:
            jenni.say(str(input.nick) + ": " + str(random.choice(('yes', 'no'))))
        else:
            jenni.say(str(input.nick) + ": " + str(random.choice(list_choices)))
ask.commands = ['ask']
ask.priority = 'medium'
ask.example = '.ask today or tomorrow or next week'

if __name__ == '__main__':
    print __doc__.strip()
