import sys

I=[]

for line in sys.stdin:
  line = line.strip()
  if not line: continue
  l=line.split('=')
  assert len(l) == 5
  sx=l[1].split(',')
  sy=l[2].split(':')
  bx=l[3].split(',')
  by=l[4]
  print(l)

  I.append(((int(sx[0]), int(sy[0])), (int(bx[0]), int(by))))

