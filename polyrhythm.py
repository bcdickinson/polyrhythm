#!/usr/bin/env python
import argparse
from typing import List

BOX_H = '\u2500'
BOX_V = '\u2502'
BOX_TL = '\u250C'
BOX_TR = '\u2510'
BOX_BL = '\u2514'
BOX_BR = '\u2518'

BOX_CHARS = [
    BOX_TL, BOX_H, BOX_TR,
    BOX_V,  '',    BOX_V,  # noqa: E241
    BOX_BL, BOX_H, BOX_BR,
]


def parse_pattern(pattern_str: str) -> List[int]:
    error_msg = 'pattern must be two integers separated by a colon'
    try:
        pattern_list = [int(p) for p in pattern_str.split(':')]
    except ValueError:
        raise argparse.ArgumentTypeError(error_msg)

    if len(pattern_list) != 2:
        raise argparse.ArgumentTypeError(error_msg)

    return pattern_list


parser = argparse.ArgumentParser(description='Print out a grid for counting a polyrhythm')
parser.add_argument(
    'pattern',
    nargs=1,
    type=parse_pattern,
    help="Two integers separated by a colon representing the polyrhythm, e.g. 4:3"

)
args = parser.parse_args()
pattern = args.pattern[0]

output = ''


def put(char):
    global output
    output += str(char)


width = pattern[1] * 3
height = pattern[0] * 3

for y in range(height):
    for x in range(width):
        i = (x // 3)
        j = (y // 3)

        beat = i + (pattern[1] * j)

        p = x - (3 * i)
        q = y - (3 * j)

        cell = p + (3 * q)

        if cell == 4:
            put(i + 1)  # TODO deal with double-digit beat numbers
        elif beat % pattern[0] == 0:
            put(BOX_CHARS[cell])
        else:
            put(' ')

    put('\n')

print(output)
