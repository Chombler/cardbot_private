

"""Importing modules required to make bot function.
Dicord is for the functions and API connection while 
re is to obtain the reg ex module needed to extract
strings within [[]] brackets"""


from random import randrange
import discord
import re as regex
import psycopg2



from dbinjections import pullCardRecord, pullHeroRecord, logRequest, pullFuzzyCardRecord, pullFuzzyHeroRecord, createTournament
from construct_tables import construct_card_tables, construct_hero_tables, construct_nickname, construct_request, construct_request_type, construct_tournament
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

		#Ideal Input Structure:
		#-register (Tournament Name) [ign UTC+X] {Hero bans}
		elif message.content.startswith('-register'):
			if '(' and ')' and '[' and ']' and '{' and '}' in message.content:
				tournament_name = regex.findall('\((.+?)\)', message.content)
				ign_and_timezone = regex.findall('\[(.+?)\]', message.content)
				hero_bans = regex.findall('\{(.+?)\}', message.content)

				print(tournament_name)
				print(ign_and_timezone)
				print(hero_bans)
			else:
				await message.channel.send("Your registration command is missing a (), [], or \{\}.")

		#Ideal Input Structure:
		#-tournament-create (Tournament Name) [# of Hero bans per side]
		elif message.content.startswith('-tournament-create'):
			if "pvzhu dev" in [role.name.lower() for role in message.author.roles]:
				try:
					await message.channel.send(message.author.nickname + ", please hold. We are attempting to make a new tournament just the way you like it.")
				except:
					await message.channel.send(message.author.name + ", please hold. We are attempting to make a new tournament just the way you like it.")
				if '(' and ')' and '[' and ']' in message.content:
					tournament_name = regex.findall('\((.+?)\)', message.content)
					number_of_hero_bans = regex.findall('\[(.+?)\]', message.content)
					successful_creation = createTournament(tournament_name[0], number_of_hero_bans[0], message.author.name)

					if(successful_creation):
						try:
							await message.channel.send(message.author.nickname + " you created a new tournament called " + tournament_name + " with " + str(number_of_hero_bans) + " per side.")
						except:
							await message.channel.send(message.author.name + " you created a new tournament called " + tournament_name + " with " + str(number_of_hero_bans) + " per side.")
					else:
						try:
							await message.channel.send(message.author.nickname + ", something went wrong when creating the tournament. Please make sure to follow the format:\
								\n-tournament-create (Tournament Name) [# of Hero bans per side]")
						except:
							await message.channel.send(message.author.name + ", something went wrong when creating the tournament. Please make sure to follow the format:\
								\n-tournament-create (Tournament Name) [# of Hero bans per side]")
				else:
					try:
						await message.channel.send(message.author.nickname + ", something went wrong when creating the tournament. Please make sure to follow the format:\
							\n-tournament-create (Tournament Name) [# of Hero bans per side]")
					except:
						await message.channel.send(message.author.name + ", you are missing a name and/or hero bans. Please make sure to follow the format:\
							\n-tournament-create (Tournament Name) [# of Hero bans per side]")
			else:
				print(message.author.roles)
				await message.channel.send("You don't have the permissions to make a tournament.")

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
			await message.channel.send("PvZ Heroes Ultimate cards:\nhttps://dulst.com/pvzhu/cards")

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
			await message.channel.send("Chombler " + construct_card_tables())
			return True

		elif message.content.startswith("$[[Regenerate Nickname]]"):
			construct_nickname()
			await message.channel.send("Chombler, you have regenerated nickname.")
			return True

		elif message.content.startswith("$[[Regenerate Hero]]"):
			construct_hero_tables()
			await message.channel.send("Chombler, you have regenerated hero.")
			return True

		elif message.content.startswith("$[[Regenerate Request]]"):
			construct_request()
			await message.channel.send("Chombler, you have regenerated request.")
			return True

		elif message.content.startswith("$[[Regenerate Request Type]]"):
			construct_request_type()
			await message.channel.send("Chombler, you have regenerated request_type.")
			return True

		elif message.content.startswith("$[[Regenerate Tournament]]"):
			construct_tournament()
			await message.channel.send("Chombler, you have regenerated tournament.")
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


