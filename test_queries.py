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
            print("Test query for table " + table)
            print("")
            print("1. Give me the artist, song title and song's length in the music app")
            print("history that was heard during sessionId = 338, and itemInSession = 4")
            print("")
            print("Query Result:")
            print("")
            for row in rows:
                print (row.artist, row.song_title, row.song_length,)

            print("")
            print("")

        elif table == "songs_per_user":
            rows = execute_select(session, select_query)
            print("Test query for table " + table)
            print("")
            print("2. Give me only the following: name of artist, song (sorted by itemInSession)") 
            print("and user (first and last name) for userid = 10, sessionid = 182")
            print("")
            print("Query Result:")
            print("")
            for row in rows:
                print (row.artist, row.song_title, row.item_in_session, row.first_name, row.last_name)

            print("")
            print("")

        elif table == "users_per_song":
            rows = execute_select(session, select_query)
            print("Test query for table " + table)
            print("")
            print("3. Give me every user name (first and last) in my music app history")
            print("who listened to the song 'All Hands Against His Own'")
            print("")
            print("Query Result:")
            print("")
            for row in rows:
                print (row.first_name, row.last_name, row.song_title,)

            print("")
            print("")


def main():
    session = create_keyspace()
    set_keyspace(session)
    print("")
    print("Testing select queries")
    print("")
    select(session)


if __name__ == "__main__":
    main()
