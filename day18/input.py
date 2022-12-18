import sys

I=set()

for line in sys.stdin:
  line = line.strip()
  if not line: continue
  I.add(tuple( map(int, line.split(',')) ))
