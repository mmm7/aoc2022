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

def mv(y,x,dy,dx):
    return (y+dy,x+dx)

@lru_cache(maxsize=None)
def tocheck(pos, c):
    if c==D('N'): return (mv(*pos,*D('N')), mv(*pos,*D('NE')), mv(*pos,*D('NW')))
    if c==D('S'): return (mv(*pos,*D('S')), mv(*pos,*D('SE')), mv(*pos,*D('SW')))
    if c==D('E'): return (mv(*pos,*D('E')), mv(*pos,*D('NE')), mv(*pos,*D('SE')))
    if c==D('W'): return (mv(*pos,*D('W')), mv(*pos,*D('NW')), mv(*pos,*D('SW')))
    assert False,c

assert tocheck((0,0), D('W'))==((0, -1), (-1, -1), (1, -1)), tocheck((0,0), D('W'))

@lru_cache(maxsize=None)
def adj8(y=0, x=0):
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
    @lru_cache(maxsize=None)
    def empty(pos):
        global I
        return tuple(pos) not in I

    global I, DIRS
    targ = {}
    stay = 0
    for pos in I:
        noonenear = True
        for adjpos in adj8(*pos):
            if not empty(adjpos):
                noonenear=False
                break
                #assert pos not in targ, '%s %s' % (pos, targ)
        if noonenear:
            #assert pos not in targ
            targ[pos] = [pos]
            stay += 1
            continue

        # consider moving
        cons = None
        for d in DIRS:
            allempty = True
            for delta in tocheck(pos,d):
                if not empty(delta):
                    allempty = False
                    break
            if not allempty: continue
            cons = mv(*pos,*d)
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

