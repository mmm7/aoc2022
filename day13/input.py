import sys

I=[]
A=[]

pair=[]
for line in sys.stdin:
  line = line.strip()
  if not line: continue
  A.append(eval(line))
  pair.append(eval(line))
  if len(pair)==2:
      I.append(pair)
      pair=[]
