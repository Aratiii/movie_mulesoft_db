# movie_mulesoft_db

# Description
Creating a database, storing interesting movie names with the names of lead actor, actress, year of release and the director name. Once stored the details, retrive the data using python .

## Installation

Install python3 in the system.

```bash
sudo apt install python3
```

## Create Database

```python
import sqlite3

conn = sqlite3.connect('movie_mulesoft.db')
print ("Opened database successfully");

#---------CREATE-------#

conn.execute('''CREATE TABLE MOVIEDB
         (ID INT PRIMARY KEY     NOT NULL,
         MOVIE_NAME           TEXT    NOT NULL,
         ACTOR_NAME           TEXT    NOT NULL,
         ACTRESS_NAME         TEXT   NOT NULL,
         YEAR_OF_RELEASE      DATE  NOT NULL,
         DIRECTOR_NAME        TEXT     NOT NULL);''')
print ("Table created successfully")



```
## CRUD Operation
![Screenshot (34)](https://user-images.githubusercontent.com/98219585/196144104-680b95fc-f462-452c-9db6-0688a76f38dc.png)




