from discord.ext import commands
from collections import defaultdict
import discord
import os
import requests
#import heart
import random
import ctypes
import youtube_dl

token = os.environ.get("BOT_TOKEN")
weatherID = os.environ.get("WEATHER_TOKEN")
weatherAPI = "http://api.openweathermap.org/data/2.5/weather?q="
weatherUnits = "&units=imperial&appid="

def rollDice(num_dice, some_dice):
    total = defaultdict(list)
    total['rolls'] = []
    total['total'] = 0
    for i in range(num_dice):
        total['rolls'].append(random.randint(1, some_dice))
        total['total'] = sum(total['rolls'])
    return total

hooman = commands.Bot(
    command_prefix='!',
    owner_id=352291290584580096,
    case_insensitive=True
)

@hooman.event
async def on_ready():
    print("Hooman awake and ready!")
    #print(hooman.owner_id)

@hooman.command(name="hello")
async def hello(ctx):
    await ctx.send("Hello {}".format(ctx.message.author.display_name))

@hooman.command(name="temp")
async def temp(ctx, *args):
    if len(args) == 0:
        city='corvallis'
    else:
        city=args[0]
        weather=requests.get(weatherAPI+city+weatherUnits+weatherID)
    await ctx.send("The temperature in {} is {} degrees Fahrenheit".format(weather.json()["name"], weather.json()["main"]["temp"]))

@hooman.command(name="roll")
async def roll(ctx, *args):
    result = defaultdict(list)
    for i in range(len(args)):
        num = int(str(args[i]).split('d')[0])
        dice = int(str(args[i]).split('d')[1])
        result = rollDice(num, dice)
    await ctx.send("The result of {}'s {}d{} is: {} for a total of {}".format(ctx.message.author.name, num, dice, result['rolls'], result['total']))

#@hooman.command(name="setMusic")
#async def setMusic(ctx):
#    await ctx.guild.create_text_channel("hooman-music")

@hooman.command(name="join")
async def join(ctx):
    ctypes.util.find_library('opus')
    author=ctx.message.author
    voiceChannel=author.voice.channel
    try:
        print('Connecting to ' + ctx.guild.name + ':' + voiceChannel.name)
        await voiceChannel.connect()
    except TimeoutError:
        print('Connection timed out...Could not connect')
    except discord.ClientException:
        print('Already in a voice channel')
        await ctx.send('I am already in a voice channel. Either use \'!disconnect\' or \'!move\'')
    except discord.opus.OpusNotLoaded:
        print('Opus Library not loaded!')

@hooman.command(name="move")
async def move(ctx):
    vc = ctx.voice_client
    author=ctx.message.author
    voiceChannel=author.voice.channel
    try:
        vc = ctx.voice_client
        print('Moving to ' + ctx.guild.name + ':' + voiceChannel.name)
        await vc.move_to(voiceChannel)
    except:
        print('Could not move to ' + ctx.guild.name + ':' + voiceChannel.name)

@hooman.command(name="play")
async def play(ctx, url):
    vc = ctx.voice_client
    options={
        #'outtmpl': '/home/vidovi/discord/songs/%(titles).%ext)s',
        'outtmpl': '/home/vidovi/discord/songs/song.%(ext)s',
        'format': 'bestaudio/best',
        'quiet': True,
    }
    print('Extracting info for ' + url)
    with youtube_dl.YoutubeDL(options) as ytdl:
        try:
            #yt = ytdl.extract_info(url, download=False)
            ytdl.download([url])
        except youtube_dl.DownloadError as e:
            print(str(e))
            await ctx.send('My apologies, This video is not available and could not be played')
            return

    #for x in yt['formats']:
        #try:
            #video = x['url']
            #audio = discord.FFmpegPCMAudio(video)
            #print(x['format'])
        #except:
            #print('Failed to create audio source')
        #break
    for files in os.listdir('/home/vidovi/discord/songs/'):
        if files.startswith('song'):
            song_to_play = '/home/vidovi/discord/songs/' + files
    audio = discord.FFmpegPCMAudio(song_to_play)

    if vc.is_playing():
        print('A song is already playing...stopping')
        vc.stop()
    print('Playing ' + url)
    vc.play(audio)
  
@hooman.command(name="pause")
async def pause(ctx):
    vc = ctx.voice_client
    if vc.is_playing():
        print('Pausing song')
        ctx.voice_client.pause()
    else:
        print('No song playing')

@hooman.command(name="resume")
async def resume(ctx):
    vc = ctx.voice_client
    if vc.is_paused():
        print('Resuming song')
        ctx.voice_client.resume()
    else:
        print('No paused song')

@hooman.command(name="stop")
async def stop(ctx):
    vc = ctx.voice_client
    if vc.is_playing():
        print('Song playing...stopping')
        vc.stop()
    print('Disconnecting from Voice Channel')
    await ctx.voice_client.disconnect()

hooman.run(token, bot=True, reconnect=True)
