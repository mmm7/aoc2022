from input import I

print(I)

for x in range(len(I)):
  s = set(I[x:x+4])
  print(s)
  if len(s)==4:
    print(x+4)
    break
