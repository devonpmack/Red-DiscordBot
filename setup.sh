#!/bin/sh

if [ "$1" = "-g" ]
then
	git -C /Red-DiscordBot pull
fi
python3 /Red-DiscordBot/launcher.py -s
