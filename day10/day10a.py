from input import I

print(I)

ret=0
for x in range(20,len(I),40):
    print(x,I[x])
    ret+=I[x]*x

print(ret)

pix=1
while True:
    line = ''
    for x in range(40):
        sprite = I[pix]
        pix+=1
        if abs(x-sprite)<2: line+='#'
        else: line+='.'
    print(line)

