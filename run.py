import json
import Summoner
import Stats
import util
import sms

tier = ["BRONZE", "SILVER", "GOLD", "PLATINUM", "DIAMOND", "MASTER", "CHALLENGER"]
division = ["I", "II", "II", "IV", "V"]



#open summoner.json 
with open("summoners.json") as json_file:
    summoners = json.load(json_file)
    #print(summoners)


for s in summoners:
	summoner_name = s["summoner_name"]
	summoner_region = s["region"]

	summoner_id = s["summoner_id"]

	if summoner_id == "":
		#print summoner_name, summoner_region
		s_obj = Summoner.getSummonerByName(summoner_region, summoner_name)
		summoner_id = str(s_obj.summonerId)
		s["summoner_id"] = str(summoner_id)
		#print s_obj.print_self()

	stats = Stats.getSummonerStats(summoner_id, summoner_region)
	#stats.print_self()

	#check for change in tier and division
	#get current tier and division
	curr_division = s["division"]
	curr_tier = s["tier"]

	if curr_division != stats.division or curr_tier != stats.tier:
		util.log(summoner_name + ": stats chagned, send message")
		message = summoner_name + " is now " + stats.tier + " " + stats.division
		sms.sendToAll(message)
	else:
		util.log(summoner_name + ": no change")


	#update tier and division
	s["division"] = stats.division
	s["tier"] = stats.tier



#write json to file
with open("summoners.json", 'w') as outfile:
	json.dump(summoners, outfile, indent = 4)


	