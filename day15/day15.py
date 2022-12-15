from input import I

print(I)

ROWS=(10, 2000000)
ANS=[[] for _ in range(len(ROWS))]
B=[set() for _ in range(len(ROWS))]

for s,b in I:
    dist=abs(s[0]-b[0])+ abs(s[1]-b[1])
    for i,row in enumerate(ROWS):
        print(i,row,dist)
        if b[1] == row: B[i].add(b[0])
        ydist=abs(row-s[1])
        rem=dist-ydist
        if rem<0: continue
        ANS[i].append((s[0]-rem, s[0]+rem))

ANS=list(map(sorted, ANS))
print(B)
print(ANS)

for i,ans in enumerate(ANS):
    print('============', i,ans)
    if len(ans) == 0: continue
    cnt=0
    secf=0
    sect=0
    start=ans[secf][0]
    while True:
        print(cnt,start,'|',secf,':',ans[secf],',',sect,':',ans[sect])
        while sect<len(ans) and ans[secf][1]>=ans[sect][1]:
            print(' ',sect,':',ans[sect])
            sect+=1
        if sect==len(ans)-1:
            cnt+=ans[-1][1]-start+1
            break
        if ans[sect][0]>ans[secf][1]:
            cnt+=ans[secf][1]-start+1
            secf=sect
            start = ans[secf][0]
            continue
        secf=sect
    print(i,cnt,B[i],cnt-len(B[i]))


# Kézzel fejeztem be


