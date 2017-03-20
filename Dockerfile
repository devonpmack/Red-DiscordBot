#USE wget https://raw.githubusercontent.com/devonpmack/Red-DiscordBot/develop/Dockerfile -P ./Discord to download
FROM ubuntu
ENTRYPOINT ["/Red-DiscordBot/setup.sh"]
#Install Prerequisites
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:fkrull/deadsnakes -y
RUN add-apt-repository ppa:mc3man/xerus-media -y
RUN apt-get install python3.5-dev \
	build-essential \
	libssl-dev \
	libffi-dev \
	git ffmpeg \
	libopus-dev \
	unzip -y \
	wget
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.5 get-pip.py
RUN git clone -b develop --single-branch https://github.com/devonpmack/Red-DiscordBot.git Red-DiscordBot
RUN python3 /Red-DiscordBot/launcher.py --update-reqs-no-audio
RUN chmod 755 /Red-DiscordBot/setup.sh
RUN pip3 install beautifulsoup4
RUN pip install praw
