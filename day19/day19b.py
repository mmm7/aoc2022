from input import I
import numpy as np
from functools import lru_cache

@lru_cache(maxsize=None)
def canafford(minerals, cost):
    return min(np.subtract(minerals, cost))>=0
assert canafford((1,2,3),(1,2,3))==True
assert canafford((1,2,3),(1,1,1))==True
assert canafford((1,2,3),(0,3,0))==False
assert canafford((1,2,3),(0,1,4))==False

@lru_cache(maxsize=None)
def add(aa,bb):
    return tuple(np.add(aa,bb))
assert add((1,2,3), (1,2,4))==(2,4,7)
assert add((0,1,0), (1,2,4))==(1,3,4)
assert add((0,-1,0), (1,2,4))==(1,1,4)


@lru_cache(maxsize=None)
def sub(aa,bb):
    return tuple(np.subtract(aa,bb))
assert sub((1,2,3), (1,2,4))==(0,0,-1)
assert sub((0,1,0), (1,2,4))==(-1,-1,-4)
assert sub((0,-1,0), (1,2,4))==(-1,-3,-4)

def dropoverload(aa, bb):
    return tuple(np.minimum(aa,bb))
assert dropoverload((1,2,3), (1,2,4))==(1,2,3), dropoverload((1,2,3), (1,2,4))

def solvefor(blueprint, t):
    maxneeded=tuple([max(i[ore] for i in blueprint) for ore in range(3)]+[99999999999999])
    print('maxneeded=', maxneeded)

    best=0

    @lru_cache(maxsize=None)
    def f(robots, minerals, exclude, t):
        nonlocal best
        nonlocal blueprint
        nonlocal maxneeded
        cachesize = f.cache_info().currsize
        if cachesize % 1000000 ==1:
            print(cachesize)
        if minerals[3] > best:
            best = minerals[3]
            print(best, t, robots, minerals, cachesize)
        if t==0: return
        if minerals[3]+sum(range(robots[3], robots[3]+t))<best: return
        newminerals=dropoverload([t*i for i in maxneeded], minerals)
        if newminerals != minerals:
            return f(robots, newminerals, exclude, t)

        newexclude = list(exclude)
        for i,cost in reversed(list(enumerate(blueprint))):
            #print(i,cost)
            if not canafford(minerals, cost): continue
            if exclude[i]: continue
            if robots[i]>= maxneeded[i]: continue
            newexclude[i] = True
            remain = add(sub(minerals,cost), robots)
            newrobots = list(robots)
            newrobots[i] += 1
            f(tuple(newrobots), remain, (False,False,False,False), t-1)
        f(robots, add(minerals, robots), tuple(newexclude), t-1)

    f((1,0,0,0), (0,0,0,0), (False,False,False,False), t)
    return best
 
for b in I:
    print(b)

ans = 1
for i,B in enumerate(I[:3]):
    print('-----------', B)
    print(list(map(max, B)))
    print(max(i[0] for i in B))
    print(max(i[1] for i in B))
    print(max(i[2] for i in B))
    print(max(i[3] for i in B))

    res = solvefor(B,32)
    ans *= res
    print(i, res, ans)

print("B:", ans)
