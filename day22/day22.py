from input import I,M

print(I)
print(M)

YL=len(I)
XL=len(I[0])
print(XL,YL)

def turn(d,f):
    if f=='L':
        return {
                (0,1):(-1,0),
                (0,-1):(1,0),
                (1,0):(0,1),
                (-1,0):(0,-1),
                }[d]
    if f=='R':
        return {
                (0,1):(1,0),
                (0,-1):(-1,0),
                (1,0):(0,-1),
                (-1,0):(0,1),
                }[d]
    assert False, '%s %s' % (d,f)

assert turn((0,1),'L')==(-1,0)
assert turn((0,1),'R')==(1,0)

def move(y,x,f):
    global I
    yy,xx=y,x
    while True:
        yy=(yy+f[0])%YL
        xx=(xx+f[1])%XL
        if I[yy][xx]!=' ': break
    return yy,xx

def fval(f):
        return {
                (0,1):0,
                (0,-1):2,
                (1,0):1,
                (-1,0):3,
                }[f]

y,x=0,0
f=(0,1)
while(I[y][x]!='.'): x+=1

for ac in M:
    print('=================',y,x,f, ac)
    if isinstance(ac, int):
        for i in range(ac):
            yy,xx = move(y,x,f)
            if I[yy][xx]=='#': break
            y,x=yy,xx
    else: f=turn(f,ac)

print('=================',y,x,f, ac)
print('A:',1000*(y+1) + 4*(x+1) + fval(f))
