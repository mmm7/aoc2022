from input import R,T
from functools import lru_cache
import time

print(R)
print(T)

BEST={}

def totalrate(nyitva):
    return sum(map(lambda f : R[f], list(nyitva)))

@lru_cache(maxsize=None)
def best(nyitva, t, hol, curr):
    #print('best', nyitva, t, hol)
    #time.sleep(1)
    if t==26:
        BEST[nyitva] = max(BEST.get(nyitva, 0), curr)
        return 0
    options=[]
    if len(nyitva) == len(T):
        options.append(best(nyitva,t+1, hol))
    else:
        if hol not in nyitva and R.setdefault(hol, 0)>0:
            ujnyitva = set(nyitva)
            ujnyitva.add(hol)
            options.append(best(tuple(sorted(list(ujnyitva))), t+1, hol, curr+totalrate(nyitva)))
        for hova in T[hol]:
            #print('goto:', hova)
            options.append(best(nyitva, t+1, hova, curr+totalrate(nyitva)))
    return totalrate(nyitva)+max(options)


print(best(tuple([]), 0, 'AA', 0))
print(len(BEST))

print("A:", max(BEST.values()))


best=0
for k1,v1 in BEST.items():
    for k2,v2 in BEST.items():
        if not set(k1).intersection(set(k2)):
            if v1+v2 > best:
                best=v1+v2
                print(k1, v1, '|||', k2, v2)

print("B:", best)

