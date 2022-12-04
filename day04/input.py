import sys

I=[]

def parse(s):
  return tuple(map(int, s.split('-')))

for line in sys.stdin:
  line = line.strip()
  if not line: continue
  l = line.split(',')
  I.append(tuple(map(parse, l)))

