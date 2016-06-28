import time
import os
import random
import Contact
import json
import smtplib
import string

#create providers
CONTACTS_FILE = "contacts.json"


providers = { 'boost' : '@myboostmobile.com',
			  'tmobile' : '@tmomail.net',
			  'virgin' : '@vmobl.com',
			  'cingular' : '@cingularme.com',
			  'sprint' : '@messaging.sprintpcs.com',
			  'verizon'  : '@vtext.com',
			  'nextel' : '@messaging.nextel.com',
			  'cellular' : '@email.uscc.net',
			  'suncom' : '@tms.suncom.com',
			  'powertel' : '@ptel.net',
			  'att' : '@txt.att.net',
			  'alltell' : '@message.alltel.com',
			  'metropcs' : '@MyMetroPcs.com' }


def parseContacts(fileName):
	allContacts = []

	jsonFile = open(fileName)
	data = json.load(jsonFile)

	for i in range(len(data)):
		name = data[i]["name"]
		number = data[i]["number"]
		provider = data[i]["provider"]

		numMail = number + providers[provider]

		c = Contact.Contact(name, number, provider, numMail)

		allContacts.append(c)

	return allContacts


def send_sms(to, from_, message):
	#args = "python send_sms.py " + to + " " + from_ + " " + message
	#send_sms.send_sms(to, from_, message)
	#print args
	#os.system(args)

	gmailAddress = "DeveloperAcc88@gmail.com"
	gmailPassword = "vxsldxjqmnsfacwv"
	server = smtplib.SMTP( "smtp.gmail.com", 587 )
	server.starttls()
	server.login( gmailAddress, gmailPassword )

	#print sys.argv[0], to, from_, message

	server.sendmail(from_, to, message )
	print "sent"

def sendToAll(message):

	contacts = parseContacts(CONTACTS_FILE)
	from_ = "LeagueAlerter"
	for i in contacts:
		to = i.numMail
		send_sms(to, from_, message)



#to = "5127799193@messaging.sprintpcs.com"
#from_ = "LeagueAlerter"
#message = "test"
#send_sms(to, from_, message)


