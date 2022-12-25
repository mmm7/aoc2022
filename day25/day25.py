from input import I

DR='012=-'

s=sum(I)
print(s)

he=1

enter=[]
while s:
    print('=================', s)
    dig=s%5
    print(dig)
    if dig>2: dig-=5
    print(dig)
    enter.append(DR[dig])
    s-=dig
    assert s%5==0, "%s | %d" %(s, dig)
    s//=5

print(''.join(reversed(enter)))

