#=========================================================== Basic Discord.py Template ===========================================================#

# Welcome to the basic Discord.py template created by DanG115.
# This template provides you with a starting point for creating your own Discord bot.

#===========================================================

# Notices:
# - Before you start:
# Simply run this command in any terminal - just installs the necessary packages to run a discord bot (discord.py):
# Run: pip install -r requirements.txt


# - Discord App & Bot Token
#   1. Create a new Discord application on the Discord Developer Portal: https://discord.com/developers/applications
#   2. Create a bot for your application and copy the token. 
#   3. Down the left hand side click:
#         OAuth2 > URL Generator 
#   4. Then in scopes click on:
#         applications.commands & bot
#   5. Scroll down to Bot Perms
#         administrator  - we need to change that later on but for now its ok!
#   6. Then at the bottom copy the url, paste into your browser and add the bot to your server


# - .env file instructions:
#   1. Open the .env file and add the following line:
#      DISCORD_BOT_TOKEN = 123 
#      Replace '123' with your discord bot token.
#   2. Do not share your .env file or the bot token with others. The token acts as a key to control your bot and with the key anyone can connect to
#      your bot.

#===========================================================


import discord
from discord.ext import commands
import os   


from dotenv import load_dotenv
load_dotenv()

discord_prefix = "w!" #Changeable prefix

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=(discord_prefix), intents=intents)
client.remove_command("help") 


@client.event
async def on_ready():
    print('YourBotNameHere')
    print('Logged in as: ' + client.user.name) 
    print('Client User ID: ' + str(client.user.id))
    print( "Created By DanG115 | v1.0.0")
    await client.change_presence(activity=discord.Game(name="Default Template | /setup"))

#=====================================================================
    #Add all of the commands starting below!
#=====================================================================


@client.commands()
async def welcome(ctx):
    await ctx.send("Welcome!")

































#=====================================================================
    #Don't edit anything below this notice
#=====================================================================
    


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
      await ctx.send('Invalid Command Used :rolling_eyes:')
      await ctx.send(f'Try: {discord_prefix}help')



token = os.environ['DISCORD_BOT_TOKEN']
client.run(token)
