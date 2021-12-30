import os
import disnake
import json
import datetime

from disnake.ext import commands
from onGuildJoin import create_db

intents = disnake.Intents.all()

bot = commands.Bot(command_prefix=">>", intents=intents)

with open('master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

token = data["token"]


@bot.event
async def on_ready():
    guild = bot.get_guild(779290532622893057)

    channel = disnake.utils.get(guild.text_channels, name="gother_terminal")

    await channel.send(f'Logged In As: {bot.user.name}\n{datetime.datetime.now()}')

for file in os.listdir('./cogs'):
    if file.endswith('py'):
        bot.load_extension(f'./cogs/{file[:-3]}.cogs')


@bot.commands()
@bot.has_any_role("Devs")
async def update(ctx):
    guild = bot.get_guild(779290532622893057)

    channel = disnake.utils.get(guild.text_channels, name="gother_terminal")

    async def start():
        os.system("python ./bot.py")
        await confirm()
    await channel.send("Gother Is resetting Now. . .")
    await start()


async def confirm(ctx):
    guild = bot.get_guild(779290532622893057)

    channel = disnake.utils.get(guild.text_channels, name="gother_terminal")

    await channel.send("Gother Has Restarted!")

if __name__ == '__main__':
    create_db()
    bot.run(token)