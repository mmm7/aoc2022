import sys

I=[]

def vect(d):
    if d=='R': return (+1,0)
    if d=='L': return (-1,0)
    if d=='U': return (0,-1)
    if d=='D': return (0,+1)

for line in sys.stdin:
  line = line.strip()
  if not line: continue
  d, x = line.split()
  I.append((vect(d), int(x)))
