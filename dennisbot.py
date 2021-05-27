import discord
import youtube_dl
import os
from discord.ext import commands
from discord import FFmpegPCMAudio


client = commands.Bot(command_prefix = ';')
client.remove_command("help")


@client.event
async def on_ready():
    print('Dennis Bot Started')

@client.command()
async def help(ctx):
    await ctx.send(file=discord.File('help.txt'))

@client.command()
async def echo(ctx, *args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await ctx.send(output)
 

@client.command()
async def dennis(ctx):
    await ctx.send('Dennis! '*3)

@client.command(aliases=['hi'])
async def saysomething(ctx):
    await ctx.send('I\'m the best midlaner! bruh')

@client.command(aliases=['bruh'])
async def saybruh(ctx):
    await ctx.send(':/')

@client.command()
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('joinAudio.m4a')
        player = voice.play(source)
        await ctx.send('Big Boy Dennis is here!')
    else:
        await ctx.send('You are not in a voice channel')

@client.command()
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.voice_client.disconnect()
        await stop(ctx)
        await ctx.send('Big Boy Dennis is leaving now :/')
    else:
        await ctx.send('I\'m not in a voice channel')

@client.command()
async def sing(ctx):
        if(ctx.voice_client):
            voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
            source = FFmpegPCMAudio('song.m4a')
            player = voice.play(source)
        else:
            if(ctx.author.voice):
                channel = ctx.author.voice.channel
                voice = await channel.connect()
                source = FFmpegPCMAudio('song.m4a')
                player = voice.play(source)

@client.command()
async def play(ctx, url):
    song = os.path.isfile("song.mp3")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    try:
        if song:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send('Another song is playing')

    if not voice.is_connected():
        channel = ctx.author.voice.channel
        voice = await channel.connect()
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, 'song.mp3')
    voice.play(discord.FFmpegPCMAudio('song.mp3'))

    


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Nothing is playing bruh")

@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Nothing is paused bruh")

@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

        

        
        




client.run('ODQ2NDUwNTUwODc5MTU4MzMy.YKvsgQ.RxPiIY1AHR1TsGTfikaKYyquxKs')