import os
import discord
from discord.ext import commands
from keep_alive import keep_alive
from dotenv import load_dotenv

intents = discord.Intents.all()
client = commands.Bot(command_prefix="g!", case_insensitive=True, intents_members=True)
intents = discord.Intents(messages=True, guilds=True)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game('g!help'))
  print("Gapla Assistant Bot is ready. \n")

@client.command(help="View the Gapla Website")
async def web(ctx):
	await ctx.send("The Gapla website is at https://my.gaplagov.org.")

@client.command(help="View the Gapla News")
async def news(ctx):
	await ctx.send("The website of the Gapla National News Network is at https://news.gaplagov.org. Disclaimer: although GNNN is on a government subdomain, it is not a government website.")

@client.command(help="Become a Citizen of Gapla")
async def citizen(ctx):
	await ctx.send("You can become a citizen of Gapla by clicking this link: https://go.gaplagov.org/citizen.")

@client.command(help="View Gapla's MicroWiki Page")
async def wiki(ctx):
	await ctx.send("View Gapla's MicroWiki page by clicking this link: https://go.gaplagov.org/wiki. It will redirect to MicroWiki.")

@client.command(help="Use the Bank of Gapla Bot")
async def bank(ctx):
	await ctx.send("Try typing gd!help.")

keep_alive()

#This is usually where the token is, but we deleted it for privacy reasons.
