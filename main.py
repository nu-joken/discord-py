import os
import discord
from discord.ext import commands
import dotenv
from sqlalchemy import true

intents = discord.Intents.default()
bot = commands.Bot(intents=intents)


TOKEN = ''

if __name__ == "__main__": 
    TOKEN = os.environ["DISCORD_TOKEN"]
else:
    dotenv.load_dotenv(override=True)
    TOKEN = os.getenv("DISCORD_TOKEN")

# hooks

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# slash command

@bot.slash_command()
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond('pong')

@bot.slash_command()
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Choo choo! 🚅")


bot.run(TOKEN)

