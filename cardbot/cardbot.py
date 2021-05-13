

"""Importing modules required to make bot function.
Dicord is for the functions and API connection while 
re is to obtain the reg ex module needed to extract
strings within [[]] brackets"""


from random import randrange
import discord
import re as regex
import psycopg2
import math

from timer import Countdown

from db_interactions_cards import pullCardRecord, pullHeroRecord, logRequest, pullFuzzyCardRecord, pullFuzzyHeroRecord, getBestHeroMatchId, registerStrength, displayBrand
from db_interactions_tournaments import createTournament, verifyTournament, registerParticipant, getTimezoneId, isRegistered, deRegister, joinTournament, hasJoined, joinBan, joinIGN, getParticipants, createMatchup, getParticipantInfo, startTournament

from construct_tables import construct_card_tables, construct_hero_tables, construct_nickname, construct_request, construct_request_type, construct_tournament
from credentials import token
from tempcode import handyman

from elo import calculateResults, applyResults, getElo, getLeaderboard

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
chombler_id = 445781406111760415
bot_id = 720763633604231209

pvzh_chat_channel_id = 285849268257030145
card_ideas_channel_id = 290316016234528769
deck_help_channel_id = 285818949457805313

debug_channels = [bot_spam_channel_id, cardbot_bugs_report_channel_id]

slow_mode_channels = [pvzh_chat_channel_id, card_ideas_channel_id, deck_help_channel_id]

pvzh_timer = Countdown()
card_ideas_timer= Countdown()
deck_help_timer = Countdown()

channel_timers = [pvzh_timer, card_ideas_timer, deck_help_timer]

help_message = "Bot Commands:\
\nUse **\[\[Card Name\]\]** to return a specific card's information. More than one card can be requested at one time.\
\nUse **\{\{Hero Name\}\}** to return a specific Hero's information. More than one Hero can be requested at one time.\
\nUse **-fuzzy** at the start of a card or Hero call to return a list of closest matches instead of a specific result.\
\nUse -help-elo to get a list of elo commands"

elo_help_message = "Bot Commands:\
\nUse **-elo \\@winner \\@loser** to report the outcome of a set.\
\nWhen you do this, the bot will reply with a message asking the loser to confirm the report.\
The loser must react to the message using ✅ in order to confirm the results.\
\nUse **-elo-score** to view your current elo score."

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

		elif(message.content.startswith('-help-elo')):
			await message.channel.send(elo_help_message)

		elif(message.content.startswith('-elo-score')):
			await message.channel.send("Your Elo Score is %s" % getElo(message.author.name), delete_after = 60)

		elif(message.content.startswith('-elo-leaderboard')):
			await message.channel.send(getLeaderboard())

		elif(message.content.startswith('-elo')):
			if 322500874486153216 in [role.id for role in message.author.roles] or message.author.id == chombler_id:
				names_mentioned = [mention.name for mention in message.mentions]
				ids_mentioned = [mention.id for mention in message.mentions]
				print("Names mentioned: %s\nIDs mentioned: %s" % (names_mentioned, ids_mentioned))
				other_name = [name for name in names_mentioned if name != message.author.name]
				other_id = [disc_id for disc_id in ids_mentioned if disc_id != message.author.id]
				if(len(names_mentioned) == 2):
					results = calculateResults(names_mentioned[0], ids_mentioned[0], names_mentioned[1], ids_mentioned[1])
					await message.channel.send(content = f"-unconfirmed\
												\nWinner: [{names_mentioned[0]}] ||{ids_mentioned[0]}|| ({results[0]} -> {results[1]})\
												\nLoser:  [{names_mentioned[1]}] ||{ids_mentioned[1]}|| ({results[2]} -> {results[3]})\
												\nReported By: [{message.author.name}] ||{message.author.id}||\
												\nMust be confirmed by: [{other_name[0]}] ||\|{other_id[0]}\|||\
												\n{} must react with ✅ to confirm these results",
												delete_after = 60)
				else:
					await message.channel.send("You need exactly two people in order to report a match", delete_after = 60)
			else:
				await message.channel.send("You must be verified in order to report matches", delete_after = 60)

		elif(message.content.startswith('-help')):
			logRequest(message.author.name, message.content, 3, None)
			await message.channel.send(help_message)

		elif(message.content.startswith('-fuzzy')):
			await fuzzySearch(message)

		else:
			await regularSearch(message)

@client.event
async def on_reaction_add(reaction, user):
	names_mentioned = regex.findall('\[(.+?)\]', reaction.message.content)
	ids_mentioned = regex.findall('\|\|(.+?)\|\|', reaction.message.content)
	is_unconfirmed_message = reaction.message.content.startswith('-unconfirmed')
	is_cardbot_author = reaction.message.author.id == bot_id

	if(is_unconfirmed_message and is_cardbot_author and reaction.emoji == '✅' and user.id == ids_mentioned[1]):
		results = applyResults(names_mentioned[0], ids_mentioned[0], names_mentioned[1], ids_mentioned[1])
		await reaction.message.edit(content = "-confirmed\
			\nWinner: [%s] (%s -> %s)\
			\nLoser:  [%s] (%s -> %s)" % (names_mentioned[0], results[0], results[1], names_mentioned[1], results[2], results[3]),
			delete_after = 600)

async def fuzzySearch(message):
	if '{{' and '}}' in message.content:
		stringInput = regex.findall('\{\{(.+?)\}\}', message.content)
		print(stringInput)
		if(len(stringInput) < 1):
			await message.channel.send("This bot call is empty, just like the promises of the other presidential candidates.")
		for text in stringInput:
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
		stringInput = regex.findall('\[\[(.+?)\]\]', message.content)
		print(stringInput)
		if(len(stringInput) < 1):
			await message.channel.send("This bot call is empty, just like the promises of the other presidential candidates.")
		for text in stringInput:
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
		stringInput = regex.findall('\{\{(.+?)\}\}', message.content)
		print("Terms input for search are: %s" % (stringInput))
		for text in stringInput:
			logRequest(message.author.name, message.content, 2, False)
			response = pullHeroRecord(text)
			try:
				if(message.channel.id in slow_mode_channels):
					print("This is a slow mode channel")
					index = slow_mode_channels.index(message.channel.id)
					if(channel_timers[index].isFinished()):
						channel_timers[index].start(30)
					else:
						await message.channel.send("Sorry, cardbot still has %s seconds left on its cooldown" % (channel_timers[index].timeRemaining()))
						return
				if(message.channel.id in debug_channels):
					await message.channel.send(response + "\n||Record generated in response to command: \{\{" + text + "\}\}||")
				else:
					await message.channel.send(response)
			except:
				await message.channel.send(response)

	if '[[' and ']]' in message.content:
		stringInput = regex.findall('\[\[(.+?)\]\]', message.content)
		print("Terms input for search are: %s" % (stringInput))
		for text in stringInput:
			logRequest(message.author.name, message.content, 1, False)
			response = pullCardRecord(text)
			try:
				if(message.channel.id in slow_mode_channels):
					print("This is a slow mode channel")
					index = slow_mode_channels.index(message.channel.id)
					if(channel_timers[index].isFinished()):
						channel_timers[index].start(30)
					else:
						await message.channel.send("Sorry, cardbot still has %s seconds left on its cooldown" % (channel_timers[index].timeRemaining()), delete_after = channel_timers[index].timeRemaining())
						return
				if(message.channel.id in debug_channels):
					await message.channel.send(response + "\n||Record generated in response to command: \[\[" + text + "\]\]||")
				else:
					await message.channel.send(response)
			except:
				await message.channel.send(response)

client.run(token)

