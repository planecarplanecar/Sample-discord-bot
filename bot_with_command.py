import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.command
async def command(ctx):
    await ctx.send('Hello World')

#Async def command defines the command, in this case command is the thing you type in discord after the prefix (ex. !command). Await ctx.send sends hello world when the bot recieves !command.

client.run('Paste your token here')
#You have to paste your token from your bot application on the discord developer portal. Pasting this code won't work, but if you have a bot in a server, you should have an app ready.