import sys

I=[]

def parse(s):
  return tuple(map(int, s.split('-')))

I={'/': {}}
pwd = ['/']
cur = []

for line in sys.stdin:
  line = line.strip()
  if not line: continue
  if line.startswith('$'):
     #print('=====>', I)
     #print(pwd, cur, line)
     l = line.split(' ')[1:]
     if l[0] == 'cd':
         if l[1] == '/': pwd = ['/']
         elif l[1] == '..': pwd.pop()
         else: pwd.append(l[1])
     elif l[0] == 'ls':
         cur = I
         for d in pwd:
             cur = cur[d]
  else:
      l = line.split(' ')
      if l[0]=='dir':
          cur[l[1]]={}
      else:
          cur[l[1]]=int(l[0])

