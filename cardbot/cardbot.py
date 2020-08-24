

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

		database_was_regenerated = await checkForRegeneration(message)
		if(database_was_regenerated):
			return

		if message.content.startswith('-fuzzy'):
			await fuzzySearch(message)

		elif message.content.startswith('-register'):
			if '(' and ')' and '[' and ']' and '{' and '}' in message.content:
				in_game_username = regex.findall('\((.+?)\)', message.content)
				timezone = regex.findall('\[(.+?)\]', message.content)
				hero_bans = regex.findall('\{(.+?)\}', message.content)

				print(in_game_username)
				print(timezone)
				print(hero_bans)

				if len(hero_bans) != 4:
					await message.channel.send("You entered an incorrect number of Hero Bans. Please try again.")
					return

				#Plant Heroes have a Hero Side value of 0, while Zombie Heroes have a Hero Side value of 1
				#Since there should be 2 Plant Hero Bans and 2 Zombie Hero Bans, if the hero_side_counter
				#is not equal to 0, then they do not have the correct ban structure
				for hero in hero_bans:
					hero_side_counter += await determineHeroSide(text)

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

		else:
			await regularSearch(message)

async def fuzzySearch(message):
	if '{{' and '}}' in message.content:
		if(message.author.name == "Gking10"):
			await message.channel.send("<:weirdibh:688921196674154517>")
		stringInput = regex.findall('\{\{(.+?)\}\}', message.content)
		print(stringInput)
		for text in stringInput:
			logRequest(message.author.name, message.content, 2, True)
			response = pullFuzzyHeroRecord(text)
			await message.channel.send(response + "\n||Record generated in response to command: -fuzzy \{\{" + text + "\}\}||")

	if '[[' and ']]' in message.content:
		if(message.author.name == "Gking10"):
			await message.channel.send("<:weirdibh:688921196674154517>")
		stringInput = regex.findall('\[\[(.+?)\]\]', message.content)
		print(stringInput)
		for text in stringInput:
			logRequest(message.author.name, message.content, 1, True)
			response = pullFuzzyCardRecord(text)
			await message.channel.send(response + "\n||Record generated in response to command: -fuzzy \[\[" + text + "\]\]||")

async def checkForRegeneration(message):
	if(message.author.name == "Chombler"):
		if message.content.startswith('$[[Regenerate Database]]'):
			await message.channel.send(message.author.name + construct_card_tables())
			return True

		elif message.content.startswith("$[[Regenerate Nickname]]"):
			construct_nickname()
			await message.channel.send(message.author.name + ", you have regenerated nickname.")
			return True

		elif message.content.startswith("$[[Regenerate Hero]]"):
			construct_hero_tables()
			await message.channel.send(message.author.name + ", you have regenerated hero.")
			return True

		elif message.content.startswith("$[[Regenerate Request]]"):
			construct_request()
			await message.channel.send(message.author.name + ", you have regenerated request.")
			return True

		elif message.content.startswith("$[[Regenerate Request Type]]"):
			construct_request_type()
			await message.channel.send(message.author.name + ", you have regenerated request_type.")
			return True
	return False


async def regularSearch(message):
	if '{{' and '}}' in message.content:
		if(message.author.name == "Gking10"):
			await message.channel.send("<:weirdibh:688921196674154517>")
		stringInput = regex.findall('\{\{(.+?)\}\}', message.content)
		print("Terms input for search are: %s" % (stringInput))
		for text in stringInput:
			logRequest(message.author.name, message.content, 2, False)
			response = pullHeroRecord(text)
			await message.channel.send(response + "\n||Record generated in response to command: \{\{" + text + "\}\}||")

	if '[[' and ']]' in message.content:
		if(message.author.name == "Gking10"):
			await message.channel.send("<:weirdibh:688921196674154517>")
		stringInput = regex.findall('\[\[(.+?)\]\]', message.content)
		print("Terms input for search are: %s" % (stringInput))
		for text in stringInput:
			logRequest(message.author.name, message.content, 1, False)
			response = pullCardRecord(text)
			await message.channel.send(response + "\n||Record generated in response to command: \[\[" + text + "\]\]||")




client.run(token)


