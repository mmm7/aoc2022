from input import I

print(I)
print(len(I))
res = 0
for l in I:
    a,b = sorted(l)
    #a,b = sorted(a), sorted(b)
    assert(len(a)==2)
    assert(len(b)==2)
    assert(a[0]<=a[1])
    assert(b[0]<=b[1])
    t = a[1]>=b[1] or a[0]==b[0]
    print(a,b,t)
    if t: res+=1

print(res)
