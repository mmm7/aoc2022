import sys

N={}
C={}

for line in sys.stdin:
  line = line.strip()
  if not line: continue
  name, comp = line.split(': ')
  c = comp.split()
  assert len(c)==1 or len(c)==3, str(c)
  if len(c) == 1:
      N[name] = int(c[0])
      continue
  C[name] = (c[0], c[1], c[2])

