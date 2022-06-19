from yahoofinancials import YahooFinancials
import json
import os

u = open('c:\\saga\\usstock.txt')
u = u.read().split('\n')
stocklist = ['aapl', 'mo', 'msft']
stocklist=u
symdic={}

i = open('c:\\saga\\pointus.dat')
i2 = i.read()
i.close()
kk = int(i2)


#a = open('yahoo3292022.csv')
#v = a.read().split('\n')

kkk = kk+50

if kkk>len(u): 
	kkk=len(u)
print(kkk,kk)
o=[]

q={}

for x in u[kk:kkk]:
	try:
		yf = YahooFinancials(x)
		print(x)
		print(yf.get_exdividend_date())
		print(yf.get_dividend_yield())
		q[x]=[x,yf.get_exdividend_date(),yf.get_dividend_yield()]
	except: continue

for x in list(q.keys()): print(x,q[x][0],q[x][1],q[x][2])

fname='c:\\saga\\buildpointus.json'
a = []
if not os.path.isfile(fname):
    a.append(q)
    with open(fname, mode='w') as f:
        f.write(json.dumps(a, indent=2))
else:
    with open(fname) as feedsjson:
        feeds = json.load(feedsjson)

    feeds.append(q)
    with open(fname, mode='w') as f:
        f.write(json.dumps(feeds, indent=2))


i = open('c:\\saga\\pointus.dat','w')
i2 = i.write(str(kkk))
i.close()
