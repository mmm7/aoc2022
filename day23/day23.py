from input import I
from functools import lru_cache

print(I)
LEN = len(I)

@lru_cache(maxsize=None)
def D(s):
    if s=='N': return (-1,0)
    if s=='NE': return (-1,1)
    if s=='E': return (0,1)
    if s=='SE': return (1,1)
    if s=='S': return (1,0)
    if s=='SW': return (1,-1)
    if s=='W': return (0,-1)
    if s=='NW': return (-1,-1)
    assert False,s

assert D('E')==(0,1)

@lru_cache(maxsize=None)
def tocheck(c):
    if c==D('N'): return (D('N'), D('NE'), D('NW'))
    if c==D('S'): return (D('S'), D('SE'), D('SW'))
    if c==D('E'): return (D('E'), D('NE'), D('SE'))
    if c==D('W'): return (D('W'), D('NW'), D('SW'))
    assert False,c

assert tocheck(D('W'))==((0, -1), (-1, -1), (1, -1)), tocheck(D('W'))

def empty(pos):
    global I
    return (pos[0], pos[1]) not in I

@lru_cache(maxsize=None)
def adj8(pos=(0,0)):
    y,x=pos
    res=[]
    for yy in range(-1,2):
        for xx in range(-1,2):
            if yy or xx: res.append((y+yy, x+xx))
    return tuple(res)

DIRS=[D(c) for c in 'NSWE']

def rotatedirs():
    global DIRS
    DIRS = DIRS[1:]+DIRS[:1]


def round():
    global I, DIRS
    targ = {}
    stay = 0
    for pos in I:
        noonenear = True
        for adjpos in adj8(pos):
            if not empty(adjpos):
                noonenear=False
                #assert pos not in targ, '%s %s' % (pos, targ)
                break
        if noonenear:
            #assert pos not in targ
            targ[pos] = [pos]
            stay += 1
            continue

        # consider moving
        cons = None
        for d in DIRS:
            allempty = True
            for yy,xx in tocheck(d):
                if not empty((pos[0]+yy, pos[1]+xx)):
                    allempty = False
                    break
            if not allempty: continue
            cons = (pos[0]+d[0], pos[1]+d[1])
            break

        if not cons:
            #assert pos not in targ
            targ[pos] = [pos]
            stay += 1
            continue
        if cons not in targ:
            targ[cons]=[]
        targ[cons].append(pos)

    #print(targ)
    newI = []
    for k,v in targ.items():
        if len(v)==1:
            newI.append(k)
            continue
        for old in v:
            stay += 1
            newI.append(old)
    I = newI
    assert len(I)==LEN, str(I)
    return stay
        
r = 0
while True:
    print('===========================', r, DIRS)
    #print(I)
    if r==10:
        xmi = min([x for y,x in I])
        xma = max([x for y,x in I])
        ymi = min([y for y,x in I])
        yma = max([y for y,x in I])

        print(xmi,xma,ymi,yma,len(I))
        print('A:', (xma-xmi+1) * (yma-ymi+1) - LEN)

    r += 1
    stay = round()
    print(stay, '/', LEN)
    if stay == LEN:
        print('B:', r)
        break
    rotatedirs()

