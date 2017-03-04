import discord
import random
from discord.ext import commands

class Memes:
    """Dank"""

    def __init__(self, bot):
        random.seed()
        self.memes = set()
        self.bot = bot
        with open('data/memes/memes.txt') as f2:
            self.memes = f2.read().splitlines()
        f2.close()

    @commands.group(pass_context=True, no_pm=True)
    async def meme(self, ctx):
        """Send a meme"""
        if ctx.invoked_subcommand is None:
            await self.bot.say(random.choice(self.memes))
    @meme.command()
    async def add(self, toAdd):
        """Add a hockeylover meme"""
        f = open('data/memes/memes.txt', 'w')
        self.memes.append(toAdd)
        for item in self.memes:
            f.write("%s\n" % item)
        await self.bot.say("Added " + toAdd + ".")
        f.close()
    @meme.command()
    async def remove(self, toRemove):
        """Remove a hockeylover meme"""
        f = open('data/memes/memes.txt', 'w')
        try:
            self.memes.remove(toRemove)
            await self.bot.say("Removed " + toRemove + ".")
            for item in self.memes:
                f.write("%s\n" % item)
            f.close()
        except:
            await self.bot.say("Failed to remove " + toRemove + ". Doesn't exist.")
def setup(bot):
    bot.add_cog(Memes(bot))
