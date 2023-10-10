import set_password
import psycopg2

#Main body code
def main():
    file_data = _parse_file_data()
    set_password.main()
    _create_init_DB(file_data)

    conn_list = open_conn(file_data[0], file_data[1], file_data[2], file_data[3], file_data[4])
    conn = conn_list[0]
    cursor = conn_list[1]
    _create_schema(cursor)
    _create_minigame_table(cursor)
    close_conn(conn)

#parse the secret.txt for Postgres data
def _parse_file_data() -> list:
    file = open("secret.txt", "r")
    return file.readline().split(",")

#establises the connection to PostGres
def open_conn(db_name, username, pswrd, ip_address, port_num) -> list: 
    conn = psycopg2.connect(
    database=db_name, user=username, password=pswrd, host=ip_address, port=port_num
    )
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    #A cursor is an object that is used to make the connection for executing SQL queries
    cursor = conn.cursor()

    return [conn, cursor]

#Closes the Postgres connection
def close_conn(conn) -> None:
    conn.close()

#Creates initial database in PostGres - connects to default created "postgres" db just to create the actual db
def _create_init_DB(file_data: list) -> None:
    conn_list = open_conn("postgres", file_data[1], file_data[2], file_data[3], file_data[4])
    conn = conn_list[0]
    cursor = conn_list[1]
    sql = '''
            CREATE DATABASE "Rhm_Db"
            WITH
            OWNER = postgres
            ENCODING = 'UTF8'
            CONNECTION LIMIT = -1
            IS_TEMPLATE = False;
          ''';

    #Creating a database
    cursor.execute(sql)
    print("Rhm_DB database created successfully........")
    close_conn(conn)

#Creates the minigame info schema in the database
def _create_schema(cursor) -> None:
    sql = '''
            CREATE SCHEMA "Minigame_info"
            AUTHORIZATION postgres;
          ''';
    cursor.execute(sql)
    print("Minigame_info schema in Rhm_DB created successfully........")

#Creates the rhythm game table in the minigame info schema
def _create_minigame_table(cursor) -> None:
    sql = '''
            CREATE TABLE "Minigame_info"."Rhythm_game"
            (
                game_id integer NOT NULL,
                game_title character varying(50) NOT NULL,
                group_id integer NOT NULL,
                game_platform character varying(50) NOT NULL,
                point_meter boolean NOT NULL,
                skill_star boolean NOT NULL,
                two_player boolean NOT NULL,
                image_file character varying(75) DEFAULT 'no.png',
                difficulty double precision,
                PRIMARY KEY (game_id)
            );

            ALTER TABLE IF EXISTS "Minigame_info"."Rhythm_game"
            OWNER to postgres;
          ''';
    cursor.execute(sql)
    print("Rhythm_game table in Minigame_info created successfully........")

if __name__ == "__main__":
    main()