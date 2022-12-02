from input import I

#print(I)

sc=0
for o,m in I:
  outcome=(6+m-o)%3
  sc += m+1
  sc += (3,6,0)[outcome]

print(sc)

###################

sc=0
for o,m in I:
  m=((o-1,o,o+1)[m])%3
  outcome=(6+m-o)%3
  #print(o,m,outcome)
  sc += m+1
  sc += (3,6,0)[outcome]

print(sc)
