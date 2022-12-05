import sys

C=[]
M=[]

def parse(s):
    res = []
    for x in range(1,len(s),4):
        res +=s[x]
    return res


cratess=[]
for line in sys.stdin:
    if len(line)<3: break
    cratess+=(parse(line),)

cratess.reverse()
print(cratess)

C=cratess[0]
for cs in cratess[1:]:
    for i,c in enumerate(cs):
        if c==' ': continue
        C[i] += c


for line in sys.stdin:
    line = line.strip()
    if not line: break
    ss=line.split(' ')
    M.append(tuple([int(ss[1]), int(ss[3]), int(ss[5])]))
