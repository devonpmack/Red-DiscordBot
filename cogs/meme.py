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

    @commands.command(pass_context=True, no_pm=True)
    async def kled(self, ctx):
        server = ctx.message.server
        author = ctx.message.author
        channel = author.voice_channel

        #try:
        self.has_connect_perm(author, server)
        #except AuthorNotConnected:
            #await self.bot.say("You must be in a voice channel.")
            #return

        voice = self.bot.join_voice_channel(channel)
        player = voice.create_ffmpeg_player('kled_quotes/Kled1.mp3')

def setup(bot):
    bot.add_cog(meme(bot))