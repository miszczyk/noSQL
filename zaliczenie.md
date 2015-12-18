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

#####2c. Zliczanie rekordów

######MongoDB:
Instalacja biblioteki dla pythona: [Geojson "LineString"](img/test4.geojson "LineString")pymongo.
```sh
sudo easy_install -U setuptools
sudo python -m easy_install pymongo
sudo python -m easy_install -U pymongo
```


Wszystkie komendy znajdują się w pliku
