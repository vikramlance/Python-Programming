#!/usr/bin/env python3
import fileinput

with fileinput.FileInput(fileToSearch, inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(textToSearch, textToReplace), end='')