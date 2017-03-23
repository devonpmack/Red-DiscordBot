FROM iron/python
RUN echo Devon-Bot Docker Project
ENTRYPOINT ["/Red-DiscordBot/setup.sh"]
RUN apk upgrade
RUN apk update
RUN apk add git
RUN apk add wget
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN git clone -b develop --single-branch https://github.com/devonpmack/Red-DiscordBot.git Red-DiscordBot
RUN apk add linux-headers \
	make \
	py-cffi \
	python-dev \
	musl-dev \
	gcc \
	openssl-dev \
	libffi-dev \
	ffmpeg \
	opus-dev \
	python3-dev \
	libc-dev \
	py-configobj \
	libusb \
	py-cryptography
RUN python3 /Red-DiscordBot/launcher.py --update-reqs
RUN chmod 755 /Red-DiscordBot/setup.sh
