
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



#-------INSERT---------#


conn.execute("INSERT INTO MOVIEDB (ID,MOVIE_NAME,ACTOR_NAME,ACTRESS_NAME,YEAR_OF_RELEASE,DIRECTOR_NAME) \
      VALUES (1,'YJHD','RANBIR','DEEPIKA',2017,'YRF')");
conn.execute("INSERT INTO MOVIEDB (ID,MOVIE_NAME,ACTOR_NAME,ACTRESS_NAME,YEAR_OF_RELEASE,DIRECTOR_NAME) \
      VALUES (2,'ZNMD','HRITIK','KATRINA',2015,'MADMAX')");
conn.execute("INSERT INTO MOVIEDB (ID,MOVIE_NAME,ACTOR_NAME,ACTRESS_NAME,YEAR_OF_RELEASE,DIRECTOR_NAME) \
      VALUES (3,'SPIDER MAN','TOM','ZENDAYA',2021,'MARVEL')");
#ADD MULTIPLE MOVIES AFTER THIS
conn.commit()
print ("Records created successfully")


#------READ----------#

cursor = conn.execute("SELECT * from MOVIEDB")
for row in cursor:
   print ("ID = ", row[0])
   print ("MOVIE_NAME = ", row[1])
   print ("ACTOR_NAME = ", row[2])
   print ("ACTRESS_NAME = ", row[3])
   print ("YEAR_OF_RELEASE  = ", row[4])
   print ("DIRECTOR_NAME  = ", row[5], "\n")

print ("READ Operation done successfully")



#------UPDATE--------#

conn.execute("UPDATE MOVIEDB set YEAR_OF_RELEASE = 2022 where ID = 1")
conn.commit()


cursor = conn.execute("SELECT * from MOVIEDB")
for row in cursor:
   print ("ID = ", row[0])
   print ("MOVIE_NAME = ", row[1])
   print ("ACTOR_NAME = ", row[2])
   print ("ACTRESS_NAME = ", row[3])
   print ("YEAR_OF_RELEASE  = ", row[4])
   print ("DIRECTOR_NAME  = ", row[5], "\n")

print ("UPDATE Operation done successfully")



#------DELETE-------#


conn.execute("DELETE from MOVIEDB where ID = 1;")
conn.commit()


cursor = conn.execute("SELECT * from MOVIEDB")
for row in cursor:
   print ("ID = ", row[0])
   print ("MOVIE_NAME = ", row[1])
   print ("ACTOR_NAME = ", row[2])
   print ("ACTRESS_NAME = ", row[3])
   print ("YEAR_OF_RELEASE  = ", row[4])
   print ("DIRECTOR_NAME  = ", row[5], "\n")

print ("DELETE Operation done successfully")
conn.close()
