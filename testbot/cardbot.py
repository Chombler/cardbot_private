

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
		response = get_card(text.group(1))
		await message.channel.send('%s\n%s\n%s\n%s\n%s\n%s' % 
			(response[0], response[1], response[2], 
				response[3], response[4], response[5]))


def get_card(name):
	if name == 'FMN':
		return ['FMN :Guardian:',
				'Flower Nut Plant',
				'1:Sun: 2:Strength:/1:Health:',
				'Zombie tricks cost +1:Brain:',
				'*I\'d forget my own flower if it wasn\'t stuck to my head. Wait, what were we talking about again?*',
				'Event']



client.run(token)