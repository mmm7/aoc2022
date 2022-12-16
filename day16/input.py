import sys

T={}
R={}

for line in sys.stdin:
  line = line.strip()
  if not line: continue
  l=line.split()
  valve=l[1]
  rate=int(l[4].split('=')[1][:-1])
  tunnels=[t.strip(',') for t in  l[9:]]
  R[valve]=rate
  T[valve]=tunnels
