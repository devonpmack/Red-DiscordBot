import discord
import requests
import json
import aiohttp
from discord.ext import commands

class lolwiki:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def champ(self, *, champ):

        url = "http://ddragon.leagueoflegends.com/cdn/7.4.3/data/en_US/champion/" + champ + ".json"

        request = requests.get(url)
        data = request.json()
        try:
            name = str(data['data'][champ]['name'])
            title = str(data['data'][champ]['title'])
        except:
            self.bot.say("Could not find that champion")
            return;

        self.bot.say(name + ", " + title)

def setup(bot):
    bot.add_cog(lolwiki(bot))
