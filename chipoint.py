import json
import datetime

a = json.loads(open('c:\\saga\\buildpointus.json').read())

c ={}

for x in a:
	for y in list(x.keys()):
		c[x[y][2]]=[y,x[y][1]]

l = []

for x in list(c.keys()):
	if x: l.append(x)

l.sort()

dl = []

for x in l: 
	if c[x][1]>str(datetime.date.today()):
		dl.append([x,c[x][0],c[x][1]])
		print(x,c[x])		

d = ''

for x in dl:
	d = d+str(x[0])+','+x[1]+','+x[2]+'\n'

r = open('c:\\saga\\divexpointus.csv','w')
r.write(d)
r.close()
