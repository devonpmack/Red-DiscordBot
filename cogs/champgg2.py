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
    async def top(self, role)

        """Top 5 highest winrate champions for a role"""

        shorthand = {

            'mid':'middle',
            'bot':'adc',
            'jg':'jungle',
            'sup':'support',
            'supp':'support'

        }

        role = role.lower()

        if role in shorthand.keys():
            role = shorthand[role]

        url = "http://api.champion.gg/stats/role/" + role + "/mostWinning/?api_key=" + self.apikey

        request = requests.get(url)
        data = request.json()

        try:

            await self.bot.say("Top 5 Champions for " + role.upper())

            for i in range(0, 5):
                champ = str(data['data']['name'])
                winrate = str(data['data']['general']['winPercent'])
                playrate = str(data['data']['general']['playPercent'])
                banrate = str(data['data']['general']['banRate'])

                await self.bot.say(str(i + 1) + ". " + champ + " - Winrate: " + winrate "%, Playrate: " + playrate + "%, Banrate " + banrate + "%.")

        except:
            self.bot.say("Couldn't find data for that role")
            raise

    @commands.command()
    async def build(self, role, *, champ):
        """Channel your inner Devon and get the highest winrate build"""

        champ = champ.replace(' ', '').replace('\'', '')

        url = "http://api.champion.gg/champion/" + champ + "/?api_key=" + self.apikey
        items = []
        say = ""

        role = role.lower()

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

        try:

            for i in range(0, len(data)):
                if data[i]['role'].lower() == role:
                    roleNum = i
                    break

            await self.bot.say("Build winrate: " + str(data[roleNum]['items']['highestWinPercent']['winPercent']) + "\% over " + str(data[roleNum]['items']['highestWinPercent']['games']) + " games")

            for i in range(0, 6):
                 items.append(str(data[roleNum]['items']['highestWinPercent']['items'][i]['name']))

            for i in range(0, 5):
                say += items[i] + " > "

            await self.bot.say(say + items[5])

        except:
            self.bot.say("Couldn't find that champion/role combination.")

def setup(bot):
    bot.add_cog(champgg2(bot))
