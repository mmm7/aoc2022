from input import N,C

print(N)
print(C)

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


while True:
    if 'root' in N:
        print(N['root'])
        break
    newC = {}
    for name, comp in C.items():
        n1, oper, n2 = comp
        if n1 in N and n2 in N:
            N[name] = compute(N[n1],oper,N[n2])
        else:
            newC[name] = comp
    C = newC

