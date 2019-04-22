#DROP TABLES

songs_in_session_drop = """DROP TABLE IF EXISTS songs_in_session"""
songs_per_user_drop = """DROP TABLE IF EXISTS songs_per_user"""
users_per_song_drop = """DROP TABLE IF EXISTS users_per_song"""

#CREATE TABLES

songs_in_session_create = """CREATE TABLE IF NOT EXISTS songs_in_session \
                                    ( \
                                        artist text, \
                                        song_title text, \
                                        song_length double, \
                                        session_id int, \
                                        item_in_session int, \
                                        PRIMARY KEY (session_id, item_in_session) \
                                    )"""
songs_per_user_create = """CREATE TABLE IF NOT EXISTS songs_per_user \
                                    ( \
                                        artist text, \
                                        song_title text, \
                                        user_id int, \
                                        first_name text, \
                                        last_name text, \
                                        session_id int, \
                                        item_in_session int, \
                                        PRIMARY KEY ((user_id, session_id), item_in_session) \
                                    )"""

users_per_song_create = """CREATE TABLE IF NOT EXISTS users_per_song \
                                    ( \
                                        song_title text, \
                                        user_id int, \
                                        first_name text, \
                                        last_name text, \
                                        PRIMARY KEY (song_title, user_id) \
                                    )"""


# INSERT DATA IN TABLES
songs_in_session_insert = """INSERT INTO songs_in_session \
                                (artist, song_title, song_length, session_id, item_in_session) \
                                VALUES (%s, %s, %s, %s, %s) \
                          """ 

songs_per_user_insert = """INSERT INTO songs_per_user \
                                (artist, song_title, user_id, first_name, last_name, session_id, item_in_session) \
                                VALUES (%s, %s, %s, %s, %s, %s, %s) \
                        """

users_per_song_insert = """INSERT INTO users_per_song \
                                (song_title, user_id, first_name, last_name) \
                                VALUES (%s, %s, %s, %s)
                        """

#SELECT QUERIES FOR TESTING

songs_in_session_test_select = """SELECT artist, song_title, song_length \
                                  FROM songs_in_session WHERE session_id=338 AND item_in_session=4 \
                               """

songs_per_user_test_select = """SELECT artist, song_title, item_in_session, first_name, last_name \
                                FROM songs_per_user WHERE user_id=10 AND session_id=182 \
                             """

users_per_song_test_select = """SELECT first_name, last_name, song_title \
                                FROM users_per_song WHERE song_title='All Hands Against His Own'\
                             """

drop_table_queries = [songs_in_session_drop, songs_per_user_drop, users_per_song_drop]
create_table_queries = [songs_in_session_create, songs_per_user_create, users_per_song_create]
