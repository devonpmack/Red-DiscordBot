import discord
import requests
import json
import aiohttp
from discord.ext import commands

class champgg2:

    def __init__(self, bot):
        self.bot = bot
        self.apikey = "b096f8311a7c35406547e0b38363f0ee"

    @commands.command()
    async def build(self, *, champ, role):
        """Channel your inner Devon and get the highest winrate build"""
        url = "http://api.champion.gg/champion/" + champ + "/?api_key=" + self.apikey

        request = requsts.get(url)
        data = request.json()

        for i in range(0, len(data)):
            if data[i]['role'] == role:
                roleNum = i
                break

        for i in range(0, 5):
            items[i] = str(data[roleNum]['items'][i]['name'])

        for i in items:
            say = i + " > "

        await self.bot.say(say)

def setup(bot):
    bot.add_cog(lolwiki(bot))
