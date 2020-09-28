

"""Importing modules required to make bot function.
Dicord is for the functions and API connection while 
re is to obtain the reg ex module needed to extract
strings within [[]] brackets"""


from random import randrange
import discord
import re as regex
import psycopg2
import math


from db_interactions_cards import pullCardRecord, pullHeroRecord, logRequest, pullFuzzyCardRecord, pullFuzzyHeroRecord, getBestHeroMatchId
from db_interactions_tournaments import createTournament, verifyTournament, registerParticipant, getTimezoneId, isRegistered, deRegister, joinTournament, hasJoined, joinBan, joinIGN, getParticipants

from construct_tables import construct_card_tables, construct_hero_tables, construct_nickname, construct_request, construct_request_type, construct_tournament
from credentials import token
from tempcode import handyman

client = discord.Client()

"""
requestTypeTuple = [
('Card Query',),
('Hero Query',),
('Help Query',),
('Fun Query',)]
"""

bot_spam_channel_id = 343233158483017748
cardbot_bugs_report_channel_id = 447437688254103552
presidental_debate_hub_id = 755917829689049208

#client.channels.get(`channelID`).send(`Text`)

help_message = "Bot Commands:\
\nUse **\[\[Card Name\]\]** to return a specific card's information. More than one card can be requested at one time.\
\nUse **\{\{Hero Name\}\}** to return a specific Hero's information. More than one Hero can be requested at one time.\
\nUse **-fuzzy** at the start of a card or Hero call to return a list of closest matches instead of a specific result.\
\nUse **-t-help** to get a list of tournament commands."

tournament_help_message = "Tournament Commands:\
\n*Use* ***-register*** *to register your name with the bot so that you can sign up for tournaments. Registration must follow the format:*\
\n-register [timezone abbreviation].\n\
\n*Once you've registered, you can use* ***-join*** *to join a tournament that hasn't started yet. Joining must follow the format:*\
\n-join (Tournament Name) [List of Hero bans seperated by a space] \"IGN\".\n\
\n*If you have the role Tournament Creators, you can use the command* ***-create-tournament*** *to create a tournament of your own. Tournament Creation must follow the format:*\
\n-tournament-create (Tournament Name) [# of Hero bans per side] OPTIONAL:<require>(this requires participants to provide an ign).\n\
\n*If you've registered as a participant with the bot and would like to remove yourself, use* ***-deregister*** *to remove your name from the registry and from any tournaments you are currently involved in.*\
\nUse **-t-examples** to see example calls of all of these commands."

