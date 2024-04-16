"""
Pequeno Gerenciador para pequenas operações CRUD no PostgreSQL
"""


import psycopg2
from psycopg2.extensions import connection, cursor

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
    
    def read_data(self):
        'get all the information in the table'
        self.cur.execute("""SELECT * FROM record_table""")
        rows = self.cur.fetchall()
        return rows

    def update_data(self):
        ...