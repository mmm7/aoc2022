from input import I

print(I)

visible = 0
h=-1
v=-1


visible = []
for _ in range(len(I)):
    visible.append([0] * len(I[0]))

for y in range(len(I)):
    xf=0
    xt=len(I)-1
    visible[y][xf]=1
    visible[y][xt]=1
    xxf=I[y][xf]
    xxt=I[y][xt]
    while True:
        if xxf<xxt:
            xf+=1
            if (xf==xt): break 
            if I[y][xf]>xxf:
                xxf=I[y][xf]
                visible[y][xf] = 1
        else:
            xt-=1
            if (xf==xt): break 
            if I[y][xt]>xxt:
                xxt=I[y][xt]
                visible[y][xt] = 1

print(visible)
print(sum(map(sum,visible)))

for x in range(len(I)):
    yf=0
    yt=len(I)-1
    visible[yf][x]=1
    visible[yt][x]=1
    yyf=I[yf][x]
    yyt=I[yt][x]
    while True:
        if yyf<yyt:
            yf+=1
            if (yf==yt): break 
            if I[yf][x]>yyf:
                yyf=I[yf][x]
                visible[yf][x] = 1
        else:
            yt-=1
            if (yf==yt): break
            if I[yt][x]>yyt:
                yyt=I[yt][x]
                visible[yt][x] = 1

print(visible)
print(sum(map(sum,visible)))
