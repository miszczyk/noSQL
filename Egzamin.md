1. Ściągamy json stąd: <link>
2. Zapisujemy dane polecenim : <polecenie>
3. Aby wykonać ciekawe agregacje na naszych danych, najpierw konwertujemy pole "duration" do zmiennej int poleceniem:

   db.youtube.find().forEach(function(doc) {
    doc.durationINT = new NumberInt(doc.duration);
    db.youtube.save(doc);
});
