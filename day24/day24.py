from input import B,X,Y,ENTRY,EXIT
from collections import defaultdict
from time import sleep

print(B)
print(X,Y,ENTRY,EXIT)

def dirchar(di):
    y,x = di
    if (y,x) == (1,0): return 'v'
    if (y,x) == (-1,0): return '^'
    if (y,x) == (0,1): return '>'
    if (y,x) == (0,-1): return '<'
    assert False, di

def moveblizzards(B):
    global X,Y
    res = defaultdict(list)
    for oldpos,bs in B.items():
        for b in bs:
            res[((oldpos[0]+b[0])%Y, (oldpos[1]+b[1])%X)].append(b)
    return res

def printb(B,poss):
    global X,Y
    for y in range(Y):
        li=''
        for x in range(X):
            if (y,x) not in B:
                if (y,x) in poss: li+='E'
                else: li+='.'
            else:
                assert (y,x) not in poss
                bs = B[(y,x)]
                if len(bs)>1:
                    li+=str(len(bs))
                    continue
                li += dirchar(bs[0])
        print(li)

def candidates(pos):
    assert len(pos)==2, pos
    return (
            (pos[0], pos[1]),
            (pos[0]+1, pos[1]),
            (pos[0]-1, pos[1]),
            (pos[0], pos[1]+1),
            (pos[0], pos[1]-1),
            )

assert (8,4) in candidates((7,4))
assert (7,4) in candidates((7,4))
assert (6,4) in candidates((7,4))
assert (7,3) in candidates((7,4))
assert (7,5) in candidates((7,4))

n = 0
poss={(-1,ENTRY)}
while True:
    n+=1
    print('==========================', n, len(poss))
    B=moveblizzards(B)
    newposs = {(-1, ENTRY)}
    for pos in poss:
        for y,x in candidates(pos):
            if y==Y and x==EXIT:
                print("A:", n)
                exit(0)
            if x<0 or x>=X: continue
            if y<0 or y>=Y: continue
            if (y,x) in B: continue
            newposs.add((y,x))
    poss = newposs
    #printb(B,poss)
    #sleep(1)

