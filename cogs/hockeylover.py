import discord
import random
from discord.ext import commands

class Hockeylover:
    """Dank"""

    def __init__(self, bot):
        random.seed()
        self.links = set()
        self.bot = bot
        with open('data/memes/data.txt') as f:
            self.links = f.read().splitlines()
        f.close()

    @commands.command()
    async def time(self):
        """Tells you the time (in PJT)"""
        import datetime
        now = datetime.datetime.now() - datetime.timedelta(hours=4) + datetime.timedelta(minutes=1)
        eleven = now.replace(hour=23, minute=0, second=0, microsecond=0)

        diff = eleven-now
        h = int(diff.total_seconds() / 3600)
        m = int(diff.total_seconds() % 3600 / 60)
        if diff.total_seconds() > 0:
            await self.bot.say("The current time is %d:%02d UJT(Until Justin's Bedtime)" % (h, m))
        else:
            await self.bot.say("IT IS %d HOURS %d MINUTES PAST JUSTIN'S BEDTIME!!!!!" % (h, m))

        if diff.total_seconds() <= 0:
            await self.bot.say(":rotating_light::rotating_light::rotating_light: WEE WOO WEE WOO WEE WOO"
                               " :rotating_light::rotating_light::rotating_light: YOU ARE BEING DETAINED"
                               " :cop::skin-tone-1::cop::skin-tone-1::cop::skin-tone-1: FOR BEING AWAKE"
                               "  PAST JUSTINS BEDTIME :clock1::ok_hand::skin-tone-1::smirk: PLEASE SHOW"
                               " ME YOUR PERMISSION SLIP FROM JUSTINS MOM :pray::skin-tone-1::pencil:"
                               " :speak_no_evil::raised_hands::skin-tone-2::fire::fire: 11 PM ONLY!!"
                               " IT DONT MATTER IF YOU UP DOING HOMEWORK OR WHAT :sweat_drops::"
                               "sweat_drops::weary::weary::100::100::100:")

    @commands.group(pass_context=True, no_pm=True)
    async def thathockeylover(self, ctx):
        """Send a hockeylover meme"""
        if ctx.invoked_subcommand is None:
            await self.bot.say(random.choice(self.links))
            # Your code will go here

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
def setup(bot):
    bot.add_cog(Hockeylover(bot))
