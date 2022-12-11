import sys
import re

I=[]

items, mul, add, test, tt, tf = [], 1, 0, 0, 0, 0

for line in sys.stdin:
  line = line.strip()
  if not line:
      I.append([items, (mul, add), (test, tt, tf)])
      items, mul, add, test, tt, tf = [], 1, 0, 0, 0, 0
  if line.startswith('Starting'):
      items = list(map(int, line.split(':')[1].split(',')))
  if line.startswith('Operation: new = old +'):
      l = line.split('+')[1].strip()
      if l == 'old': add = None
      else: add = int(l)
  if line.startswith('Operation: new = old *'):
      l = line.split('*')[1].strip()
      if l == 'old': mul = None
      else: mul = int(l)
  if line.startswith('Test: divisible by'):
      test = int(line.split()[-1])
  if line.startswith('If true'):
      tt = int(line.split()[-1])
  if line.startswith('If false'):
      tf = int(line.split()[-1])



I.append([items, (mul, add), (test, tt, tf)])

