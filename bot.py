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
term_chan = data["botInfo"]["terminal_channel"]


@bot.event
async def on_ready():
    channel = bot.get_channel(term_chan)
    await channel.send(
        f'''Logged In As: {bot.user.name}
            {datetime.datetime.now().__format__(
                '%m/%d/%y -- %H:%M:%S')}
         '''
    )

channel = bot.get_channel(term_chan)
for filename in os.listdir('./cogs'):
    if filename.endswith('py'):
        bot.load_extension(f'cogs/{filename[:-3]}')
        channel.send(filename, 'loaded')


@bot.commands()
@bot.has_any_role("Devs")
async def update(ctx):
    channel = bot.get_channel(term_chan)
    async def start():
        os.system("python ./bot.py")
        await confirm()
    await channel.send("Gother Is resetting Now. . .")
    await start()


async def confirm(ctx):
    channel = bot.get_channel(term_chan)
    await channel.send("Gother Has Restarted!")

if __name__ == '__main__':
    # create_db()
    bot.run(token)