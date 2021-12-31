import sqlite3 as sql
import asyncio
import datetime
import disnake
import json

from disnake.ext import commands

with open('config.json','r',encoding='utf-8-sig') as f:
    data = json.load(f)

terminal = data["botInfo"]["terminal_channel"]

class OwnerCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """
    figure out why command takes too long to respond
    """

    @commands.command()
    @commands.is_owner()
    async def resetServer(self, ctx):
        self.gawther_terminal = self.bot.get_channel(terminal)

        await self.gawther_terminal.send(f"Gawther Server Reset Function Triggered For {ctx.guild.name} @ {datetime.datetime.utcnow().__format__('%m/%d/%y -- %H:%M:%S')} By {ctx.message.author.name}")

        def check(m):
            return ctx.message.author.id == m.author.id

        messageCount = 0

        for channel in ctx.guild.text_channels:
            async for message in channel.history(limit=None):
                messageCount += 1

        file=disnake.File('./images/warning.jpg')

        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            timestamp=ctx.message.created_at,
            title='Gawther System Notifications',
            description=':rotating_light:You have executed a very dangerous command.:rotating_light:.'
        ).add_field(
            name=':rotating_light:This Command Is Going To Execute The Following:rotating_light:',
            value=f'Remove All Roles, Text Channels, Voice Channels, Categories, and Messages Within {ctx.guild.name}',
            inline=False
        ).add_field(
            name=f'Categories To Be Deleted: {len([cat for cat in ctx.guild.categories])}',
            value='\u200b'
        ).add_field(
            name=f'Channels To Be Deleted: {len([channel for channel in [category for category in ctx.guild.categories]])}',
            value='\u200b'
        ).add_field(
            name=f'Total Number Of Messages Being Deleted: {messageCount}',
            value='\u200b'
        ).add_field(
            name='Confirmation',
            value='Given the information above, are you sure that you want to completed erase, and re-write Gawther Discord? Y/N',
            inline=False
        ).set_image(
            url="attachment://./images/warning.jpg"
        ).set_thumbnail(
            url=ctx.guild.icon
        )

        msg = await ctx.send(embed=embed, file=file)

        answer = await self.bot.wait_for('message', check=check)

        if answer.content.lower() == 'y':
            await self.gawther_terminal.send('Gawther Is Cleaning Up The Server Now. . .')

            await self.backup()

        else:
            await msg.delete()
            await answer.delete()
            msg = await ctx.send('Operation Cancelled')
            await asyncio.sleep(10)
            await msg.delete()

    async def backup(self):
        # insert backup stuff here, or wherever needed
        await self.gawther_terminal.send('Message Backup Started')

        await self.gawther_terminal.send('Message Backup Complete. . .')

        await self.executeTemplate()


    async def executeTemplate(self):
        for cat in self.gawther_terminal.guild.categories:
            new_cat = await cat.clone(
                name=cat.name,
                reason="LockDown Initiated"
            )

            await new_cat.edit(
                position=cat.position,
                sync_permissions=True
            )

            for chan in cat.channels:
                new_chan = await chan.clone(
                    name=chan.name,
                    reason="LockDown Initiated"
                )

                await new_chan.edit(
                    category=new_cat,
                    sync_permissions=True
                )

                if new_chan.name == "gawther_terminal":
                    with open('config.json','r',encoding='utf-8-sig') as f:
                        data = json.load(f)

                    data["botInfo"]["terminal_channel"] = new_chan.id

                    with open('config.json','w',encoding='utf-8-sig') as new:
                        data = json.dump(data,new,indent=4)

                    await chan.delete()

                    await asyncio.sleep(0.5)

                else:
                    await chan.delete()

                    await asyncio.sleep(0.2)

            await cat.delete()

            await asyncio.sleep(0.2)

        await self.confirmation()


    async def confirmation(self):
        guild = self.bot.get_guild(self.gawther_terminal.guild.id)

        categories = 0
        channels = 0

        for category in guild.categories:
            for channel in category.channels:
                channels += 1
            categories += 1

        embed=disnake.Embed(
            color=disnake.Colour.green(),
            title='Gother System Notification',
            description=f'''Execution Successful! All Categories and Channels have been recreated.
                Category Count: {categories}
                Channel Count: {channels}
            '''
        ).set_thumbnail(
            url=guild.icon
        )

        category = disnake.utils.get(guild.categories, name='Logs')

        for channel in category.channels:
            if channel.name == 'gawther_terminal':
                await channel.send(embed=embed)
                break
            else:
                if channel.permissions_for(guild.me).send_messages == True:
                    await channel.send(embed=embed)
                    break


def setup(bot):
    bot.add_cog(OwnerCommands(bot))
