from queries import select_table_queries
from create_tables import create_keyspace, set_keyspace


def execute_select(session, select_query):
    try:
        rows = session.execute(select_query)
    except Exception as e:
        print(e)

    return rows

def select(session):
    for table, select_query in select_table_queries.items():
        if table == "songs_in_session":
            rows = execute_select(session, select_query)
            print("query for table " + table)
            print("1---------------------------->")
            for row in rows:
                print (row.artist, row.song_title, row.song_length,)

            print("---------------------------->")

        elif table == "songs_per_user":
            rows = execute_select(session, select_query)
            print("query for table " + table)
            print("2---------------------------->")
            for row in rows:
                print (row.artist, row.song_title, row.item_in_session, row.first_name, row.last_name)

            print("---------------------------->")

        elif table == "users_per_song":
            rows = execute_select(session, select_query)
            print("query for table " + table)
            print("3---------------------------->")
            for row in rows:
                print (row.first_name, row.last_name, row.song_title,)

            print("---------------------------->")


def main():
    session = create_keyspace()
    set_keyspace(session)
    select(session)


if __name__ == "__main__":
    main()
