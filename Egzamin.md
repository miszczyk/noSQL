1. Ściągamy json stąd: <link>
2. Zapisujemy dane polecenim : <polecenie>
3. Aby wykonać ciekawe agregacje na naszych danych, najpierw konwertujemy pole "duration" do zmiennej int poleceniem:

   db.youtube.find().forEach(function(doc) {
    doc.durationtonumber = new NumberInt(doc.duration);
    db.youtube.save(doc);
});

zwraca:

{ "_id" : "Total", "length" : 855414093 }

Jest to suma długości wszystkich filmów wrzuconych na youtube w minutach. W sumie:  ~ 14,256,901 godzin.
