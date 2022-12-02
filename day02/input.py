import sys

I=[]

for line in sys.stdin:
  line = line.strip()
  if not line: continue
  I.append(( ord(line[0])-ord('A'), ord(line[2])-ord('X') ))
