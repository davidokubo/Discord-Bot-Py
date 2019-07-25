from discord.ext import commands
from collections import defaultdict
import discord
import os
import requests
import heart
import random
import ctypes


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
  print(hooman.owner_id)


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


@hooman.command(name="setMusic")
async def setMusic(ctx):
  await ctx.guild.create_text_channel("hooman-music")

@hooman.command(name="play")
async def play(ctx, url):
  musicChannel = discord.utils.get(ctx.guild.text_channels, name="hooman-music")
  channel = ctx.channel
  if channel == musicChannel:
    author=ctx.message.author
    voiceChannel=author.voice.channel
    await voiceChannel.connect()

    #player=await vc.create_ytdl_player(url)
    #player.start

heart.heartbeat()
hooman.run(token, bot=True, reconnect=True)