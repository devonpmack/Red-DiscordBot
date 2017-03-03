import discord
import random
from discord.ext import commands

class memes:
    """Dank"""

    def __init__(self, bot):
        random.seed()
        self.links = set()
        self.memes = set()
        self.bot = bot
        with open('data/memes/data.txt') as f:
            self.links = f.read().splitlines()
        f.close()
        with open('data/memes/memes.txt') as f2:
            self.memes = f2.read().splitlines()
        f2.close()

    @commands.group(pass_context=True, no_pm=True)
    async def thathockeylover(self,ctx):
        """Send a hockeylover meme"""
        if ctx.invoked_subcommand is None:
            await self.bot.say(random.choice(self.links))

        #Your code will go here

    @thathockeylover.command()
    async def add(self, toAdd):
        """Add a hockeylover meme"""
        f = open('data/memes/data.txt', 'w')
        self.links.append(toAdd)
        for item in self.links:
            f.write("%s\n" % item)
        await self.bot.say("Added " + toAdd + ".")
        f.close()

    @thathockeylover.command()
    async def remove(self, toRemove):
        """Remove a hockeylover meme"""
        f = open('data/memes/data.txt', 'w')
        try:
            self.links.remove(toRemove)
            await self.bot.say("Removed " + toRemove + ".")
            for item in self.links:
                f.write("%s\n" % item)
            f.close()
        except:
            await self.bot.say("Failed to remove " + toRemove + ". Doesn't exist.")



    @commands.group(pass_context=True, no_pm=True)
    async def meme(self,ctx):
        """Send a random meme"""
        rnd = 8
        #Your code will go here
        if ctx.invoked_subcommand is None:
            await self.bot.say(random.choice(self.memes))

    @meme.command()
    async def add(self, toAdd):
        """Add a meme"""
        f = open('data/memes/memes.txt', 'w')
        self.links.append(toAdd)
        for item in self.memes:
            f.write("%s\n" % item)
        await self.bot.say("Added " + toAdd + ".")
        f.close()

    @meme.command()
    async def remove(self, toRemove):
        """Remove a meme"""
        f = open('data/memes/memes.txt', 'w')
        try:
            self.links.remove(toRemove)
            await self.bot.say("Removed " + toRemove + ".")
            for item in self.memes:
                f.write("%s\n" % item)
            f.close()
        except:
            await self.bot.say("Failed to remove " + toRemove + ". Doesn't exist.")


def setup(bot):
    bot.add_cog(memes(bot))
