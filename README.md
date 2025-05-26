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