import json
import asyncio
import datetime
import disnake

from disnake.ext import commands

with open('config.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

terminal_channel = data["botInfo"]["terminal_channel"]
guild = data["botInfo"]["guild_id"]


with open('permissions.json','r',encoding='utf-8-sig') as g:
    data = json.load(g)
    
owner = data["owner"]
devs = data["devs"]
bots = data["bots"]
hd_admin = data["head_admin"]
admins = data["admins"]
mods = data["moderators"]
cyb_pol = data["cyber_police"]
supp_staff = data["support_staff"]
comm_helper = data["community_helper"]
nitro_mem = data["nitro_member"]
member = data["member"]
default_role = data["default_role"]

class OwnerCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.guild = guild
        self.gawther_terminal = self.bot.get_text_channel(terminal_channel)
        
        self.owner = owner
        self.devs = devs
        self.bots = bots 
        self.hd_admin = hd_admin
        self.admins = admins
        self.mods = mods 
        self.cyb_pol = cyb_pol 
        self.supp_staff = supp_staff 
        self.comm_helper = comm_helper
        self.nitro_mem = nitro_mem
        self.member = member 
        self.default_role = default_role


    @commands.command()
    @commands.is_owner()
    async def useGuildTemplate(self, ctx):
        self.gawther_terminal.send(f'''
            Gawther Server Reset Function Triggered For 
            {self.guild.name} @ {datetime.datetime.utcnow()}
        ''')

        def check(m):
            return ctx.message.author.id == m.author.id
        
        """
        show counts of items being deleted
        """
        messageCount = 0
        
        for channel in self.guild.text_channels:
            async for message in channel.history(limit=None):
                messageCount += 1
                
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            timestamp=ctx.message.created_at,
            title='Gawther System Notifications',
            description='You have execute a very dangerous function.\
                Please enter your discord id to continue.'
        ).set_thumbnail(
            url=self.bot.user.avatar
        )

        msg = await ctx.send(embed=embed)

        owner_id = await self.bot.wait_for('message', check=check, timeout=15)

        if owner_id.content == self.bot.owner_id:
            embed.add_field(
                name='This Command Is Going To Exeute The Following:',
                value=f'Remove All Roles, Text Channels, Voice Channels, Categories, and Messages Within {self.guild.name}',
                inline=False
            ).add_field(
                name=f'Categories To Be Deleted: {len([cat for cat in ctx.guild.categories])}'
            ).add_field(
                name=f'Channels To Be Deleted: {len([a for a in [b for b in ctx.guild.categories]])}'
            ).add_field(
                name=f'Roles To Be Deleted: {len([r for r in ctx.guild.roles])}'
            ).add_field(
                name=f'Total Number Of Messages Being Deleted: {messageCount}'
            ).add_field(
                name='Confirmation',
                value='Given the information above, are you sure that you want\
                    to completed erase, and re-write Gawther Discord? Y/N',
                inline=False
            )

            await owner_id.delete()
            await msg.edit(embed=embed)

            answer = await self.bot.wait_for('message', check=check, timeout=15)

            if answer.content.lower() == 'y':
                self.gawther_terminal.send('gawther Is Cleaning Up The Server Now. . .')

                # await self.backup()

            else:
                await msg.delete()
                await answer.delete()
                msg = await ctx.send('Operation Cancelled')
                await asyncio.sleep(10)
                await msg.delete()


def setup(bot):
    bot.add_cog(OwnerCommands(bot))
    
    
    
"""
BELOW THIS COMMENT IS A
WHOLE LOT OF CODE. I AM WORKING
ON IT. IGNORE IT OR DELETE IT FOR 
AS OF RIGHT NOW IT'S USELESS
"""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

















































































































# async def backup(self):
#         self.gawther_terminal.send(
#             'gawther Is Backing Up All Channel Messages. . .')

#         with sql.connect('main.db') as mdb:
#             cur = mdb.cursor()

#             for category in self.guild.categories:
#                 for channel in category:
#                     async for message in channel.history(limit=None):
#                         srch = 'INSERT INTO chatBackup(guildId,timestamp,author,category,channel,content) VALUES (?,?,?,?,?,?)'
#                         val = (self.guild.id, message.created_at, message.author.id,
#                                category.id, channel.id, message.content)

#                         cur.execute(srch, val)

#         self.gawther_terminal.send('Message Backup Complete. . .')

#         await self.deleteRoles()

#     async def deleteRoles(self):
#         self.gawther_terminal.send('Removing Roles. . .')

#         role_count = 0

#         for role in self.guild.roles:
#             await role.delete()
#             role_count += 1

#         self.gawther_terminal.send(f'Removed {role_count} roles. . .')

#         await self.clear_cat_chan()

#     async def clear_cat_chan(self):
#         self.gawther_terminal.send('Removing Categories and Channels. . .')
#         category_counter = 0
#         channel_counter = 0

#         for category in self.guild.categories:
#             category_counter += 1

