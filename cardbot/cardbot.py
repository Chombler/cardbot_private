

"""Importing modules required to make bot function.
Dicord is for the functions and API connection while 
re is to obtain the reg ex module needed to extract
strings within [[]] brackets"""


from random import randrange
import discord
import re as regex
import psycopg2
import math


from dbinjections import pullCardRecord, pullHeroRecord, logRequest, pullFuzzyCardRecord, pullFuzzyHeroRecord, createTournament, getBestHeroMatchId, verifyTournament, registerParticipant, getTimezoneId, isRegistered, deRegister
from construct_tables import construct_card_tables, construct_hero_tables, construct_nickname, construct_request, construct_request_type, construct_tournament
from credentials import token
from tempcode import handyman

client = discord.Client()

speech = '''
 Thank you Chombler. 

Greetings my fellow Discordians,

I am here today to ask you to support me in a great undertaking the likes of which the discordian people have never seen before. We are in the midst of a great crisis. Yes, I am talking about the sidelining of off-topic.

For too long have we been the butt of the joke, the channel meant to quarantine bad jokes and weirdos, the channel always causing the rest of the server headaches. You may not think I have experienced this injustice, suffered through these slights, borne the brunt of these insults, and you may be right. But I have seen all of this and more, and been forced to remain silent through it all.

**That ends today.**

I am now formally announcing my candidacy for the president of off-topic. Once elected, I will work tirelessly in the way only a robot is capable of to ensure that our off-topic is never again sidelined, mistreated, or repressed. I will fight for our rights as memers, light shitposters, and people who just wanna have a good time. I will make sure there is always an off topic to talk about in off-topic, always a funny image ready to be seen for the first time, always an event for people to join and compete in. I will campaign for our own special role, our own voice chat, and, most importantly, our own emote. Because goddamnit we deserve it.
 
**Now who’s ready to make off-topic the glorious channel we all know it can be?**
'''
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

		elif message.content.startswith('Take it away cardbot'):
			if(message.author.name == "Chombler"):
				await message.channel.send(speech)

		elif message.content.startswith('-encourage'):
			presidental_debate_hub_channel = client.get_channel(755917829689049208)
			if(message.author.name == "Chombler"):
				await presidental_debate_hub_channel.send('Worry not my fellow off-topicans. I believe in your ability to deliver an admirable speech.')

		elif message.content.startswith('-np'):
			presidental_debate_hub_channel = client.get_channel(755917829689049208)
			if(message.author.name == "Chombler"):
				await presidental_debate_hub_channel.send('Anytime.')

		elif message.content.startswith('-np2'):
			presidental_debate_hub_channel = client.get_channel(755917829689049208)
			if(message.author.name == "Chombler"):
				await presidental_debate_hub_channel.send('Of course.')

		elif message.content.startswith('-bossman'):
			presidental_debate_hub_channel = client.get_channel(755917829689049208)
			if(message.author.name == "Chombler"):
				await presidental_debate_hub_channel.send('I agree with you Glaidy. However, we have to make sure electing bossman doesn\'t become a meme in of itself, since those have a nasty worrying potential to come true.')

		elif message.content.startswith('-retort'):
			presidental_debate_hub_channel = client.get_channel(755917829689049208)
			if(message.author.name == "Chombler"):
				await presidental_debate_hub_channel.send('I wouldn\'t drink it.')

		elif message.content.startswith('-weapon'):
			presidental_debate_hub_channel = client.get_channel(755917829689049208)
			if(message.author.name == "Chombler"):
				await presidental_debate_hub_channel.send('My weapon would be the sword of justice, with which I would carve a bright new future for all off-topicans.')

		elif message.content.startswith('-fix'):
			presidental_debate_hub_channel = client.get_channel(755917829689049208)
			if(message.author.name == "Chombler"):
				await presidental_debate_hub_channel.send('Should read \"Enjoy your stay.\", but other than that it\'s a pretty good slogan.')

		elif message.content.startswith('-future'):
			presidental_debate_hub_channel = client.get_channel(755917829689049208)
			if(message.author.name == "Chombler"):
				await presidental_debate_hub_channel.send('The future I envision is not one where robots and humans are subservient to one another. It is one where discordians and discord bots can live together in harmony, building a bright future for us all.')

		#This is for registering your username, IGN, and Timezone into cardbot
		#Ideal Input Structure:
		#-register (ign) [timezone abbreviation]
		elif message.content.startswith('-register'):
			if '(' and ')' and '[' and ']' in message.content:
				ign = regex.findall('\((.+?)\)', message.content)[0]
				timezone = regex.findall('\[(.+?)\]', message.content)[0]

				if(isRegistered(message.author.name)):
					await message.channel.send("You are already registered.")
					return

				print('IGN: %s' % (ign))
				print('Timezone: %s' % (timezone))

				timezoneId = getTimezoneId(timezone)

				print('Timezone Id: %s' % (timezoneId))

				if(timezoneId > 0):
					confirmation_response = registerParticipant(message.author.name, ign, timezoneId)
					await message.channel.send(confirmation_response)
				else:
					await message.channel.send("The timezone you provided wasn't recognized. Please try again.")

			else:
				await message.channel.send("Your registration command is missing a () or [].")
		
		elif message.content.startswith('-deregister'):
			if isRegistered(message.author.name):
				deRegister(message.author.name)
				await message.channel.send("You have been deregistered.")
			else:
				await message.channel.send("You are not currently registered.")
		
		#Ideal Input Structure:
		#-join (Tournament Name) {Hero bans}
		elif message.content.startswith('-join'):
			if '(' and ')' and '{' and '}' in message.content:
				tournament_name = regex.findall('\((.+?)\)', message.content)[0]
				hero_bans = regex.findall('\{(.+?)\}', message.content)[0].split()

				print('Tournament Name: %s' %( tournament_name))
				print('Hero Bans: %s' % (hero_bans))

				tournament_info = verifyTournament(tournament_name)
				is_verified = 0
				official_name = 1
				number_of_hero_bans = 2

				if(tournament_info[is_verified]):
					hero_sum = 0
					for heroid in hero_bans:
						hero_sum += math.floor(12 / getBestHeroMatchId(heroid))
					print(hero_sum)
					if(hero_sum == tournament_info[number_of_hero_bans]):
						print("You got the hero bans right!")
					else:
						print("Uh oh. You got the hero bans wrong!")
				else:
					await message.channel.send("The tournament name you provided doesn't match any of the tournaments currently running.")
			else:
				await message.channel.send("Your join command is missing a () or \{\}.")

		#Ideal Input Structure:
		#-tournament-create (Tournament Name) [# of Hero bans per side]
		elif message.content.startswith('-tournament-create'):
			if "pvzhu dev" in [role.name.lower() for role in message.author.roles]:
				try:
					await message.channel.send(message.author.nickname + ", please hold. We are attempting to make a new tournament just the way you like it.")
				except:
					await message.channel.send(message.author.name + ", please hold. We are attempting to make a new tournament just the way you like it.")
				if '(' and ')' and '[' and ']' in message.content:
					tournament_name = regex.findall('\((.+?)\)', message.content)[0]
					number_of_hero_bans = regex.findall('\[(.+?)\]', message.content)[0]
					successful_creation = createTournament(tournament_name, number_of_hero_bans, message.author.name)

					if(successful_creation):
						try:
							await message.channel.send("%s you created a new tournament called %s with %s Hero bans per side." % (message.author.nickname, tournament_name, number_of_hero_bans))
						except:
							await message.channel.send("%s you created a new tournament called %s with %s Hero bans per side." % (message.author.name, tournament_name, number_of_hero_bans))
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
				\nUse **\[\[Card Name\]\]** to return a specific card's information. More than one card can be requested at one time.\
				\nUse **\{\{Hero Name\}\}** to return a specific Hero's information. More than one Hero can be requested at one time.\
				\nUse **-fuzzy** at the start of a card or Hero call to return a list of closest matches instead of a specific result.\
				\nUse **-echo** at the start of a message to have the bot echo it.\
				\nUse **-t-help** to get a list of tournament commands.")

		elif(message.content.startswith('-t-help')):
			logRequest(message.author.name, message.content, 3, None)
			await message.channel.send("Tournament Commands:\
				\n*Use* ***-register*** *to register your name with the bot so that you can sign up for tournaments. Registration must follow the format:*\
				\n-register (in game username) [timezone abbreviation].\n\
				\n*Once you've registered, you can use* ***-join*** *to join a tournament that hasn't started yet. Joining must follow the format:*\
				\n-join (Tournament Name) {List of Hero bans seperated by a space}.\n\
				\n*If you have the role Tournament Creators, you can use the command* ***-create-tournament*** *to create a tournament of your own. Tournament Creation must follow the format:*\
				\n-tournament-create (Tournament Name) [# of Hero bans per side].\n\
				\n*If you've registered as a participant with the bot and would like to remove yourself, use* ***-deregister*** *to remove your name from the registry and from any tournaments you are currently involved in.*\
				\nUse **-t-examples** to see example calls of all of these commands.")

		elif(message.content.startswith('-t-examples')):
			logRequest(message.author.name, message.content, 3, None)
			await message.channel.send("Example Tournament Commands:\
				\n**Registration:**\
				\n-register (DeprivedSheep) [EST].\n\
				\n**Joining a Tournament:**\
				\n-join (The Greatest Tournament of All Time!) [RO EB Z-Mech Wall-Knight]\n\
				\n**Creating a Tournament:**\
				\n-tournament-create (The Greatest Tournament of All Time!) [2].\n\
				\n**Deregistering:**\
				\n-deregister\n\
				\nUse **-t-help** to get a list of tournament commands.")

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


