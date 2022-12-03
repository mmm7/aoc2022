from input import I

def v(c):
  if c.islower():
      return ord(c)-ord('a')+1
  return ord(c)-ord('A')+27

print(I)

res = 0
for a,b in I:
  shared = list(a.intersection(b))
  assert len(shared)==1
  vv = v(shared[0])
  print(shared, vv)
  res += vv

print(res)
