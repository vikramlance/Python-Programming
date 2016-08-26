'''
https://www.hackerrank.com/challenges/calendar-module
'''

import datetime

k=raw_input()

p= datetime.datetime.strptime(k, '%m %d %Y').strftime('%A')

print p.upper()
