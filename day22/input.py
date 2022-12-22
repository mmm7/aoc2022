import sys

I=[]
M=[]

def pad(s,l):
    assert len(s)<=l
    return s+(' '*(l-len(s)))

longest=0
for line in sys.stdin:
  line = line.strip('\n')
  if not line: break
  longest=max(len(line), longest)
  print(len(line))
  I.append(line)

I=[pad(x, longest) for x in I]

for line in sys.stdin:
  line = line.strip()
  if not line: break
  print(line)
  s=''
  for c in line:
      if c=='L':
          if s:
              M.append(int(s))
              s=''
          M.append('L')
      elif c=='R':
          if s:
              M.append(int(s))
              s=''
          M.append('R')
      else: s=s+c
  if s: M.append(int(s))

  print(M)
