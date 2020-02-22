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

@bot.command(name="kick", pass_context=True)
async def _kick(ctx, user: discord.Member = None, *, arg = None):
    if ctx.author.guild_permissions.kick_members == True:
        if user is None:
            await ctx.send(":thonk: Provide a user to kick.")    
            return False
        if arg is None:
            await ctx.send(":reason: I need a reason to ban: **{}**".format(user.name))
            return False
        reason = arg
        author = ctx.author
        await user.kick()
        embed = discord.Embed(title=":done: Successfully Kicked!", description=" ", color=0x00ff00)
        embed.add_field(name="User: ", value="<@{}>".format(user.id), inline=False)
        embed.add_field(name="Moderator: ", value="{}".format(author.mention), inline=False)
        embed.add_field(name="Reason: ", value="{}\n".format(arg), inline=False)
        embed.set_image(url=random.choice(['https://media.giphy.com/media/m9eG1qVjvN56H0MXt8/giphy.gif', 'https://media.giphy.com/media/UrcXN0zTfzTPi/giphy.gif', 'https://media.giphy.com/media/7DzlajZNY5D0I/giphy.gif']))
        await ctx.send(embed=embed)
    else:
        await ctx.send("You Don't have Permissions!")
