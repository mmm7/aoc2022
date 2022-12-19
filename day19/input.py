import sys

I=[]
s=1

for line in sys.stdin:
  line = line.strip()
  if not line: continue
  print(line)
  b,desc = line.split(':')
  ds=desc.split('.')
  print(ds)
  item = []
  for d in ds:
      if not d: continue
      target, source = d.split(' robot costs ')
      print(target, '<-', source)
      ss = source.split(' and ')
      itemsource={}
      for s in ss:
          s = s.strip('.')
          itemsource[s.split()[1]] = int(s.split()[0])
      item.append((
          itemsource.get('ore',0),
          itemsource.get('clay',0),
          itemsource.get('obsidian',0),
          itemsource.get('geode',0),
          ))

  I.append(item)