#             for channel in category:
#                 if channel.name == self.gawther_terminal.name:
#                     pass
#                 else:
#                     channel_counter += 1
#                     await channel.delete()

#             await category.delete()

#         self.gawther_terminal.send(
#             f'Removed {category_counter} categories, and {channel_counter} channels. . .'
#             )
        
#         await self.writeRoles()
        
        
#     async def writeRoles(self):
#         names = [
#             'Owner', '#FB0707',
#             'Devs', '#FF8405',
#             'Bots', '#FFD905',
#             'Head Admin', '#74FF05',
#             'Admin', '#051DFF',
#             'Moderator', '#9005FF',
#             'Cyber Police', '#9005FF',
#             'Support Staff', '#05FFE3',
#             'Community Helper', '#FF05AF',
#             'Nitro Member', '#9FE2BF',
#             'Member', '#CCCCFF',
#             'Muted', '#000000'
#         ]
        
#         for name in names:
#             new_role = await self.guild.create_role(
#                 name=name,
                
#             )
        
#         await self.writeGawther()
    
    
#     async def writeGawther(self, ctx):
#         await self.gawther_terminal.send('Creating Gawther Category')

#         gawther = await self.guild.create_category(name='=========Gawther=========')

#         text = ['announcements', 'rules', 'welcome', 'change_log']

#         for channel in text:
#             new_channel = await self.guild.create_text_channel(name=channel, category=gawther)
            
#         for perm in self.owner:
#             if perm == True:
#                 new_channel.permission_overwrites()

#         await self.guild.create_category(name='=========================')

#         await self.gawther_terminal.send('Gawther Category Created Successfully')

#         await self.writeShowCase()

#     async def writeShowCase(self, ctx):
#         await self.gawther_terminal.send('Creating Show Case Category')

#         showcase = await self.guild.create_category(name='========Show-Case========')

#         text = ['plugins', 'themes', 'art',
#                 'achievments', 'awards', 'trophies']

#         for channel in text:
#             await self.guild.create_text_channel(name=channel, category=showcase)

#         await self.guild.create_category(name='=========================')

#         await self.gawther_terminal.send('Show Case Category Created Successfully')

#         await self.writeCodeChall()

#     async def writeCodeChall(self, ctx):
#         await self.gawther_terminal.send('Creating Code Challenges Category')

#         codechall = await self.guild.create_category(name='=====Code-Challenges=====')

#         text = ['python', 'html_css', 'javascript', 'java']

#         for channel in text:
#             await self.guild.create_text_channel(name=channel, category=codechall)

#         await self.guild.create_category(name='=========================')

#         await self.gawther_terminal.send('Code Challenges Category Created Successfully')

#         await self.writeSuggestions()

#     async def writeSuggestions(self, ctx):
#         await self.gawther_terminal.send('Creating Suggestions Category')

#         suggestions = await self.guild.create_category(name='=======Suggestions=======')

#         text = ['how_to', 'submit', 'view_others']

#         for channel in text:
#             await self.guild.create_text_channel(name=channel, category=suggestions)

#         await self.guild.create_category(name='=========================')

#         await self.gawther_terminal.send('Suggestions Category Created Successfully')

#         await self.writeLounge()

#     async def writeLounge(self, ctx):
#         await self.gawther_terminal.send('Creating G-Lounge Category')

#         lounge = await self.guild.create_category(name='=========GLounge=========')

#         text = ['chat', 'memes', 'food', '420_friendly', 'weather']
#         voice = ['hangout1', 'hangout2', 'hangout3', 'hangout4']

#         for channel in text:
#             await self.guild.create_text_channel(name=channel, category=lounge)

#         for channel in voice:
#             await self.guild.create_voice_channel(name=channel, category=lounge)

#         await self.guild.create_category(name='=========================')

#         await self.gawther_terminal.send('G-Lounge Category Created Successfully')

#         await self.writeMusic()

#     async def writeMusic(self, ctx):
#         await self.gawther_terminal.send('Creating G-Music Category Now')

#         music = await self.guild.create_category(name='=========G-Music=========')

#         text = ['radio1_commands', 'radio2_commands',
#                 'radio3_commands', 'radio4_commands']
#         voice = ['radio1', 'radio2', 'radio3', 'v-radio4']

#         for channel in text:
#             await self.guild.create_text_channel(name=channel, category=music)

#         for channel in voice:
#             await self.guild.create_text_channel(name=channel, category=music)

#         await self.guild.create_category(name='=========================')

#         await self.gawther_terminal.send('G-Music Category Created Successfully')

#         await self.writeGgaming()

#     async def writeGgaming(self, ctx):
#         await self.gawther_terminal.send('Creating Gaming Categories')

#         await self.guild.create_category(name='=========G-Gaming========')

#         await self.createMinecraft()

#     async def createMinecraft(self, ctx):
#         minecraft = await self.guild.create_category(name='========Minecraft========')

#         text = ['announcements', 'chat', 'patterns',
#                 'accomplishments', 'game_chat']
#         voice = ['room_one', 'room_two',
#                  'room_three', 'room_four', 'room_five']

