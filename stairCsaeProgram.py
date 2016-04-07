#!/bin/python

import sys


def  StairCase(n):
    for stairs in range(1, n + 1):
        print ' ' * (n - stairs) + '#' * stairs

_n= int(raw_input());

StairCase(_n);
