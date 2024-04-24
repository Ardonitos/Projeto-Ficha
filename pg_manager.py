"""
Pequeno Gerenciador para pequenas operações CRUD no PostgreSQL
"""

import psycopg2
from psycopg2.extensions import connection, cursor

def verifier(data:list[str]) -> bool:
    answer = data[0].upper()
    return answer.isupper()


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
                VALUES(%s, %s, %s, %s, %s, %s, %s);
                """, data)
            self.conn.commit()
            print('Insert OK!')

        except Exception as e:
            print('Insert Fail')
            print(e.__class__.__name__, e)
            self.conn.rollback()
    
    def read_all_data(self, data:list) -> list[tuple]:
        'get all the information stored in the table'

        if len(data) == 2:
            self.cur.execute("""SELECT * FROM record_table WHERE name=%s AND date=%s ORDER BY id ASC""", data)
            rows = self.cur.fetchall()
            return rows
        elif verifier(data):
            self.cur.execute("""SELECT * FROM record_table WHERE name=%s ORDER BY id ASC""", data)
            rows = self.cur.fetchall()
            return rows
        self.cur.execute("""SELECT * FROM record_table WHERE date=%s ORDER BY id ASC""", data)
        rows = self.cur.fetchall()
        return rows
    
    def max_id(self):
        'get the max id number'
        self.cur.execute("SELECT MAX(id) FROM record_table")
        max_id = self.cur.fetchone()
        return max_id[0]
        

    def update_data(self):
        ...