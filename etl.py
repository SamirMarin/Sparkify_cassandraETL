import csv
from queries import insert_table_queries
from create_tables import create_keyspace, set_keyspace

def execute_insert(session, query, values):
    session.execute(query, values)

def insert_into_tables(session):
    file = 'event_datafile_new.csv'
    
    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader)
        for line in csvreader:
            for table, insert_query in insert_table_queries.items():
                if table == "songs_in_session":
                    values = (line[0], line[9], float(line[5]), int(line[8]), int(line[3]))
                    execute_insert(session, insert_query, values)
                elif table == "songs_per_user":
                    values = (line[0], line[9], int(line[10]), line[1], line[4], int(line[8]), int(line[3]))
                    execute_insert(session, insert_query, values)
                elif table == "users_per_song":
                    values = (line[9], int(line[10]), line[1], line[4])
                    execute_insert(session, insert_query, values)
                



def main():
    session = create_keyspace()
    set_keyspace(session)
    print("Inserting data into tables")
    print("")
    insert_into_tables(session)
    print("Data inserted")
    print("")


if __name__ == "__main__":
    main()