example_tournament_commands = "Example Tournament Commands:\
\n**Registration:**\
\n-register [EST].\n\
\n**Joining a Tournament:**\
\n-join (The Greatest Tournament of All Time!) [RO EB Z-Mech Wall-Knight]\n\
\n**Creating a Tournament:**\
\n-tournament-create (The Greatest Tournament of All Time!) [2] <require>.\n\
\n**Deregistering:**\
\n-deregister\n\
\nUse **-t-help** to get a list of tournament commands."


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

		message_author = ""
		try:
			message_author = message.author.nickname
		except:
			message_author = message.author.name

		database_was_regenerated = await checkForRegeneration(message)
		if(database_was_regenerated):
			return

		#This is for registering your username and Timezone into cardbot
		#Ideal Input Structure:
		#-register (ign) [timezone abbreviation]
		elif message.content.startswith('-register'):
			if '[' and ']' in message.content:
				timezone = regex.findall('\[(.+?)\]', message.content)[0]

				if(isRegistered(message.author.name)):
					await message.channel.send("You are already registered.")
					return

				print('Timezone: %s' % (timezone))

				timezoneId = getTimezoneId(timezone)

				print('Timezone Id: %s' % (timezoneId))

				if(timezoneId > 0):
					confirmation_response = registerParticipant(message.author.name, timezoneId)
					await message.channel.send(confirmation_response)
				else:
					await message.channel.send("The timezone you provided wasn't recognized. Please try again.")

			else:
				await message.channel.send("Your registration command is missing [] brackets to indicate timezone.")

		elif message.content.startswith('-deregister'):
			if isRegistered(message.author.name)[0]:
				deRegister(message.author.name)
				await message.channel.send("You have been deregistered.")
			else:
				await message.channel.send("You are not currently registered.")
		
		#Ideal Input Structure:
		#-join (Tournament Name) [Hero bans] "ign"
		elif message.content.startswith('-join'):
			if isRegistered(message.author.name)[0]:	
				if '(' and ')' in message.content:
					requires_ign = False
					requires_bans = True

					tournament_name = regex.findall('\((.+?)\)', message.content)[0]

					participant_id = isRegistered(message.author.name)[1]

					print('Tournament Name: %s' % (tournament_name))

					tournament_info = verifyTournament(tournament_name)
					tournament_exists = tournament_info[0]
					tournament_id = tournament_info[1]
					number_of_hero_bans = tournament_info[2]
					tournament_needs_ign = tournament_info[3]
					print('Tournament needs ign : %s' % (tournament_needs_ign))

					if(hasJoined(participant_id, tournament_id)):
						await message.channel.send("%s, you are already registered for this tournament." % (message_author))
						return

					ign = ""
					if(tournament_needs_ign):
						requires_ign = True
						ign = regex.findall('\"(.+?)\"', message.content)[0]
						if(len(ign) > 0):
							pass
						else:
							await message.channel.send("This tournament requires an ign. Please try again.")
							return

					hero_ids = []
					if(number_of_hero_bans > 0):
						requires_bans = True
						hero_sum = []
						hero_bans = regex.findall('\[(.+?)\]', message.content)[0].split()
						print(hero_bans)
						for hero_pick in hero_bans:
							hero_ids.append(getBestHeroMatchId(hero_pick))
							hero_sum.append(1 + math.floor(getBestHeroMatchId(hero_pick) / 12))
						print(hero_sum)
						if(sum(hero_sum) == number_of_hero_bans * 3):
							pass
						else:
							await message.channel.send("This tournament requires Hero bans. Either you forgot to add them or you've made a mistake in your picks. Please try again.")
							return

					part_to_tourney_id = 0
					if(tournament_exists):
						print("That tournament exists!")
						part_to_tourney_id = joinTournament(participant_id, tournament_id)
						if(requires_bans):
							for heroid in hero_ids:
								joinBan(part_to_tourney_id, heroid)
						if(requires_ign):
							joinIGN(part_to_tourney_id, ign)
						await message.channel.send('%s has joined the tournament %s.' % (message_author, tournament_name))

					else:
						await message.channel.send("The tournament name you provided doesn't match any of the tournaments currently running.")
				else:
					await message.channel.send("Your join command is missing () brackets.")
			else:
				await message.channel.send("Please register with the bot using the command \"-register [Timezone Abbreviation]\" before joining a tournament.")

		#Ideal Input Structure:
		#-tournament-create (Tournament Name) [# of Hero bans per side] OPTIONAL: <require>
		elif message.content.startswith('-tournament-create'):
			if "pvzhu dev" in [role.name.lower() for role in message.author.roles] or "pokemod" in [role.name.lower() for role in message.author.roles]:

				if '(' and ')' and '[' and ']' in message.content:
					tournament_name = regex.findall('\((.+?)\)', message.content)[0]
					number_of_hero_bans = regex.findall('\[(.+?)\]', message.content)[0]
					require_ign = True if '<require>' in message.content else False

					successful_creation = createTournament(tournament_name, number_of_hero_bans, require_ign, message.author.name)

					if(successful_creation):
						if(require_ign):
							await message.channel.send("%s, you created a new tournament called %s with %s Hero bans per side that requires an ign." % (message_author, tournament_name, number_of_hero_bans))
						else:
							await message.channel.send("%s, you created a new tournament called %s with %s Hero bans per side that does not require an ign." % (message_author, tournament_name, number_of_hero_bans))
					else:
						await message.channel.send(message_author + ", something went wrong when creating the tournament. Please make sure to follow the format:\
								\n-tournament-create (Tournament Name) [# of Hero bans per side]")
				else:
					await message.channel.send(message_author + ", you are missing a tournament name and/or hero bans. Please make sure to follow the format:\
							\n-tournament-create (Tournament Name) [# of Hero bans per side]")
			else:
				print(message.author.roles)
				await message.channel.send("You don't have the permission to make a tournament.")

		elif message.content.startswith("-participants"):
			if '(' and ')' in message.content:

				tournament_name = regex.findall('\((.+?)\)', message.content)[0]

				returnString = "__ID__ | __NAME__ | __TIMEZONE__"
				try:
					tournament_info = verifyTournament(tournament_name)
					tournament_exists = tournament_info[0]
					tournament_id = tournament_info[1]
					number_of_hero_bans = tournament_info[2]
					tournament_needs_ign = tournament_info[3]
					tournament_creator = tournament_info[4]
				except:
					await message.channel.send("It doesn't appear there is a tournament with that name. Please try again.")
					return

				if(message.author.name == tournament_creator):
					for participant in getParticipants(tournament_id):
						returnString += "\n%s | %s | %s" % (participant[0], participant[1], participant[2])
					await message.channel.send(returnString)
				else:
					await message.channel.send("You don't have the permission to view that.")


		elif(message.content.startswith('-help')):
			logRequest(message.author.name, message.content, 3, None)
			await message.channel.send(help_message)

		elif(message.content.startswith('-t-help')):
			logRequest(message.author.name, message.content, 3, None)
			await message.channel.send(tournament_help_message)

		elif(message.content.startswith('-t-examples')):
			logRequest(message.author.name, message.content, 3, None)
			await message.channel.send(example_tournament_commands)

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
		if(len(stringInput) < 1):
			await message.channel.send("This bot call is empty, just like the promises of the other presidential candidates.")
		for text in stringInput:
			if(text == '\u2028'):
				await message.channel.send("This bot call is empty, just like the promises of the other presidential candidates.")
				return
			logRequest(message.author.name, message.content, 2, True)
			response = pullFuzzyHeroRecord(text)
			try:
				print("Channel name: %s" % (message.channel.name))
				print("Channel id: %s" % (message.channel.id))
				if(message.channel.id == bot_spam_channel_id or message.channel.id == cardbot_bugs_report_channel_id):
					await message.channel.send(response + "\n||Record generated in response to command: \{\{" + text + "\}\}||")
				else:
					await message.channel.send(response)
			except:
				await message.channel.send(response)

	if '[[' and ']]' in message.content:
		if(message.author.name == "Gking10"):
			await message.channel.send("<:weirdibh:688921196674154517>")
		stringInput = regex.findall('\[\[(.+?)\]\]', message.content)
		print(stringInput)
		if(len(stringInput) < 1):
			await message.channel.send("This bot call is empty, just like the promises of the other presidential candidates.")
		for text in stringInput:
			if(text == '\u2028'):
				await message.channel.send("This bot call is empty, just like the promises of the other presidential candidates.")
				return
			logRequest(message.author.name, message.content, 1, True)
			response = pullFuzzyCardRecord(text)
			try:
				print("Channel name: %s" % (message.channel.name))
				print("Channel id: %s" % (message.channel.id))
				if(message.channel.id == bot_spam_channel_id or message.channel.id == cardbot_bugs_report_channel_id):
					await message.channel.send(response + "\n||Record generated in response to command: \{\{" + text + "\}\}||")
				else:
					await message.channel.send(response)
			except:
				await message.channel.send(response)

