import sys

I=[0]
s=1

for line in sys.stdin:
  line = line.strip()
  if not line: continue
  if line == 'noop':
      I.append(s)
      continue
  I.append(s)
  I.append(s)
  s+=int(line.split()[1])
