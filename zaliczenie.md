####Zadania
#####2a. Import pliku do bazy danych

Instalacja:
######MongoDB:
Korzystamy z homebrew (coś ala apt-get dla maca):
```sh
brew install mongodb
brew services start mongodb
```
#####PostgreSQL:
jw. korzystamy z homebrew:
```sh
brew install postgres
```

Importowanie bazy danych:
Rozpakujemy zipa pobranego z Mongo DB Json Data - YoutubeVideos (1.12 GB unpacked).
Odpalamy bazy danych i korzystamy z komend do importu.
######MongoDB:
```sh
time mongorestore --drop -d test -c youtube /Users/aidem/Desktop/zadanie1neo4js/Data/media/youtube.bson
```
Zużycie procesora:
Zużycie procesora wachało się pomiędzy 30 a 60% dla rdzeni 1 i 3, oraz 15 - 40% dla pozostałych.
![import](img/importMongoProcesory.png)

![import](img/mongoImportWykres.png)

Zużycie pamięci:

![import](img/importMongoPamiec2.png)

Czas importu:

![import](img/mongoImportCzas.png)

#####PostgreSQL:
Najpierw konwertujemy plik bson do jsona komenda:
```sh
time bsondump youtube.bson > youtube.json
```
Nastepnie korzystamy z pgfuttera (na macu korzystam z curla zamiast wgeta):
```sh
curl -o pgfutter https://github.com/lukasmartinelli/pgfutter/releases/download/v0.3.2/pgfutter_darwin_amd64clear
```
Importujemy:
```sh
./pgfutter --port "5431" --pass aidem123 json youtube.json
```
Zużycie procesora:
Zużycie procesora wachało się pomiędzy 30 a 60% dla rdzeni 1 i 3, oraz 15 - 40% dla pozostałych.
![import](img/postgresImportProcesory.png)

![import](img/postgresImportWykres.png)

Zużycie pamięci było podobne jak przy imporcie do mongo.

Czas importu:

![import](img/postgresImportCzas.png)

#####2b. Zliczanie rekordów

######MongoDB:

![import](img/zliczanieRekordowMongo.png)

Czas wyniósł 0

#####PostgreSQL:
```sql
select count(*) from import.youtube;
```
Czas wyniósł 4.45 min

#####2c. Agregacje

######MongoDB:
Instalacja biblioteki dla pythona - pymongo.
```sh
sudo easy_install -U setuptools
sudo python -m easy_install pymongo
sudo python -m easy_install -U pymongo
```


*Wszystkie komendy znajdują się w pliku ["SKRYPT"](lol "SKRYPT").

####### 1. Znajdź użytkownika wrzucającego film o nicku FCLEANDROELEONARDO
```py
>db.youtube.find({'uploader':'FCLEANDROELEONARDO'})
[
	{
		"_id" : ObjectId("55f15665c7447c3da70b5519"),
		"id" : "--0zjb5SZck",
		"uploader" : "FCLEANDROELEONARDO",
		"upload_date" : "2011-08-30",
		"title" : "Leandro & Leonardo - Cerveja - Videoclipe Oficial",
		"description" : "Videoclipe Oficial Da Música \" Cerveja \" Em 1997 ! Pra Matar As Saudades !!!",
		"duration" : "204"
	}
]
```

Realtime:	0m53.017s

####### 2. Zlicz liczbę filmów które w opisie posiadają słowo sex
```py
>db.youtube.count({"description": {'$regex' : '.*' + 'sex' + '.*'}})
11229
```

Realtime:	0m26.898s

