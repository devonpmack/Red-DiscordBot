import discord
import random
import praw
import subprocess
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
    @commands.command()
    async def angery(self):
        """ANGERY!!!!"""
        await self.bot.say("https://cdn.discordapp.com/attachments/175379883172691968/293511301752160256/71b.png")

    @commands.command()
    async def gitpull(self):
        """Pulls github changes"""
        bashCommand = "git -C /Red-DiscordBot pull"
        print("pulling git")
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        await self.bot.say(output)


    @commands.command()
    async def dank(self):
        """Get a random r/dankmemes post"""
        r = praw.Reddit(client_id='r_c8xhZFOC1kyQ',client_secret='-tdUgft_NRso9idHBmWkSRCfBfQ',password='devonbot',user_agent='discordbot',username='devon_bot')
        sub = r.subreddit('dankmemes')
        posts = sub.random()
        await self.bot.say(posts.title)
        await self.bot.say(posts.url)

    @commands.command()
    async def reddit(self,subreddit):
        """Get a random post from your choice of subreddit"""
        r = praw.Reddit(client_id='r_c8xhZFOC1kyQ', client_secret='-tdUgft_NRso9idHBmWkSRCfBfQ', password='devonbot',
                        user_agent='discordbot', username='devon_bot')
        sub = r.subreddit(subreddit)
        posts = sub.random()
        await self.bot.say(posts.title)
        await self.bot.say(posts.url)

    @commands.command()
    async def diwhy(self):
        """Get a random r/diWHY post"""
        r = praw.Reddit(client_id='r_c8xhZFOC1kyQ',client_secret='-tdUgft_NRso9idHBmWkSRCfBfQ',password='devonbot',user_agent='discordbot',username='devon_bot')
        sub = r.subreddit('diwhy')
        posts = sub.random()
        await self.bot.say(posts.title)
        await self.bot.say(posts.url)

    @commands.command()
    async def wholesome(self):
        """Get a random r/wholesomememes post"""
        r = praw.Reddit(client_id='r_c8xhZFOC1kyQ',client_secret='-tdUgft_NRso9idHBmWkSRCfBfQ',password='devonbot',user_agent='discordbot',username='devon_bot')
        sub = r.subreddit('wholesomememes')
        posts = sub.random()
        await self.bot.say(posts.title)
        await self.bot.say(posts.url)

    @commands.command(pass_context=True)
    async def pullup(self, ctx, user: discord.Member):
        """PULL UP ON @USER >.<"""

        # Your code will go here
        await self.bot.say(
            "BANG BANG! Yung " + ctx.message.author.mention + " just pulled up on " + user.mention + " ! :open_mouth: :open_mouth: :gun: :gun:")

    @commands.group(pass_context=True, no_pm=True)
    async def meme(self, ctx):
        """Send a meme"""
        if ctx.invoked_subcommand is None:
            await self.bot.say(random.choice(self.memes))
    @meme.command()
    async def add(self, toAdd):
        """Add a meme"""
        f = open('data/memes/memes.txt', 'w')
        self.memes.append(toAdd)
        for item in self.memes:
            f.write("%s\n" % item)
        await self.bot.say("Added " + toAdd + ".")
        f.close()
    @meme.command()
    async def remove(self, toRemove):
        """Remove a meme"""
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
