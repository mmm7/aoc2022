from collections import Counter

from inputb import I

def v(c):
  if c.islower():
      return ord(c)-ord('a')+1
  return ord(c)-ord('A')+27

print(I)

res = 0
for x in range(0, len(I), 3):
    group = I[x:x+3]
    shared = group[0]
    shared = shared.intersection(group[1])
    shared = shared.intersection(group[2])
    shared = list(shared)
    print(x, group, shared)
    assert len(shared)==1
    res += v(shared[0])

print(res)