####### 3. Znajdź filmy, które trwają dłużej niż 9998 minut
```py
> db.youtube.find({"duration": {"$gt": "9998"}})
[
	{
		"_id" : ObjectId("55f15679c7447c3da71080df"),
		"id" : "apbfC0SmPLo",
		"uploader" : "Shesellssheshells",
		"upload_date" : "2015-02-19",
		"title" : "Lets Stream DreadOut Act 2",
		"description" : "Ghosts with the almost. Co-commentary by VoidBurger (http://twitter.com/voidburger), ChipCheezum (http://twitter.com/chipcheezum), and kcgreenn (https://twitter.com/kcgreenn)\n\nLike this channel? Support it on Patreon! https://www.patreon.com/kamoc",
		"duration" : "9999"
	},
	{
		"_id" : ObjectId("55f1569ac7447c3da719783a"),
		"id" : "lDLM-dXP-KE",
		"uploader" : "UCyoTTxSCZ3vQsaFqlNi1qVg",
		"upload_date" : "2015-05-04",
		"title" : "Star Wars: The Blackened Mantle (The Prequels Rewritten / Recut)",
		"description" : "The Star Wars prequel trilogy (Episodes I-III). Re-edited, interwoven, and entirely rewritten using English subtitles over Japanese audio. A story you haven't seen.\n\n\"Star Wars: The Blackened Mantle\" chronicles the rise of a young Jedi named Anakin Skywalker. Haunted by vivid and prophetic nightmares since he was a slave on Tatooine, Anakin is trained to find peace through the Force by his friend and mentor, Jedi Master Obi-Wan Kenobi - until an act of brutal violence shatters Anakin's fragile grip on his own perilous gift.\n\nThis three-year project was inspired by a challenge unwittingly issued by Peter Sciretta of /Film: was Topher Grace's 85-minute recut trilogy genuinely the \"best possible edit of the Star Wars prequels given the footage released and available?\" To test that claim, the creators of this film turned away from the original English footage - and the original script - and pursued an option based on new research showing how our minds integrate written subtitles with spoken language. This was the result.\n\nNOTE: Unlike many other fan-edits of the prequels, \"The Blackened Mantle\" is not simply three separate films glued back-to-back with the fat cut out. It has proper dramatic pacing, new character arcs, reworked image quality, and a heavily modified plot constructed from a brand new, non-chronological script. It is not necessarily compatible with any Star Wars canon other than the original film trilogy (such as the fantastic \"Clone Wars\" animated series). Apologies go out to fluent Japanese speakers, who will likely not be able to watch the film without muting the audio.\n\nThis is a fan-made, not-for-profit edit of the Star Wars prequels. The creators have no affiliation with Twentieth Century Fox, Lucasfilm Ltd., or Walt Disney Studios.",
		"duration" : "9999"
	},
	{
		"_id" : ObjectId("55f156aac7447c3da71c13fc"),
		"id" : "OG6hdUJf4Qw",
		"uploader" : "KlausTrophobie44",
		"upload_date" : "2013-07-02",
		"title" : "Monkey Safari Live At Fusion Festival 2013 [DJ-SET]",
		"description" : "live mix from the Fusion Festival 2013 on saturday 19-22 at Tanzwiese\n\n\nhttps://soundcloud.com/monkey-safari/",
		"duration" : "9999"
	}
]
```

Realtime	0m18.679s

####### 4. Zlicz liczbę filmów trwających poniżej 1 minuty
```py
> db.youtube.count({"duration": {"$lt": "1"}})
657
```

Realtime	0m9.874s

######PostgreSQL:

####### 1. Wyświetl 3 tytuły które zaczynają się od słowa „crazy”.
```sql
SELECT data->>'title' AS title FROM import.youtube WHERE data->>'title' like ('crazy%') LIMIT 3;
```
Czas 1.2s

![import](img/postgresCrazy.png)

####### 2. Wyswietl 10 nazw flmów wraz z datą uploadu, ktore zostały wrzucone przed 14.10.2010 (pomiń 10).
```sql
SELECT data->>'upload_date' AS Upload, data->>'title' AS title FROM import.youtube WHERE data->>'upload_date' < '2010-10-14' LIMIT 10 OFFSET 10;
```
Czas 0.15s

![import](img/postgresData.png)

####### 3. Znajdz tytuły filmów wrzuconych przez użytkownika DiSonik.
```sql
SELECT data->>'uploader' AS Uploader, data->>'title' AS title FROM import.youtube WHERE data->>'uploader' = 'DiSonik';
```
Czas 0.18s

![import](img/postgresUploader.png)

#####2d. GeoJson

Pobralem geoJson z informacjami o stanach w ameryce oraz wykaz trzęsień ziemi na świecie w przeciągu ostatnich 30 dni.

Import do mongo poleceniem:
```sh
mongoimport -c states < states.json
```
Dodajemy geo-indeks:
```sh
> db.states.ensureIndex({"loc": "2dsphere"})
{
	"createdCollectionAutomatically" : false,
	"numIndexesBefore" : 1,
	"numIndexesAfter" : 2,
	"ok" : 1
}
```

Pobieramy jq:
```sh
brew install jq
```

####Mapki

["Trzęsienia ziemi"](earthquakes.geojson "Trzęsienia ziemi")
["Stany Ameryki"](states.geojson "Stany Ameryki")




