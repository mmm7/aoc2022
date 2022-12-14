from input import I,Y,X,FLOOR
from time import sleep

#print(I)

def prnt():
    global I
    for l in I:
        print(''.join(l))

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

print(FLOOR)

for x in range(X):
    I[FLOOR][x] = '#'

cnt = 0
while True:
    d = drop()
    if d is None: break
    x,y=d
    old = I[y][x]
    #print(cnt, d, old)
    I[y][x] = 'o'
    cnt+=1
    if y==0 and x==500: break
        
print(cnt)
