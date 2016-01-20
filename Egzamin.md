####Zadania

#####Dane

Ściągamy json stąd: https://dl.dropboxusercontent.com/u/15056258/mongodb/media.zip 

Json zawiera 1,769,759 rekordów

#####Import do mongo
Zapisujemy dane poleceniem : 

```sh
mongorestore --drop -d test -c youtube /Users/aidem/Desktop/zadanie1neo4js/Data/media/youtube.bson
```
Sprawdzamy przykladowy rekord:
```javascript   
> db.youtube.findOne()
{
	"_id" : ObjectId("55f15665c7447c3da70b5519"),
	"id" : "--0zjb5SZck",
	"uploader" : "FCLEANDROELEONARDO",
	"upload_date" : "2011-08-30",
	"title" : "Leandro & Leonardo - Cerveja - Videoclipe Oficial",
	"description" : "Videoclipe Oficial Da Música \" Cerveja \" Em 1997 ! Pra Matar As Saudades !!!",
	"duration" : "204",
}
```

#####Aby wykonać jakieś ciekawe agregacje, musimy najpierw przekonwertowac nasze dane ze stringow:
	
#####Zamieniamy pole "duration" na wartosc INT i zapisujemy w polu durationtonumber:

```javascript 	
	db.youtube.find().forEach(function(doc) {
	doc.durationtonumber = new NumberInt(doc.duration);
    	db.youtube.save(doc);
	});
```	

#####Następnie pole "upload_date" na wartosc DATE i zapisujemy w polu uploadtodate:

```javascript 	
	db.youtube.find().forEach(function(doc) {
    	doc.uploadtodate = new Date(doc.upload_date);
    	db.youtube.save(doc);
	});
```	

#####Teraz nasz dane wyglądają tak:

```javascript
	> db.youtube.findOne()
{
	"_id" : ObjectId("55f15665c7447c3da70b5519"),
	"id" : "--0zjb5SZck",
	"uploader" : "FCLEANDROELEONARDO",
	"upload_date" : "2011-08-30",
	"title" : "Leandro & Leonardo - Cerveja - Videoclipe Oficial",
	"description" : "Videoclipe Oficial Da Música \" Cerveja \" Em 1997 ! Pra Matar As Saudades !!!",
	"duration" : "204",
	"durationtonumber" : 204,
	"uploadtodate" : ISODate("2011-08-30T00:00:00Z")
}
```

Ciekawostka: obie operacje zajęły około 20 minut, dla wszystkich 1769759 rekordów.

####Agregacje

#####Przykładowe agregacje w javascript:
	
#####1. Zwróć całkowitą sumę długości wszystkich filmów wrzuconych na youtube:

```javascript 	
	>db.youtube.aggregate({$group:{_id:"result",length:{$sum: "$durationtonumber"}}})
```
```javascript 
	{ "_id" : "Total", "length" : 855414093 }
```

Jest to suma długości wszystkich filmów wrzuconych na youtube w minutach. W sumie:  ~ 14,256,901 godzin.
	
#####2. Wyświetl 10 najbardziej aktywnych uploaderów:
 
```javascript 	
db.youtube.aggregate({ $group: { _id: "$uploader", NumberOfUploads: { $sum: 1 } } } ,
{ $sort: { NumberOfUploads: -1 } }, { $limit: 10 })
```
```javascript 	
{ "_id" : "IGNentertainment", "NumberOfUploads" : 104635 }
{ "_id" : "TEDxTalks", "NumberOfUploads" : 52275 }
{ "_id" : "StarMakerApp", "NumberOfUploads" : 48709 }
{ "_id" : "BBC", "NumberOfUploads" : 17725 }
{ "_id" : "gamespot", "NumberOfUploads" : 16340 }
{ "_id" : "TheYoungTurks", "NumberOfUploads" : 16087 }
{ "_id" : "ubisoft", "NumberOfUploads" : 7660 }
{ "_id" : "CrossFitHQ", "NumberOfUploads" : 6931 }
{ "_id" : "amctheatres", "NumberOfUploads" : 6811 }
{ "_id" : "Cisco", "NumberOfUploads" : 5149 }
```

#####3. Pokaż liczbę wrzuconych filmów w poszczególnych latach:

Dla 2015:

```javascript 
>db.youtube.aggregate( [
  { $match: { uploadtodate: { $gte : new ISODate("2015-01-01T00:00:00Z"), $lte : new ISODate("2015-12-31T23:59:59Z")  } } },
  { $group: { _id: null, count: { $sum: 1 } } }
] );
```
```javascript 
		{ "_id" : null, "count" : 753685 }
```

Dla 2006:

```javascript 		
>db.youtube.aggregate( [
  { $match: { uploadtodate: { $gte : new ISODate("2006-01-01T00:00:00Z"), $lte : new ISODate("2006-12-31T23:59:59Z")  } } },
  { $group: { _id: null, count: { $sum: 1 } } }
] );
```
```javascript 
		{ "_id" : null, "count" : 7027 }
```

itd. Jak widać liczba wrzucanych filmów nieźle wzrosła przez te lata.
		
#####4. Srednia dlugosc filmikow w danym roku:
```javascript 		
>db.youtube.aggregate( [
  { $match: { uploadtodate: { $gte : new ISODate("2006-01-01T00:00:00Z"), $lte : new ISODate("2006-12-31T23:59:59Z")  } } },
  { $group: { _id: null, AverageLength: { $avg: "$durationtonumber"} } }
] );
```
```javascript 
		{ "_id" : null, "AverageLength" : 194.72264124092786 }
```

CODECOPY

from pymongo import MongoClient
import pprint
from datetime import datetime
client = MongoClient()
db = client.test



def Menus():
	print("Choose aggregation by letter:\n\n")
	print("a - Show summary duration of all uploaded videos\n")
	print("u - Show X most active users\n")
	print("l - Show number of videos uploaded year X\n")
	print("g - Find count of movies shorter than 1 min\n\n")


	userChoice = raw_input("Choose option:")

	if userChoice == 'a':
		AllVideosDuration
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
		print i

def MostActiveUsers():

	myagg = [
	{ "$group": { "_id": "$uploader", "NumberOfUploads": { "$sum": 1 } } } ,
	{ "$sort": { "NumberOfUploads": -1 } }, { "$limit": 10 }
	]

  	query = db.youtube.aggregate(myagg)

	for i in query:
		print i

def VideosCountYear():
	myagg = [
	{ "$match": { "uploadtodate": { "$gte" : datetime(2015, 1, 1), "$lte" : datetime(2015, 12, 31)  } } },
  	{ "$group": { "_id": "null", "count": { "$sum": 1 } } }
	]
	query = db.youtube.aggregate(myagg)

	for i in query:
		print i

def AverageVideoLengthYear():
	myagg = [
	{ "$match": { "uploadtodate": { "$gte" : datetime(2015, 1, 1), "$lte" : datetime(2015, 12, 31)  } } },
  	{ "$group": { "_id": "null", "count": { "$sum": 1 } } }
	]
	
	query = db.youtube.aggregate(myagg)

	for i in query:
		print i

#Menus()

VideosCountYear()
	
