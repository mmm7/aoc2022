import sys

I=[]

for line in sys.stdin:
  line = line.strip()
  if not line: continue
  l = list(line)
  n = len(l)//2
  I.append((set(l[0:n]), set(l[n:])))
