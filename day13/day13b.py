from input import A

from functools import cmp_to_key
print(A)

def comp(a,b):
    x=0
    while True:
        #print(x, 'comp:', a,b)
        if x<len(a) and x>=len(b): return False
        if x>=len(a) and x<len(b): return True
        if x>=len(a) and x>=len(b): return None
        aa = a[x]
        bb = b[x]
        #print('aa:', aa, 'bb:', bb)
        if isinstance(aa, int) and isinstance(bb, int):
            if aa<bb: return True
            if aa>bb: return False
        else:
            aaa=aa
            bbb=bb
            if isinstance(aa,int): aaa=[aa]
            if isinstance(bb,int): bbb=[bb]
            #print('aaa:', aaa, 'bbb:', bb)
            res = comp(aaa,bbb)
            #print('res=', res, 'aaa:', aaa, 'bbb:', bb)
            if isinstance(res, bool): return res
        x += 1

def compare(a,b):
    res=comp(a,b)
    if res is None: return 0
    if comp(a,b): return -1
    return 1

A.append([[2]])
A.append([[6]])
from functools import cmp_to_key
S=sorted(A, key=cmp_to_key(compare))
print(S)

res = 1
for i,e in enumerate(S):
    if e==[[2]] or e==[[6]]:
        print(i+1,e)
        res *= i+1

print(res)
