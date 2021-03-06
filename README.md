# Devon-Bot Installation
[Install Docker](https://docs.docker.com/engine/getstarted/linux_install_help/)

This is how you should run the bot each time. It will mount your data and will be stored on the host machine at $HOME/data. Adding -g to the end will make it pull from the github if it's cached an older version.

` docker run -itv $HOME/data:/Red-DiscordBot/data devonpmack/discordbot`

In order to leave the bot always on, you must run it in detached mode. First, after running the bot normally and doing the first time setup, press CTRL-C to exit the bot. Next run the bot again with this command:

`docker run -itv $HOME/data:/Red-DiscordBot/data -d devonpmack/discordbot`

The bot should now be running in the background.

***
![intro](http://i.imgur.com/RgGlNpQ.jpg)
# Red - A fully customizable Discord bot
#### *Music, admin, trivia, fun commands and much more!*
[<img src="https://img.shields.io/badge/Support-me!-orange.svg">](https://www.patreon.com/Twentysix26)  [<img src="https://img.shields.io/badge/discord-py-blue.svg">](https://github.com/Rapptz/discord.py) [<img src="https://discordapp.com/api/guilds/133049272517001216/widget.png?style=shield">](https://discord.gg/red) [![Build Status](https://travis-ci.org/Twentysix26/Red-DiscordBot.svg?branch=develop)](https://travis-ci.org/Twentysix26/Red-DiscordBot)

> **Red** is a fully modular bot which comes with sets of features/commands that can be enabled/disabled to your liking, making it customizable exactly how you want.  
You can turn Red into a trivia bot, an admin bot, a music bot (...) or all of these together.  

The default set of modules includes and it's not limited to:
* Moderation features (kick/ban/softban, filters, mod-log...)
* Trivia (lists included and you can make new ones!)
* Music features (playlists, youtube, soundcloud, queues...)
* Stream alerts (twitch/hitbox)
* Slot machines (yes, really!)
* Custom commands
* Imgur/gif search
* And much much more

# How to install this?

The installation process is as straightforward as ever, all major platforms are supported: 
* [Windows](https://twentysix26.github.io/Red-Docs/red_install_windows/)
* [Linux](https://twentysix26.github.io/Red-Docs/red_install_linux/)
* [macOS](https://twentysix26.github.io/Red-Docs/red_install_mac/)

Don't forget to read the [getting started](https://twentysix26.github.io/Red-Docs/red_getting_started/) guide to quickly learn about the main features of Red.

If you have any other questions, feel free to explore the [Wiki](https://twentysix26.github.io/Red-Docs/) for guidance.

If [*after reading the guides*](https://twentysix26.github.io/Red-Docs/) you're still experiencing issues that are not listed in [this page](https://twentysix26.github.io/Red-Docs/red_guide_troubleshooting/) or in the [FAQs](https://twentysix26.github.io/Red-Docs/red_faq/), feel free to join the [official server](https://discord.gg/0k4npTwMvTpv9wrh) with your main account to get some help.  
Have fun!

# Join the community!

Red is in continuous development, new features get added all the time and it's supported by an active community that produces lots of content (plugins!) for everyone to enjoy. Stay tuned by [joining the official server](https://discord.gg/0k4npTwMvTpv9wrh)!

# License

Released under the [GNU GPL v3](LICENSE).

*Red is named after the main character of "Transistor", a videogame by [Supergiant Games](https://www.supergiantgames.com/games/transistor/)*
