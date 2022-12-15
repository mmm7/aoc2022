from input import I

print(I)

ROW=2000000
ANS=[]
B=set()

for s,b in I:
    dist=abs(s[0]-b[0])+ abs(s[1]-b[1])
    print(ROW,dist)
    if b[1] == ROW: B.add(b[0])
    ydist=abs(ROW-s[1])
    rem=dist-ydist
    if rem<0: continue
    ANS.append((s[0]-rem, s[0]+rem))

ANS.sort()
print(B)
print(ANS)

cnt=0
x=ANS[0][0]
for r1,r2 in ANS:
    if r1<=x and x<=r2:
        cnt+=r2+1-x
        x=r2+1
print(cnt-len(B))


# Kézzel fejeztem be


