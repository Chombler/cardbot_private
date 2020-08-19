

"""Importing modules required to make bot function.
Dicord is for the functions and API connection while 
re is to obtain the reg ex module needed to extract
strings within [[]] brackets"""


from random import randrange
import discord
import re as regex
import psycopg2



from dbinjections import pullCardRecord, pullHeroRecord, logRequest, pullFuzzyCardRecord, pullFuzzyHeroRecord
from construct_tables import construct_card_tables, construct_hero_tables, construct_nickname, construct_request, construct_request_type
from credentials import token

client = discord.Client()

"""
requestTypeTuple = [
('Card Query',),
('Hero Query',),
('Help Query',),
('Fun Query',)]
"""


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	"""if message.author == client.user:
		return"""
	if(message.author.bot or message.content.startswith('-ignore')):
		pass
	else:

		if message.content.startswith('-fuzzy'):
			await fuzzySearch(message)

		elif(message.content.startswith('-help')):
			logRequest(message.author.name, message.content, 3, None)
			await message.channel.send("Bot Commands:\
				\nUse \[\[Card Name\]\] to return a specific card's information. More than one card can be requested at one time.\
				\nUse \{\{Hero Name\}\} to return a specific Hero's information. More than one Hero can be requested at one time.\
				\nUse -fuzzy at the start of a card or Hero call to return a list of closest matches instead of a specific result.\
				\nUse -echo at the start of a message to have the bot echo it.")

		elif(message.content.startswith('-echo')):
			logRequest(message.author.name, message.content, 4, None)
			await message.channel.send(message.content[5:] + " indeed")

		elif(message.content.startswith('-ultimate')):
			await message.channel.send("PvZ Heroes Ultimate card sheet:\nhttps://docs.google.com/spreadsheets/d/1CKrYbWVdZMW4kQvTMsNgPB2YsUDz_mBnsR7J60hNp-U/edit?usp=sharing")

		elif(message.content == 'WITNESS ME!'):
			logRequest(message.author.name, message.content, 4, None)
			await message.channel.send("WITNESSED!")
			
		else:
			if '{{' and '}}' in message.content:
				stringInput = regex.findall('\{\{(.+?)\}\}', message.content)
				print(stringInput)
				for text in stringInput:
					logRequest(message.author.name, message.content, 2, False)
					response = pullHeroRecord(text)
					await message.channel.send(response + "\n||Record generated in response to command: \{\{" + text + "\}\}||")

			if '[[' and ']]' in message.content:
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

					elif(text == "Regenerate Request"):
						if(message.author.name == "Chombler"):
							if message.content.startswith('$'):
								construct_request()
								await message.channel.send(message.author.name + ", you have regenerated request.")
							else:
								await message.channel.send(message.author.name + ", that was the wrong input.")
						else:
							await message.channel.send("<:forgetthis:592554507766857731> Nice try " + message.author.name)

					elif(text == "Regenerate Request Type"):
						if(message.author.name == "Chombler"):
							if message.content.startswith('$'):
								construct_request_type()
								await message.channel.send(message.author.name + ", you have regenerated request_type.")
							else:
								await message.channel.send(message.author.name + ", that was the wrong input.")
						else:
							await message.channel.send("<:forgetthis:592554507766857731> Nice try " + message.author.name)

					else:
						logRequest(message.author.name, message.content, 1, False)
						response = pullCardRecord(text)
						await message.channel.send(response + "\n||Record generated in response to command: \[\[" + text + "\]\]||")

async def fuzzySearch(message):
	if '{{' and '}}' in message.content:
		stringInput = regex.findall('\{\{(.+?)\}\}', message.content)
		print(stringInput)
		for text in stringInput:
			logRequest(message.author.name, message.content, 2, True)
			response = pullFuzzyHeroRecord(text)
			message.channel.send(response + "\n||Record generated in response to command: -fuzzy \{\{" + text + "\}\}||")

	if '[[' and ']]' in message.content:
		stringInput = regex.findall('\[\[(.+?)\]\]', message.content)
		print(stringInput)
		for text in stringInput:
			logRequest(message.author.name, message.content, 1, True)
			response = pullFuzzyCardRecord(text)
			message.channel.send(response + "\n||Record generated in response to command: -fuzzy \[\[" + text + "\]\]||")





client.run(token)


