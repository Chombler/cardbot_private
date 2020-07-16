

"""Importing modules required to make bot function.
Dicord is for the functions and API connection while 
re is to obtain the reg ex module needed to extract
strings within [[]] brackets"""

import discord
import re as regex
import psycopg2
from random import randrange

from dbinjections import pullCardRecord, pullHeroRecord

from credentials import token
from construct_tables import construct_card_tables, construct_hero_tables, construct_nickname

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
		pass
	else:
		if(message.content.startswith('-help')):
			await message.channel.send("Bot Commands:\nUse [[Card Name]] to return a specific card's information. More than one card can be requested at one time.\nUse{Hero Name} to return a specific Hero's information. More than one can be requested at one time.")
		elif '{' and '}' in message.content:
			stringInput = regex.findall('\{(.+?)\}', message.content)
			print(stringInput)
			for text in stringInput:
				response = pullHeroRecord(text)
				await message.channel.send(response)
		elif '[[' and ']]' in message.content:
			stringInput = regex.findall('\[\[(.+?)\]\]', message.content)
			print(stringInput)
			for text in stringInput:
				if(text == "Regenerate Database"):
					if(message.author.name == "Chombler"):
						if message.content.startswith('$'):
							await message.channel.send(message.author.name + construct_card_tables())
						else:
							await message.channel.send(message.author.name + ", that was the wrong input.")
					else:
						await message.channel.send("<:forgetthis:592554507766857731> Nice try " + message.author.name)
				elif(text == "Regenerate Nickname"):
					if(message.author.name == "Chombler"):
						if message.content.startswith('$'):
							construct_nickname()
							await message.channel.send(message.author.name + ", you have regenerated nickname.")
						else:
							await message.channel.send(message.author.name + ", that was the wrong input.")
					else:
						await message.channel.send("<:forgetthis:592554507766857731> Nice try " + message.author.name)
				elif(text == "Regenerate Hero"):
					if(message.author.name == "Chombler"):
						if message.content.startswith('$'):
							construct_hero_tables()
							await message.channel.send(message.author.name + ", you have regenerated hero.")
						else:
							await message.channel.send(message.author.name + ", that was the wrong input.")
					else:
						await message.channel.send("<:forgetthis:592554507766857731> Nice try " + message.author.name)
				elif(text.lower() == "florasia"):
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
				else:
					response = pullCardRecord(text)
					await message.channel.send(response)
		elif(message.content.startswith('-echo')):
			await message.channel.send(message.content[5:] + " indeed")





client.run(token)


