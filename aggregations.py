from pymongo import MongoClient
import pprint
from datetime import datetime
client = MongoClient()
db = client.test



def Menus():
	print("Choose aggregation by letter:\n\n")
	print("a - Show summary duration of all uploaded videos\n")
	print("u - Show X most active users\n")
	print("l - Show number of videos uploaded in X year\n")
	print("g - Show duration of videos upladed in X year\n\n")


	userChoice = raw_input("Choose option:")

	if userChoice == 'a':
		AllVideosDuration()
	elif userChoice == 'u':
		MostActiveUsers()
	elif userChoice == 'l':
		VideosCountYear()
	elif userChoice == 'g':
		AverageVideoLengthYear()
	else:
		Menus()

def AllVideosDuration():
	myagg = [
	{"$group":{"_id":"result","length":{"$sum": "$durationtonumber"}}}
	]
	
  	mydata = db.youtube.aggregate(myagg)

	for i in mydata:
		print "All videos uploaded duration summary:\n"
		print "Minutes",i["length"], "   Hours",i["length"]/60

def MostActiveUsers():

	myagg = [
	{ "$group": { "_id": "$uploader", "NumberOfUploads": { "$sum": 1 } } } ,
	{ "$sort": { "NumberOfUploads": -1 } }, { "$limit": 10 }
	]

  	query = db.youtube.aggregate(myagg)

	for i in query:
		print "Uploaded by: " + i["_id"],"   Number of uploads:", i["NumberOfUploads"]

def VideosCountYear():

	print "\nChoose range of years (value have to be between 2005 and 2015)"
	dateFrom = raw_input("From\n")
	dateTo = raw_input("To\n")
	if dateFrom > dateTo:
		print "\n Wrong values, try again! \n"
		Menus()
		return

	counter = int(dateTo) - int(dateFrom)
	if counter > 10:
		print "\n Wrong values, try again! \n"
		Menus()
		return

	counter += 1

	for k in range(counter):
		myagg = [
		{ "$match": { "uploadtodate": { "$gte" : datetime(int(dateFrom), 1, 1), "$lte" : datetime(int(dateFrom), 12, 31)  } } },
	  	{ "$group": { "_id": "null", "count": { "$sum": 1 } } }
		]
		query = db.youtube.aggregate(myagg)

		for i in query:
			print "Year: " , dateFrom , "   Videos Count: " , i["count"]

		dateFrom = int(dateFrom) + 1

def AverageVideoLengthYear():

	print "\nChoose range of years (value have to be between 2005 and 2015)"
	dateFrom = raw_input("From\n")
	dateTo = raw_input("To\n")
	if dateFrom > dateTo:
		print "\n Wrong values, try again! \n"
		Menus()
		return

	counter = int(dateTo) - int(dateFrom)
	if counter > 10:
		print "\n Wrong values, try again! \n"
		Menus()
		return

	counter += 1

	for k in range(counter):
		myagg = [
		{ "$match": { "uploadtodate": { "$gte" : datetime(int(dateFrom), 1, 1), "$lte" : datetime(int(dateFrom), 12, 31)  } } },
    	{ "$group": { "_id": "null", "AverageLength": { "$avg": "$durationtonumber"} } }
		]
		query = db.youtube.aggregate(myagg)

		for i in query:
			print "Year: " , dateFrom , "   Average videos duration: " , i["AverageLength"]

		dateFrom = int(dateFrom) + 1

Menus()





