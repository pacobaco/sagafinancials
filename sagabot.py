import discord,asyncio,os
from discord.ext import commands, tasks
from yahoofinancials import YahooFinancials
import json
from discord import Intents
from neuralintents import GenericAssistant
import requests

def opencountry():
	a=open('c:\\saga\\corporation.csv').read().split('\n')
	b=[]
	for x in a:
		c=x.split(',')
		b.append(c)
	return b	

def countryandindustry(c,i):
	o = []
	for x in b:
		if x[4]==c and x[3]==i:
			o.append(x)
	return o

def industrybycountry(i,c):
	o = []
	for x in b:
		if x[4]==c: o.append(x)
	return o

def countrybyindustry(c,i):
	o=[]
	for x in b:
		if x[3]==i: o.append(x)
	return o


b=opencountry()

#cb = GenericAssistant("c:\\saga\\arch\\intents.json")
#cb.train_model()
#cb.save_model()

client = discord.Client()
f=open("c:\\saga\\arch\\intents.json", "r")
#ins = Intents()
#json.load(f)
#client = commands.Bot(command_prefix="!", intents=ins)

@client.event
async def on_ready():  #  Called when internal cache is loaded
	print('{0.user}'.format(client))

@client.event
async def on_message(message):
	username = str(message.author).split('#')[0]
	userm = str(message.content)
	channel = str(message.channel.name)
	print(f'{username}: {userm} ({channel})')
	
	if message.author == client.user:
		return

	if message.content.startswith('$sagadog'):
		response = userm[9:]
		a=response.split('|')
		r = countryandindustry(a[0],a[1])
		p = ''
		for x in r:
			for y in x:
				p = p+y+'\t'
			p=p+'\n'
		await message.channel.send(p)

	if message.channel.name == 'general':
		if userm == 'h':
			await message.channel.send(f'Hello {userm}!')
		
		else:
			yf = YahooFinancials(userm)
			url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol='+userm+'&apikey=0L0J5NK5GLIQR3LG'
			r = requests.get(url)
			data = r.json()
			rf = data['Name']
			rg = data['Description']
			sector = data['Sector']
			industry = data['Industry']
			mcap = data['MarketCapitalization']
			b = str(yf.get_ebit())
			await message.channel.send(f'{rg}  \nsector {sector} \nindustry {industry} \nmarket capitalization {mcap}') 
client.run("LICENSEKEY")  # Starts up the bot
