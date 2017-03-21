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
    async def build(self, role, *, champ):
        """Channel your inner Devon and get the highest winrate build"""
        url = "http://api.champion.gg/champion/" + champ + "/?api_key=" + self.apikey
        items = []
        say = ""

        role = role.lower()
        champ = champ.replace(' ', '')

        shorthand = {

            'mid':'middle',
            'bot':'adc',
            'jg':'jungle',
            'sup':'support',
            'supp':'support'

        }

        if role in shorthand.keys():
            role = shorthand[role]

        request = requests.get(url)
        data = request.json()

        roleNum = -1

        for i in range(0, len(data)):
            if data[i]['role'].lower() == role:
                roleNum = i
                break

        if roleNum < 0:
            await self.bot.say("Couldn't find that champion/role combination.")

        await self.bot.say("Build winrate: " + str(data[roleNum]['items']['highestWinPercent']['winPercent']) + "\% over " + str(data[roleNum]['items']['highestWinPercent']['games']) + " games")

        for i in range(0, 6):
             items.append(str(data[roleNum]['items']['highestWinPercent']['items'][i]['name']))

        for i in range(0, 5):
            say += items[i] + " > "

        await self.bot.say(say + items[5])

def setup(bot):
    bot.add_cog(champgg2(bot))