async def checkForRegeneration(message):
	if(message.author.name == "Chombler"):
		if message.content.startswith("$truehandyman"):
			await message.channel.send("Chombler " + handyman(True))
			return True
		elif message.content.startswith("$handyman"):
			await message.channel.send("Chombler " + handyman(False))
			return True

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
		if(len(stringInput) < 1):
			await message.channel.send("This bot call is empty, just like the promises of the other presidential candidates.")
		for text in stringInput:
			if(text == '\u2028'):
				await message.channel.send("This bot call is empty, just like the promises of the other presidential candidates.")
				return
			logRequest(message.author.name, message.content, 2, False)
			response = pullHeroRecord(text)
			try:
				print("Channel name: %s" % (message.channel.name))
				print("Channel id: %s" % (message.channel.id))
				if(message.channel.id == bot_spam_channel_id or message.channel.id == cardbot_bugs_report_channel_id):
					await message.channel.send(response + "\n||Record generated in response to command: \{\{" + text + "\}\}||")
				else:
					await message.channel.send(response)
			except:
				await message.channel.send(response)

	if '[[' and ']]' in message.content:
		if(message.author.name == "Gking10"):
			await message.channel.send("<:weirdibh:688921196674154517>")
		stringInput = regex.findall('\[\[(.+?)\]\]', message.content)
		print("Terms input for search are: %s" % (stringInput))
		if(len(stringInput) < 1):
			await message.channel.send("This bot call is empty, just like the promises of the other presidential candidates.")
		for text in stringInput:
			if(text == '\u2028'):
				await message.channel.send("This bot call is empty, just like the promises of the other presidential candidates.")
				return
			logRequest(message.author.name, message.content, 1, False)
			response = pullCardRecord(text)
			try:
				print("Channel name: %s" % (message.channel.name))
				print("Channel id: %s" % (message.channel.id))
				if(message.channel.id == bot_spam_channel_id or message.channel.id == cardbot_bugs_report_channel_id):
					await message.channel.send(response + "\n||Record generated in response to command: \[\[" + text + "\]\]||")
				else:
					await message.channel.send(response)
			except:
				await message.channel.send(response)




client.run(token)


