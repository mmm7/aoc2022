import sys

I=[]

for line in sys.stdin:
  line = line.strip()
  if not line: continue
  l = list(line)
  I.append(set(l))