#         for channel in text:
#             await self.guild.create_text_channel(name=channel, category=minecraft)

#         for channel in voice:
#             await self.guild.create_voice_channel(name=channel, category=minecraft)

#         await self.guild.create_category(name='=========================')

#         await self.gawther_terminal.send('Created Minecraft Category Successfully')

#         await self.createSW()

#     async def createSW(self, ctx):
#         sw = await self.guild.create_category(name='======Summoners-War======')

#         text = ['announcements', 'chat', 'arena_hook_up',
#                 'raid_hook_up', 'add_me', 'accomplishments', 'most_proud_of']
#         voice = ['room_one', 'room_two',
#                  'room_three', 'room_four', 'room_five']
#         # re-write channel names to reflect gaming itself.

#         for channel in text:
#             await self.guild.create_text_channel(name=channel, category=sw)

#         for channel in voice:
#             await self.guild.create_text_channel(name=channel, category=sw)

#         await self.guild.create_category(name='=========================')

#         await self.gawther_terminal.send('Created Summoners War Category Successfully')

#         await self.writeFactorio()

#     async def writeFactorio(self, ctx):
#         await self.gawther_terminal.send('Creating Factorio Category')

#         factorio = await self.guild.create_category(name='========Factorio!========')

#         text = ['announcements', 'blueprints', 'servers', 'setups', 'chat']
#         voice = ['room_one', 'room_two',
#                  'room_three', 'room_four', 'room_five']

#         for channel in text:
#             await self.guild.create_text_channel(name=channel, category=factorio)

#         for channel in voice:
#             await self.guild.create_text_channel(name=channel, category=factorio)

#         await self.guild.create_category(name='=========================')

#         await self.gawther_terminal.send('Created Factorio Category Successfully')

#         await self.writeSupport()

#     async def writeSupport(self, ctx):
#         await self.gawther_terminal.send('Creating Support Category')

#         support = await self.guild.create_category(name='=========Support=========')

#         text = ['how_to', 'que', 'alpha', 'bravo', 'charlie', 'delta', 'echo',
#                 'frank', 'golf', 'hotel', 'igloo', 'juliet', 'kilo', 'lima',
#                 'mike', 'november', 'oscar', 'papa', 'quebec', 'romeo', 'sierra',
#                 'tango', 'uniform', 'victor', 'whiskey', 'x-ray', 'yankee', 'zulu']

#         for channel in text:
#             await self.guild.create_text_channel(name=channel, category=support)

#         await self.guild.create_category(name='=========================')

#         await self.gawther_terminal.send('Created Support Category Successfully')

#         await self.writeStaff()

#     async def writeStaff(self, ctx):
#         await self.gawther_terminal.send('Creating Staff Category')

#         staff = await self.guild.create_category(name='==========Staff==========')

#         text = ['announcements', 'reminders', 'rules', 'info_per_role', 'chat']
#         voice = ['one', 'two', 'three', 'four', 'five']

#         for channel in text:
#             await self.guild.create_text_channel(name=channel, category=staff)

#         for channel in voice:
#             await self.guild.create_voice_channel(name=channel, category=staff)

#         await self.guild.create_category(name='=========================')

#         await self.gawther_terminal.send('Created Staff Category Successfully')

#         await self.writeDevelopers()

#     async def writeDevelopers(self, ctx):
#         await self.gawther_terminal.send('Creating Developers Category')

#         devs = await self.guild.create_category(name='========Developers=======')

#         text = ['announcements', 'reminders', 'notes',
#                 'file_swap', 'member_suggestions', 'chat']
#         voice = ['one', 'two', 'three', 'four', 'five']

#         for channel in text:
#             await self.guild.create_text_channel(name=channel, category=devs)

#         for channel in voice:
#             await self.guild.create_voice_channel(name=channel, category=devs)

#         await self.guild.create_category(name='=========================')

#         await self.gawther_terminal.send('Created Developers Category Successfully')

#         await self.writeLogs()

#     async def writeLogs(self, ctx):
#         await self.gawther_terminal.send('Creating Logs Category')

#         logs = await self.guild.create_category(name='===========Logs==========')

#         text = ['gawther_terminal', 'warning_logs', 'mute_logs',
#                 'kick_logs', 'ban_logs', 'audit_logs', 'bugs']

#         for channel in text:
#             await self.guild.create_text_channel(name=channel, category=logs)

#         await self.guild.create_category(name='=========================')

#         await self.gawther_terminal.send('Created Logs Category Successfully')

#         await self.send_confirmation()

#     async def send_confirmation(self, ctx):
#         embed = disnake.Embed(
#             color=disnake.Colour.green(),
#             timestamp=ctx.message.created_at,
#             title='Gawther System Notification',
#             description='Gother has successfully:\n1) Backed Up All Chat Channels.\n2)Created All Categories and Channels With Corresponding Permissions'
#         ).set_thumbnail(
#             url=self.bot.user.avatar
#         )

#         await self.gawther_terminal.send(embed=embed)