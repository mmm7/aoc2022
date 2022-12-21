from input import N,C

print(N)
print(C)

del N['humn']

def compute(n1, oper, n2):
    if oper == '+':
        return float(n1) + float(n2)
    if oper == '-':
        return float(n1) - float(n2)
    if oper == '*':
        return float(n1) * float(n2)
    if oper == '/':
        return float(n1) / float(n2)
    assert False, '%s,%s,%s' % (n1, oper, n2)

F={'humn': 'humn'}
a,oper,b = C['root']
C['root'] = (a, '=', b)

while True:
    if 'root' in F:
        print(F['root'])
        break
    newC = {}
    for name, comp in C.items():
        n1, oper, n2 = comp
        if n1 in N and n2 in N:
            N[name] = compute(N[n1],oper,N[n2])
        elif n1 in F and n2 in N:
            F[name] = '(%s)%c%s' % (F[n1],oper,N[n2])
        elif n1 in N and n2 in F:
            F[name] = '%s%c(%s)' % (N[n1],oper,F[n2])
        elif n1 in F and n2 in F:
            F[name] = '(%s)%c(%s)' % (F[n1],oper,F[n2])
        else:
            newC[name] = comp
    C = newC

