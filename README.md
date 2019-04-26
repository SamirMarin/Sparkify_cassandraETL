This is an ETL pipeline in python that creates an Apache Cassandra database which can create queries on song 
play data to answere three questions.

## The Questions
1. Give the artist, song title and song's length in the music app history that was heard during a 
    given sessionId and itemInSession?
2. Give the name of artist, song (sorted by itemInSession) and user (first and last name) for given userid and sessionid?
3. Give the user name (first and last) in my music app history who listened to a given song?

## The Dataset
There is one data set under event_data/* the files under this folder will be streamed line into a single csv file 
event_datafile_new.csv

## The ETL Pipeline
Consit of 4 python this scripts process the data, create the tables, insert the data into the tables and test the tables with
select queries

> 1. create_event_datafile_new.py streamlines the data from event_data/* into single csv file event_datafile_new.csv which 
      contains the following columns:
>>      artist, firstName of user, gender of user, item number in session, last name of user, length of the song, level (paid or free song), location of the user, sessionId, song title, userId

>>  Run with:

```
python3 create_event_datafile_new.py
```


> 2. create_tables.py creates three tables based on the three questions

>> Table 1: Creates table using columns - artis, song_title, song_length, session_id, and item_in_session
>> with PRIMARY KEY: (session_id, item_in_session), PARTITION KEY: session_id, and CLUSTERING COLUMNS item_in_session

>> Table 2: Creates table using columns - artist, song_title, user_id, first_name, last_name, session_id, item_in_session
>> with PRIMARY KEY: (user_id, session_id, item_in_session), PARTITION KEY: (user_id, session_id), and CLUSTERING COLUMNS:  item_in_session

>> Table 3: Creates table using columns - song_title, user_id, first_name, last_name,
>> with PRIMARY KEY: (song_title, user_id), PARTITION KEY: song_title, and CLUSTERING COLUMNS: user_id

>>  Run with:

```
python3 create_tables.py
```

