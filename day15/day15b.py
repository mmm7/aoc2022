from input import I

print(I)

def ran(s,b,y):
    dist=abs(s[0]-b[0])+ abs(s[1]-b[1])
    ydist=abs(y-s[1])
    rem=dist-ydist
    if rem<0: return (-1,-1)
    return (s[0]-rem, s[0]+rem)


R=4000000
for y in range(R+1):
    if y % 100000 == 0: print('==== y', y)
    x=0
    tortent = True
    while x<=R and tortent:
        tortent = False
        for s,b in I:
            r1,r2 = ran(s,b,y)
            #print(y, x, s, b, r1, r2)
            if r1<=x and x<=r2:
                x=r2+1
                tortent = True
    if x<=R: print(x,y)

