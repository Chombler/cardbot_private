

"""Importing modules required to make bot function.
Dicord is for the functions and API connection while 
re is to obtain the reg ex module needed to extract
strings within [[]] brackets"""

import discord
import re as regex
import psycopg2

from psycopg2 import Error

from databaseinteractions import checkTable

from credentials import token, db_credentials

from tables import card, cardclass, cardset, cardtoclass, cardtotrait, cardtotribe, rarity, side, trait, tribe

from dbinjections import pullCardRecord

client = discord.Client()


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

	if message.content.startswith('$c'):
		checkTable()
		await message.channel.send('Table checked!')

	if '[[' and ']]' in message.content:
		text = regex.search('\[\[(.+?)\]\]', message.content)
		print(text)
		response = pullCardRecord(text.group(1))
		await message.channel.send(response)





client.run(token)