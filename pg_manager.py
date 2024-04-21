"""
Pequeno Gerenciador para pequenas operações CRUD no PostgreSQL
"""

import psycopg2
from psycopg2.extensions import connection, cursor
from psycopg2.sql import SQL, Identifier

def db_connect(dbname:str, user:str, password:str):
    'Conect to the database and return the connection and cursor objects'
    try:
        conn = psycopg2.connect(f"dbname={dbname} user={user} password={password}")
        cur = conn.cursor()
        print('Connection OK!')
       
        return conn, cur
    except Exception as e:
        print(e.__class__.__name__, e)

    
class CrudOperations:
    def __init__(self, conn: connection, cur: cursor):
        self.conn = conn
        self.cur = cur
        
    def insert_data(self, data):
        'inserts the data to database'
        try:
            self.cur.execute("""
                INSERT INTO record_table
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
                """, data)
            self.conn.commit()
            print('Insert OK!')

        except Exception as e:
            print('Insert Fail')
            print(e.__class__.__name__, e)
            self.conn.rollback()
    
    def read_all_data(self) -> list[tuple]:
        'get all the information stored in the table'
        self.cur.execute(SQL("""SELECT * FROM record_table ORDER BY id ASC"""))
        rows = self.cur.fetchall()
        return rows

    def read_data(self, field):
        'get some especific information in the table'
        self.cur.execute(SQL("""SELECT {} FROM record_table ORDER BY id ASC""").format(Identifier(field)))
        rows = self.cur.fetchall()
        return rows
    
    def max_id(self):
        'get the max id number'
        self.cur.execute("SELECT MAX(id) FROM record_table")
        max_id = self.cur.fetchone()
        return max_id[0]
        

    def update_data(self):
        ...