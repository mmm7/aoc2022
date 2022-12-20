from input import I

NUM=811589153

I = [(i,x*811589153) for i,x in enumerate(I)]
print(I)
L=len(I)
print(L)


for _ in range(10):
    for num in range(L):
        for i in range(L):
            if I[i][0]==num: break
        x = I[i][1]
        elem = I.pop(i)
        newpos = (i+x) % (L-1)
        I.insert(newpos,elem)
        #print(x,i,newpos,I)

print(x,i,newpos,I)

for zero in range(L):
    if I[zero][1] == 0: break
px,py,pz = (zero+1000)%L, (zero+2000)%L, (zero+3000)%L
x,y,z = I[px][1], I[py][1], I[pz][1]
print(px,py,pz)
print(x,y,z)
print(x+y+z)
