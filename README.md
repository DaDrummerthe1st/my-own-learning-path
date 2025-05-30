# Bank-app-handling transactions

Detta är händelseflödet för att klara uppgiften

### 1. PostgreSQL - få upp den
### 2. Bygga upp en databas med migrationsverktyget Alembic
* https://github.com/WeeHorse/python-bank-project-start
* Alembic bygger schemat
* Tittar på förändring
* Bygger databas åt oss
* Bygger kolumner av variablerna
* klasserna går 1 till 1
* Constraints byggs i Alembic men historisk data blir svårare att hantera. Kan ha svårt att identifiera nya constraints om man redan har en skapad klass
* PostgreSQL - skript
* Skriva egna migrationsfiler
* Bygga om Alembichistorik
* Alembic bygger commits (tänk Git)
### 3. ETL-flöde: Python, Pandas (ej Great Expectations)
* Implementera datarensning
* skippa rader med trasig data
* KAN dumpa raden vid provskrining till db
* Rensa annars innan provkör mot db
* key / value - pair
* Spara en csv-fil med broken data
### 4. Förbättra cleaningprocessen

## Command cheat sheet
### Create a working docker postgresql container
sudo docker run --name postgresql-bank-datakvalitet -e POSTGRES_PASSWORD=root -e POSTGRES_USER=postgres -p 5432:5432 -d postgres:latest
#### other docker commands
sudo docker ps # lists active containers
sudo docker ps -a # lists ALL containers
sudo docker restart [containerhash]
##### connect to db:
sudo docker exec -it [docker container name] psql -U [username] -d [databasename]
### Logged into postgresql:
\dt # check tables
select * from employees; # dont forget the ; sign
quit # quit
\q # also quit
### Alembic commands:
alembic revision -m "[what will this revision do?]" # create a new migration
alembic upgrade head # there are several ways of 
alembic history # see revision history
alembic current # information about current revision
alembic downgrade -1 # downgrade to previous revision


