from input import I

print(I)


for x in range(1,len(I)):
  s = set(I[x:x+14])
  print(s)
  if len(s)==14:
    print(x+14)
    break
