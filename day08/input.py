import sys

I=[]

for line in sys.stdin:
  line = line.strip()
  if not line: continue
  I.append(list(map(int,list(line))))
