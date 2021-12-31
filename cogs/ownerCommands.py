import sqlite3 as sql
import asyncio
import datetime
import disnake

from disnake.ext import commands

class OwnerCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.is_owner()
    async def useGuildTemplate(self, ctx):
        self.gawther_terminal.send(f'''
            Gawther Server Reset Function Triggered For 
            {self.guild.name} @ {datetime.datetime.utcnow()}
            By {ctx.message.author.name}
        ''')

        def check(m):
            return ctx.message.author.id == m.author.id
        
        messageCount = 0
        
        for channel in self.guild.text_channels:
            async for message in channel.history(limit=None):
                messageCount += 1
                
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            timestamp=ctx.message.created_at,
            title='Gawther System Notifications',
            description='You have execute a very dangerous function. Please enter your discord id to continue.'
        ).set_thumbnail(
            file='./images/warning.jpg'
        )

        msg = await ctx.send(embed=embed)

        embed.add_field(
            name='This Command Is Going To Exeute The Following:',
            value=f'Remove All Roles, Text Channels, Voice Channels, Categories, and Messages Within {self.guild.name}',
            inline=False
        ).add_field(
            name=f'Categories To Be Deleted: {len([cat for cat in ctx.guild.categories])}'
        ).add_field(
            name=f'Channels To Be Deleted: {len([a for a in [b for b in ctx.guild.categories]])}'
        ).add_field(
            name=f'Total Number Of Messages Being Deleted: {messageCount}'
        ).add_field(
            name='Confirmation',
            value='Given the information above, are you sure that you want\
                to completed erase, and re-write Gawther Discord? Y/N',
            inline=False
        )

        await msg.edit(embed=embed)

        answer = await self.bot.wait_for('message', check=check, timeout=15)

        if answer.content.lower() == 'y':
            self.gawther_terminal.send('Gawther Is Cleaning Up The Server Now. . .')

            await self.backup()

        else:
            await msg.delete()
            await answer.delete()
            msg = await ctx.send('Operation Cancelled')
            await asyncio.sleep(10)
            await msg.delete()

                
    async def backup(self):
        # insert backup stuff here, or wherever needed

        self.gawther_terminal.send('Message Backup Complete. . .')
        
        
    async def 


def setup(bot):
    bot.add_cog(OwnerCommands(bot))