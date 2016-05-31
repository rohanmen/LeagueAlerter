import util
import urllib2
import json

BASE_URL = "https://{region}.api.pvp.net/api/lol/{region}/v{version}/summoner/by-name/{summoner_name}?api_key={api_key}"

class Summoner:

	def __init__(self, summonerId, name, profileIconId, revisionDate, summonerLevel):
		self.summonerId = summonerId
		self.name = name
		self.profileIconId = profileIconId
		self.revisionDate = revisionDate
		self.summonerLevel = summonerLevel

def writeToFile(summoner):
	util.log(summoner)

def parseJson(data, name):
	jsonData = json.loads(data)
	#util.log(jsonData)

	myId = jsonData[name]["id"]
	myName = jsonData[name]["name"]
	myProfileIconId = jsonData[name]["profileIconId"]
	myRevisonDate = jsonData[name]["revisionDate"]
	mySummonerLevel = jsonData[name]["summonerLevel"]

	summoner = Summoner(myId, myName, myProfileIconId, myRevisonDate, mySummonerLevel)
	util.log(summoner.summonerId)
	util.log(summoner.name)

def getSummonerByName(region, name):

	name = util.replace(name, " ", "")

	ApiKey = util.getApiKey()
	url = BASE_URL
	url = util.replace(url, "{region}", region)
	url = util.replace(url, "{summoner_name}", name)
	url = util.replace(url, "{api_key}", ApiKey)
	url = util.replace(url, "{version}", util.getCurrentVersion())
	#util.log(url)

	summonerFound = False

	try:
		response = urllib2.urlopen(url)
		data = response.read()
		parseJson(data, name)
		summonerFound = True
	except:
		util.log("Summoner not Found")



getSummonerByName("na", "raju")


