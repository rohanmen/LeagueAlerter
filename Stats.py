import util
import urllib2
import json

BASE_URL = "https://{region}.api.pvp.net/api/lol/{region}/v{version}/league/by-summoner/{summoner_id}?api_key={api_key}"

class Stats:

	def __init__(self):
		self.summonerId = ""
		self.division = ""
		self.tier = ""
		self.leaguePoints = ""


	def print_self(self):
		print "summonerId = " + self.summonerId
		print "divison = " + self.division
		print "tier = " + self.tier
		print "leaguePoints = " + self.leaguePoints

def parseJson(data, summonerId):
	jsonData = json.loads(data)

	stats = Stats();
	stats.summonerId = summonerId

	for j in jsonData[summonerId]:

		if j["queue"] == "RANKED_SOLO_5x5":
			tier = jsonData[summonerId][0]["tier"]
			stats.tier = tier

			for e in j["entries"]:
				if e["playerOrTeamId"] == summonerId:
					stats.division = e["division"]
					stats.leaguePoints = str(e["leaguePoints"])

	stats.print_self()


def getSummonerStats(summonerId, region):

	ApiKey = util.getApiKey()
	url = BASE_URL

	url = util.replace(url, "{region}", region)
	url = util.replace(url, "{summoner_id}", summonerId)
	url = util.replace(url, "{api_key}", ApiKey)
	url = util.replace(url, "{version}", util.getCurrentVersion())

	#try:
	response = urllib2.urlopen(url)
	data = response.read()
	parseJson(data, summonerId)
	#except:
		#print response.getcode()

getSummonerStats("32280833", "na")