import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

client.run('Paste your token here')
#You have to paste your token from your bot application on the discord developer portal. Pasting this code won't work, but if you have a bot in a server, you should have an app ready.