from input import R,T
from functools import lru_cache
import time

print(R)
print(T)

BEST={}

def totalrate(nyitva):
    return sum(map(lambda f : R[f], list(nyitva)))

@lru_cache(maxsize=32)
def best(nyitva, t, hol):
    print('best', nyitva, t, hol)
    #time.sleep(1)
    if t==30: return 0
    if len(nyitva) == len(T): return (30-t)*totalrate(nyitva)
    if (nyitva,hol) in BEST and BEST[(nyitva, hol)] < t: return -10000000
    BEST[(nyitva, hol)] = t
    options=[]
    if hol not in nyitva and R.setdefault(hol, 0)>0:
        options.append(best(tuple(list(nyitva) + [hol]), t+1, hol))
    for hova in T[hol]:
        print('goto:', hova)
        options.append(best(nyitva, t+1, hova))
    return totalrate(nyitva)+max(options)


print(best(tuple([]), 0, 'AA'))
