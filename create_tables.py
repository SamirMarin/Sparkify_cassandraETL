import cassandra
from cassandra.cluster import Cluster
from queries import drop_table_queries, create_table_queries

def create_keyspace():
    """Connects to cassandra cluster and creates sparkify KeySpace"""

    cluster = Cluster()
    session = cluster.connect()

    try:
        session.execute("""
                    CREATE KEYSPACE IF NOT EXISTS sparkify 
                    WITH REPLICATION = 
                    { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
                    """
    )
    except Exception as e:
        print(e)

    return session

def set_keyspace(session):
    """Sets the sparkify KeySpace"""

    try:
        session.set_keyspace('sparkify')
    except Exception as e:
        print(e)
        

def drop_tables(session):
    """Drops tables defined in drop_table_queries if they exist"""

    for drop_table_query in drop_table_queries:
        try:
            session.execute(drop_table_query)
        except Exception as e:
            print(e)

def create_tables(session):
    """Creates tables defined in create_table_queries in they don't exsit"""

    for create_table_query in create_table_queries:
        try:
            session.execute(create_table_query)
        except Exception as e:
            print(e)

def main():
    session = create_keyspace()
    set_keyspace(session)
    drop_tables(session)
    create_tables(session)

if __name__ == "__main__":
    main()

