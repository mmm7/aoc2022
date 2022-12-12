import sys

H={}
S=None
SS=[]
E=None
I={}

for y,line in enumerate(sys.stdin):
  line = line.strip()
  if not line: continue
  for x,c in enumerate(line):
      if c=='S':
          S=(y,x)
          c='a'
      elif c=='E':
          E=(y,x)
          c='z'
      if c=='a': SS.append((y,x))
      elev=ord(c)-ord('a')
      H[(y,x)] = elev
      print(y,x,c)

for c,e in H.items():
    y,x=c
    dest=[]
    if H.get((y-1,x), 1000)<=e+1: dest.append((y-1,x))
    if H.get((y+1,x), 1000)<=e+1: dest.append((y+1,x))
    if H.get((y,x-1), 1000)<=e+1: dest.append((y,x-1))
    if H.get((y,x+1), 1000)<=e+1: dest.append((y,x+1))
    I[(y,x)] = dest
