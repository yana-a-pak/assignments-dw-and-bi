# 1.Data Modeling with PostgreSQL

## Get Start on Codespaces

Install psycopg2
`````````````````````````````````````````````
pip install psycopg2
`````````````````````````````````````````````
docker nginx
`````````````````````````````````````````````
docker run -p 8080:80 nginx
`````````````````````````````````````````````

**Port**  

* 8080 = Adminer
* 5432 = Postgres

## Running Postgres

`````````````````````````````````````````````
docker compose up
`````````````````````````````````````````````

Connect postgres and login: http://localhost:8080/

* System: PostgreSQL
* Server: postgres
* Username: postgres
* Password: postgres
* Database: postgres

## Insert your `code` here

create table:
`````````````````````````````````````````````
python create_tables.py
`````````````````````````````````````````````

insert data into tables:
`````````````````````````````````````````````
python etl.py
`````````````````````````````````````````````

### Close webserver

To shutdown, press Ctrl+C and run: 
`````````````````````````````````````````````
docker compose down
`````````````````````````````````````````````


## Entity Relationship (ER) Diagram

Image:
![](https://github.com/yana-a-pak/Assignments-dw-and-bi/blob/main/01-data-modeling-i/ERD-01%20DW%20%26%20BI.png)