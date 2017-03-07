#!/bin/sh
if [ "$1" == "-g" ]; then
  git pull
fi
python3 /Red-DiscordBot/launcher.py -s
