import discord
from discord.ext import commands
import asyncio
import os
import inspect
import time

bot = commands.Bot(command_prefix='x!')

bot.remove_command('help')

@bot.event

async def on_ready():

	print('Bot is ready')

@bot.command(pass_context=True, no_pm=True)

@commands.has_permissions(kick_members=True)

async def clean(ctx, amount=100):

	channel = ctx.message.channel

	messages = [ ]

	async for message in bot.logs_from(channel, limit=int(amount) + 1):

		messages.append(message)

	await bot.delete_messages(messages)

	await bot.say(f"{amount} message has been deleted.")

