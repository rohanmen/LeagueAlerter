import string

API_KEY = "5bb381bb-530e-4e03-a14a-cb7e6ab3e69a"
BASE_URL = "https://global.api.pvp.net/"
SUMMONER_VERSION = "1.4"
STATS_VERSION = "2.5"

def log(data):
	print data

def getApiKey():
	return API_KEY

def getBaseUrl():
	return BASE_URL

def replace(original, tag, value):
	return string.replace(original, tag, value)

def getSummonerVersion():
	return SUMMONER_VERSION

def getStatsVersion():
	return STATS_VERSION