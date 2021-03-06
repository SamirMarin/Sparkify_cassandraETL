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
Consits of 4 python scripts that process the data, create the tables, insert the data into the tables and test the tables with
select queries

> 1. create_event_datafile_new.py streamlines the data from event_data/* into single csv file `event_datafile_new.csv` which 
      contains the following columns:
>>      artist, firstName of user, gender of user, item number in session, last name of user, length of the song, level (paid or free song), location of the user, sessionId, song title, userId

>>  Run with:

```
python3 create_event_datafile_new.py
```


> 2. create_tables.py creates three tables based on the three questions, note everytime you run this script it also drops tables before creating so you will have to re-insert data if you run.

>> Table 1: Creates table using columns - artis, song_title, song_length, session_id, and item_in_session
>> with PRIMARY KEY: (session_id, item_in_session), PARTITION KEY: session_id, and CLUSTERING COLUMN item_in_session

>> Table 2: Creates table using columns - artist, song_title, user_id, first_name, last_name, session_id, item_in_session
>> with PRIMARY KEY: (user_id, session_id, item_in_session), PARTITION KEY: (user_id, session_id), and CLUSTERING COLUMN:  item_in_session

>> Table 3: Creates table using columns - song_title, user_id, first_name, last_name,
>> with PRIMARY KEY: (song_title, user_id), PARTITION KEY: song_title, and CLUSTERING COLUMN: user_id

>>  Run with:

```
python3 create_tables.py
```

> 3. etl.py inserts data into the three tables from event_datafile_new.csv

>> Run with:

```
python3 etl.py
```

> 4. test_queries.py runs test select queries based on the three questions:

>> 1. Selects the artist, song title and song's length in the music app history that was heard during a 
     sessionId =338 and itemInSession=4.
>> 2. Selects the name of artist, song (sorted by itemInSession) and user (first and last name) for userid=10 and sessionid=182
>> 3. Selects the user name (first and last) in my music app history who listened to a the song=All Hands Against His Own

>> Run with:

```
python3 test_queries.py
```

These four python scripts can be run at once with a bash script: `run_etl_pipeline.sh`

To Run:

```
./run_etl_pipeline.sh
```

It should be executable but if not executable you can make executable by:

```
chmod +x run_etl_pipeline.sh
```

## Jupyter notebook
lastly there is a Jupyter notebook that can be used to accomplish what the python scripts accomplishes. Starting with the python code that stream lines the dataset into a single csv file (code given with project template). After which you will find for each question addressed:
1) A table creation statement
2) An insert statement
3) A select test statement (like the one found in the python script)

And lastly drop statements for the three tables.

