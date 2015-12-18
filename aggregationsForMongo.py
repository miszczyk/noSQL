from pymongo import MongoClient
import pprint

client = MongoClient()
db = client.test



def Menus():
	print("Choose aggregation by letter:\n\n")
	print("f - Find uploader named: FCLEANDROELEONARDO\n")
	print("s - Check word sex occurences in text\n")
	print("l - Find movies longer than 9998 min\n")
	print("g - Find count of movies shorter than 1 min\n\n")


	userChoice = raw_input("Choose option:")

	if userChoice == 'f':
		PrintUploader()
	elif userChoice == 's':
		CheckSexOccurence()
	elif userChoice == 'l':
		CheckNumberOfMoviesLongerThan9000()
	elif userChoice == 'g':
		CheckNumberOfMoviesShorter()
	else:
		Menus()

def PrintUploader():
	result = db.youtube.find({'uploader':'FCLEANDROELEONARDO'})
	for i in result:
		print i

def CheckSexOccurence():
	number = db.youtube.count({"description": {'$regex' : '.*' + 'sex' + '.*'}})
	print number
	return

def CheckNumberOfMoviesLongerThan9000():
	length = db.youtube.find({"duration": {"$gt": "9998"}})
	for j in length:
		print j
		print "\n\n"

def CheckNumberOfMoviesShorter():
	desc = db.youtube.count({"duration": {"$lt": "1"}})
	print desc

Menus()
#PrintUploader()
#CheckSexOccurence()
#CheckNumberOfMoviesLongerThan9000()
#CheckNumberOfMoviesShorter()


