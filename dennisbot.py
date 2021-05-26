import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ';')
players = {}

@client.event
async def on_ready():
    print('Dennis Bot Started')

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)
 

@client.command()
async def dennis(ctx):
    await ctx.send('Dennis! '*3)

@client.command(aliases=['hi', 'saysomething'])
async def say(ctx):
    await ctx.send('I\'m the best midlaner! bruh')

@client.command(aliases=['bruh'])
async def saybruh(ctx):
    await ctx.send(':/')

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()



client.run('ODQ2NDUwNTUwODc5MTU4MzMy.YKvsgQ.EW8H2B3PvqNgVv29fDY3qOp_-cA')