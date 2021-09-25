import os

class Config(object):
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_NAME = os.environ.get("BOT_NAME")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
	UPDATES_CH = os.environ.get("UPDATES_CH")
	SUPPORT_GRP = os.environ.get("SUPPORT_GRP")
	UPDATES_NAME = os.environ.get("UPDATES_NAME")
	SUPPORT_NAME = os.environ.get("SUPPORT_NAME")
	APP_ID = int(os.environ.get("APP_ID"))
	API_HASH = os.environ.get("API_HASH")
	DATABASE_URL = os.environ.get("DATABASE_URL")
	SUDO_USERS = list(set(int(x) for x in ''.split()))
	SUDO_USERS.append(853393439)
	SUDO_USERS = list(set(SUDO_USERS))

