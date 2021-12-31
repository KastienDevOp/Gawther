import os
import disnake
import json
import datetime

from disnake.ext import commands
# from createDb import create_db

intents = disnake.Intents.all()

bot = commands.Bot(command_prefix=">>", intents=intents)

with open('config.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

token = data["botInfo"]["token"]
guildId = data["botInfo"]["guild_id"]


@bot.event
async def on_ready():
    guild = bot.get_guild(guildId)
    
    channel = disnake.utils.get(guild.text_channels, name='gawther_terminal')
    
    await channel.send(f"Logged In As: {bot.user.name} @ {datetime.datetime.now().__format__('%m/%d/%y -- %H:%M:%S')}")


for filename in os.listdir('./cogs'):
    if filename.endswith('py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.command()
@commands.has_any_role("Owner", "Devs")
async def update(ctx,):
    async def start(ctx):
        os.system("python ./bot.py")
        
    
    guild = bot.get_guild(guildId)
    
    channel = disnake.utils.get(guild.text_channels, name='gawther_terminal')
    
    await channel.send("Gother Is resetting Now. . .")

    await start(ctx)

if __name__ == '__main__':
    # create_db()
    bot.run(token)