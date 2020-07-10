

"""Importing modules required to make bot function.
Dicord is for the functions and API connection while 
re is to obtain the reg ex module needed to extract
strings within [[]] brackets"""

import discord
import re as regex
import psycopg2
from random import randrange

from psycopg2 import Error

from databaseinteractions import checkTable


from tables import card, cardclass, cardset, cardtoclass, cardtotrait, cardtotribe, rarity, side, trait, tribe

from dbinjections import pullCardRecord

try:
	import os
	#bot token
	token = os.environ['DISCORD_TOKEN']
except:
	from credentials import token

client = discord.Client()

florasiaPraises = {
0 : "Long Live Florasia!!",
1 : "Florasia Lives On!!",
2 : "Florasia is the Best!!",
3 : "No one can stop Florasia!!"
}

zombwanalandPraises = {
0 : "Long Live Zombwanaland!!",
1 : "Zombwanaland Lives On!!",
2 : "Zombwanaland is the Best!!",
3 : "No one can stop Zombwanaland!!"
}

panthalasaurusPraises = {
0 : "Long Live Panthalasaurus!!",
1 : "Panthalasaurus Lives On!!",
2 : "Panthalasaurus is the Best!!",
3 : "No one can stop Panthalasaurus!!"
}

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	"""if message.author == client.user:
		return"""
	if message.author.bot:
		return

	if message.content.startswith('$hello'):
		await message.channel.send('Hello!')

	if message.content.startswith('$goodbye'):
		await message.channel.send('Goodbye!')

	if message.content.startswith('$help'):
		await message.channel.send('Goodbye!')

	if message.content.startswith('$'):
		await message.channel.send('Goodbye!')

	if '[[' and ']]' in message.content:
		stringInput = regex.findall('\[\[(.+?)\]\]', message.content)
		print(stringInput)
		for text in stringInput:
			if(text.lower() == "florasia"):
				responseChoice = randrange(4)
				await message.channel.send(florasiaPraises.get(responseChoice, "Nothing to see here"))
			elif(text.lower() == "zombwanaland"):
				responseChoice = randrange(4)
				await message.channel.send(zombwanalandPraises.get(responseChoice, "Nothing to see here"))
			elif(text.lower() == "panthalasaurus"):
				responseChoice = randrange(4)
				await message.channel.send(panthalasaurusPraises.get(responseChoice, "Nothing to see here"))
			elif(text.lower() == "understandable"):
				await message.channel.send("Have a nice day")
			elif(text.lower() == "h"):
				await message.channel.send(text + " indeed")
			elif(text.lower() == "<:weirdibh:688921196674154517>"):
				await message.channel.send("<:weirdibh:688921196674154517> indeed")
			else:
				response = pullCardRecord(text)
				await message.channel.send(response)





client.run(token)