import discord
from discord.ext import commands

class meme:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def noodles(self):
	    await self.bot.say("Orders over $25 (before tax) are 10% off (walk-ins only, cash only) at www.noodle2go.com")
	
    @commands.command()
    async def betrayers(self):	
	    await self.bot.say("[Quran 8:58] When you are betrayed by a group of people, you shall mobilize against them in the same manner. God does not love the betrayers.")
        
def setup(bot):
    bot.add_cog(meme(bot))