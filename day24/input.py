import sys
from collections import defaultdict

B=defaultdict(list)
X=None
Y=0
ENTRY=None
EXIT=None

def blizdir(c):
    if c == 'v': return (1,0)
    if c == '^': return (-1,0)
    if c == '<': return (0,-1)
    if c == '>': return (0,1)
    assert False, c

for l in sys.stdin:
  l = l.strip()
  if not l: continue
  if l.count('#') == len(l)-1:
      pos = l.find('.')
      if ENTRY is None:
          ENTRY=pos-1
          print('ENTRY:', ENTRY)
      else:
          assert EXIT is None
          EXIT=pos-1
          print('EXIT:', EXIT)
          break
      continue
  assert l[0]=='#', l
  assert l[-1]=='#', l
  l = l[1:-1]
  for x,c in enumerate(l):
      if c == '.': continue
      B[(Y,x)].append(blizdir(c))
  X=len(l)
  Y+=1
