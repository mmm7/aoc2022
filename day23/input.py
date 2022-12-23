import sys

I=[]

for y,line in enumerate(sys.stdin):
  line = line.strip()
  if not line: break
  for x,c in enumerate(line):
      if c=='#': I.append((y,x))
