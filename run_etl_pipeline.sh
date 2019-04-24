#!/bin/bash

#run each of the python scripts

#1 create event_data_new.csv from datafile
python3 create_event_datafile_new.py
#2 create cassandra tables
python3 create_tables.py
#3 run the etl pipeline insert data into tables
python3 etl.py
#4 test with select queries given in the questions
python3 test_queries.py

