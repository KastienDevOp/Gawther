import disnake
import sqlite3 as sql

from disnake.ext import commands 

class OnJoinFunctions(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        
        self.gother_terminal = self.bot.get_text_channel(861632215393763376)
        
        
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        self.gother_terminal.send(f'On Guild Join Function Triggered For {guild.name}')
        self.gother_terminal.send('Checking Categories Now. . .')
        
    
    async def cat_check(self, guild):
        allItems = [
            '=========Gawther=========', 'announcements', 'rules', 'welcome', 'change_log', '=========================',
            '========Show-Case========', 'plugins', 'themes', 'art', 'achievments', 'awards', 'trophies', '========================='
            '=====Code-Challenges=====', 'python', 'html_css', 'javascript', 'java', '=========================',
            '=======Suggestions=======', 'how_to', 'submit', 'view_others', '=========================',
            '=========GLounge=========', 'chat', 'memes', 'food', '420_friendly', 'weather', '=========================',
            '=========G-Music=========', 'radio1', 'radio2', 'radio3', 'radio4', 'v-radio1', 'v-radio2', 'v-radio3', 'v-radio4', '=========================',
            '=========G-Gaming========',
            '========Minecraft========', 'announcements', 'chat', 'patterns', 'accomplishments', 'game_chat', '======VoiceChannels======', 'one', 'two', 'three', 'four', 'five', '=========================',
            '======Summoners-War======', 'announcements', 'chat', 'arena_hook_up', 'raid_hook_up', 'add_me', 'accomplishments', 'most_proud_of', '======VoiceChannels======', 'one', 'two', 'three', 'four', 'five''=========================',
            '========Factorio!========', 'announcements', 'blueprints', 'servers', 'setups', 'chat', '======VoiceChannels======', 'v-one', 'v-two', 'v-three', 'v-four', 'v-five', '=========================',
            '=========Support=========', 'how_to', 'que', 'alpha', 'bravo', 'charlie', 'delta', 'echo', 'frank', 'golf', 'hotel', 'igloo', 'juliet', 'kilo', 'lima', 'mike', 'november', 'oscar', 'papa', 'quebec', 'romeo', 'sierra', 'tango', 'uniform', 'victor', 'whiskey', 'x-ray', 'yankee', 'zulu', '=========================',
            '==========Staff==========', 'announcements', 'reminders', 'rules', 'info_per_role', 'chat', '======VoiceChannels======', 'v-one', 'v-two', 'v-three', 'v-four', '=========================',
            '========Developers=======', 'announcements', 'reminders', 'notes', 'file_swap', 'member_suggestions', 'chat', '======VoiceChannels======', 'v-one', 'v-two', 'v-three', 'v-four', '=========================',
            '===========Logs==========', 'gother_terminal', 'warning_logs', 'mute_logs', 'kick_logs', 'ban_logs', 'audit_logs', 'bugs', '========================='
        ]
        
        categories = []
        text_channels = []
        voice_channels = []
    
    
    async def clear_cat_chan(self, guild):
        for category in guild.categories:
            await category.delete()
            
        for channel in guild.text_channels:
            await channel.delete()
            
        for channel in guild.voice_channels:
            await channel.delete()
    
    
    async def cat_write(self, guild):
        pass
    
    
    async def chan_check(self, cat):
        pass
    
    
    async def chan_write(self, cat):
        pass
    
    
    async def write_members(self, guild):
        pass