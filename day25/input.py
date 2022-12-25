import sys

I=[]

D = {
        '=':-2,
        '-':-1,
        '0':0,
        '1':1,
        '2':2,}

def parse5(s):
    he=1
    res=0
    for c in reversed(s):
        res += he * D[c]
        he*=5
    return res

for line in sys.stdin:
  line = line.strip()
  if not line: continue
  I.append(parse5(line))
  print(line, I[-1])
