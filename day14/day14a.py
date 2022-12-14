from input import I,Y,X,FLOOR
from time import sleep

#print(I)

def prnt():
    global I
    for l in I:
        print(''.join(l[490:510]))

def drop():
    global I
    x,y = 500,0
    while True:
        if I[y][x]=='~': return x,y
        if I[y+1][x]=='.':
            y+=1
            continue
        if I[y+1][x-1] in '.~':
            y+=1
            x-=1
            continue
        if I[y+1][x+1] in '.~':
            y+=1
            x+=1
            continue
        return x,y

for x in range(X):
    for y in range(Y-1,-1,-1):
        if I[y][x]!='.': break
        I[y][x]='~'

cnt = 0
while True:
    d = drop()
    if d is None: break
    x,y=d
    old = I[y][x]
    print(cnt, d, old)
    if old == '~': break
    I[y][x] = 'o'
    cnt+=1
        
