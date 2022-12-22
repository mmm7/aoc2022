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
    yy,xx,ff=y,x,f
    yy=(yy+f[0])%YL
    xx=(xx+f[1])%XL
    if I[yy][xx]!=' ': return yy,xx,ff
    if f==(1,0):
        if x<50:
            assert yy==0, '%d.%d.%s'%(y,x,str(f))
            return 0, xx+100, (1,0)
        if x<100:
            assert yy==150, '%d.%d.%s'%(y,x,str(f))
            return 150+xx-50, 49, (0,-1)
        if x<150:
            assert yy==50, '%d.%d.%s'%(y,x,str(f))
            return 50+xx-100, 99, (0,-1)
        assert False, '%d.%d.%s'%(y,x,str(f))
    if f==(-1,0):
        if x<50:
            assert yy==99, '%d.%d.%s'%(y,x,str(f))
            return 50+xx, 50, (0,1)
        if x<100:
            assert yy==199, '%d.%d.%s'%(y,x,str(f))
            return 150+xx-50, 0, (0,1)
        if x<150:
            assert yy==199, '%d.%d.%s'%(y,x,str(f))
            return 199, xx-100, (-1,0)
        assert False, '%d.%d.%s'%(y,x,str(f))
    if f==(0,-1):
        if y<50:
            assert xx==49, '%d.%d.%s'%(y,x,str(f))
            return 149-yy, 0, (0,1)
        if y<100:
            assert xx==49, '%d.%d.%s'%(y,x,str(f))
            return 100, yy-50, (1,0)
        if y<150:
            assert xx==149, '%d.%d.%s'%(y,x,str(f))
            return 49-(yy-100), 50, (0,1)
        if y<200:
            assert xx==149, '%d.%d.%s'%(y,x,str(f))
            return 0, yy-100, (1,0)
        assert False, '%d.%d.%s'%(y,x,str(f))
    if f==(0,1):
        if y<50:
            assert xx==0, '%d.%d.%s'%(y,x,str(f))
            return 149-yy, 99, (0,-1)
        if y<100:
            assert xx==100, '%d.%d.%s'%(y,x,str(f))
            return 49, 100+yy-50, (-1,0)
        if y<150:
            assert xx==100, '%d.%d.%s'%(y,x,str(f))
            return 49-(yy-100), 149, (0,-1)
        if y<200:
            assert xx==50, '%d.%d.%s'%(y,x,str(f))
            return 149, 50+yy-150, (-1,0)
        assert False, '%d.%d.%s'%(y,x,str(f))
    return y,x,f

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
            yy,xx,ff = move(y,x,f)
            assert I[yy][xx]!=' ', '%d.%d.%s'%(yy,xx,str(ff))
            if I[yy][xx]=='#': break
            y,x,f=yy,xx,ff
    else: f=turn(f,ac)

print('=================',y,x,f, ac)
print('A:',1000*(y+1) + 4*(x+1) + fval(f))
