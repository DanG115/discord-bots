import discord
from discord.ext import commands



discord_prefix = "w!" #Changeable prefix

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=(discord_prefix), intents=intents)
client.remove_command("help") #removes default help command


@client.event
async def on_ready():
    print('YourBotNameHere')
    print('Logged in as: ' + client.user.name) 
    print('Client User ID: ' + str(client.user.id))
    print("Created By DanG4115 | v1.0.0" )
    await client.change_presence(activity=discord.Game(name="Hello"))



@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(client.latency * 1000)}ms 🏓')
