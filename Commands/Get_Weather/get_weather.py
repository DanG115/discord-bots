import discord
from discord.ext import commands
import requests
import os

class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'


api_key = "YOUR_API_KEY"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


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
    print(Colors.BLUE + "Created By DanG4115 | v1.0.0" + Colors.RESET)
    await client.change_presence(activity=discord.Game(name="Weather Bot | w!setup"))




@client.command(name='weather', help='Get the current weather for a city')
async def weather(self, ctx, *, city: str):
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel

    if x["cod"] != "404":
        async with channel.typing():
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]

            embed = discord.Embed(
                    title=f"Weather in {city_name}",
                    color=ctx.guild.me.top_role.color,
                    timestamp=ctx.message.created_at,
            )
            embed.add_field(name="Description", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
            embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await channel.send(embed=embed)
    else:
        await channel.send("City not found.")




@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        error_message = f"Invalid Command Used :rolling_eyes:\nTry: `{ctx.prefix}help`"
        embed = discord.Embed(
            title="Error",
            description=error_message,
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)


client.run(os.getenv('DISCORD_BOT_TOKEN'))