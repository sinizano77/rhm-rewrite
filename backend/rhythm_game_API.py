import psycopg2

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

def get_rhythm_game() -> tuple:
    """ query data from the rhythm_game table """
    conn = None
    try:
        file_data = _parse_file_data()
        conn_list = open_conn(file_data[0], file_data[1], file_data[2], file_data[3], file_data[4])
        conn = conn_list[0]
        cursor = conn_list[1]
        cursor.execute('SELECT * FROM "Minigame_info"."Rhythm_game"')
        return cursor.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print("There was something wrong when trying to call the database")
        print(error)
    finally:
        if conn is not None:
            close_conn(conn)

# Running app
if __name__ == '__main__':
    get_rhythm_game()
