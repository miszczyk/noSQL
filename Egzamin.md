Ściągamy json stąd: <link>

Zapisujemy dane polecenim : <polecenie>
   
Sprawdzamy przykladowy rekord:
   
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

	Aby wykonać jakieś ciekawe agregacje, musimy najpierw przekonwertowac nasze dane ze stringow:
	
	Zamieniamy pole "duration" na wartosc INT i zapisujemy w polu durationtonumber:
	
	db.youtube.find().forEach(function(doc) {
	doc.durationtonumber = new NumberInt(doc.duration);
    	db.youtube.save(doc);
	});
	
	Następnie pole "upload_date" na wartosc DATE i zapisujemy w polu uploadtodate:
	
	db.youtube.find().forEach(function(doc) {
    	doc.uploadtodate = new Date(doc.upload_date);
    	db.youtube.save(doc);
	});
	
	Teraz nasz dane wyglądają tak:
	
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
	"durationINT" : 0,
	"uploadtodate" : ISODate("2011-08-30T00:00:00Z")
}

	Ciekawostka: obie operacje zajęły około 20 minut, dla wszystkich 1769759 rekordów.

3. Przykładowe agregacje w javascript:
	
	1. Zwroc calkowita sume dulgosci, wszystkich wrzuconych filmow
	
	>db.youtube.aggregate({$group:{_id:"result",length:{$sum: "$durationtonumber"}}})

   
	zwraca:

	{ "_id" : "Total", "length" : 855414093 }

	Jest to suma długości wszystkich filmów wrzuconych na youtube w minutach. W sumie:  ~ 14,256,901 godzin.
	
	2. Wyswietl 10 najbardziej aktywnych uploaderow:
	
	db.youtube.aggregate({ $group: { _id: "$uploader", NumberOfUploads: { $sum: 1 } } } , { $sort: { NumberOfUploads: -1 } }, { $limit: 10 })

	wynik:
	
	> db.youtube.aggregate({ $group: { _id: "$uploader", NumberOfUploads: { $sum: 1 } } } , { $sort: { NumberOfUploads: -1 } }, { $limit: 10 })
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

	3. Suma wrzuconych filmow w poszczegolnych latach:
		Dla 2015:
		db.youtube.aggregate( [
  { $match: { uploadtodate: { $gte : new ISODate("2015-01-01T00:00:00Z"), $lte : new ISODate("2015-12-31T23:59:59Z")  } } },
  { $group: { _id: null, count: { $sum: 1 } } }
] );

		wynik:
		{ "_id" : null, "count" : 753685 }
		
		Dla 2006:
		
		db.youtube.aggregate( [
  { $match: { uploadtodate: { $gte : new ISODate("2006-01-01T00:00:00Z"), $lte : new ISODate("2006-12-31T23:59:59Z")  } } },
  { $group: { _id: null, count: { $sum: 1 } } }
] );

		wynik:
		{ "_id" : null, "count" : 7027 }
		
		itd. Jak widac liczba wrzucanych filmow niezle wzrosla przez te lata.
		
		
		
		4. Srednia dlugosc filmikow w danym roku:
		
			db.youtube.aggregate( [
  { $match: { uploadtodate: { $gte : new ISODate("2006-01-01T00:00:00Z"), $lte : new ISODate("2006-12-31T23:59:59Z")  } } },
  { $group: { _id: null, AverageLength: { $avg: "$durationtonumber"} } }
] );

		wynik:
		
		{ "_id" : null, "AverageLength" : 194.72264124092786 }
	
	
	
