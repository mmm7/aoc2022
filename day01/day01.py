import sys

e=[]
c=0

for line in sys.stdin:
  l = line.strip()
  if len(l) == 0:
    e.append(c)
    c=0
  else:
    c+=int(l)

e.append(c)

print(max(e))

e.sort()

print(sum(e[-3:]))
