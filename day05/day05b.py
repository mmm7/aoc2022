from input import C
from input import M


print(C)
print(M)

for num,fro,to in M:
    fro=fro-1
    to=to-1
    print('==================', num, fro, to)
    print(num, fro, to)
    C[to] += C[fro][-num:]
    C[fro] = C[fro][:-num]
    print(C)

ret = ''
for cc in C:
    ret += cc[-1]

print(ret)
