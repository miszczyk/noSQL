1. Ściągamy json stąd: <link>
2. Zapisujemy dane polecenim : <polecenie>
   
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

3. Aby wykonać ciekawe agregacje na naszych danych, najpierw konwertujemy pole "duration" do zmiennej int poleceniem:

   db.youtube.find().forEach(function(doc) {
    doc.durationtonumber = new NumberInt(doc.duration);
    db.youtube.save(doc);
});

zwraca:

{ "_id" : "Total", "length" : 855414093 }

Jest to suma długości wszystkich filmów wrzuconych na youtube w minutach. W sumie:  ~ 14,256,901 godzin.
