from input import I
from time import sleep

print(I)

def comp(a,b):
    x=0
    while True:
        print(x, 'comp:', a,b)
        if x<len(a) and x>=len(b): return False
        if x>=len(a) and x<len(b): return True
        if x>=len(a) and x>=len(b): return None
        aa = a[x]
        bb = b[x]
        print('aa:', aa, 'bb:', bb)
        if isinstance(aa, int) and isinstance(bb, int):
            if aa<bb: return True
            if aa>bb: return False
        else:
            aaa=aa
            bbb=bb
            if isinstance(aa,int): aaa=[aa]
            if isinstance(bb,int): bbb=[bb]
            print('aaa:', aaa, 'bbb:', bb)
            res = comp(aaa,bbb)
            print('res=', res, 'aaa:', aaa, 'bbb:', bb)
            if isinstance(res, bool): return res
        x += 1


cnt=0
for i,p in enumerate(I):
    a,b=p
    print('===============', i, (a,b))
    res = comp(a,b)
    if res: cnt+=i+1
    print(i, cnt, res)

print(cnt)
