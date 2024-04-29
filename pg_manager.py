"""
Library for Database Operations and Data Processing
"""

import psycopg2
from psycopg2.extensions import connection, cursor
from aux_fuctions import verifier, remove_none, update_conversor


def db_connect(dbname:str, user:str, password:str) -> tuple:
    """
    Connects to the database and returns the connection and cursor objects.

    :parameters:
        dbname (str): The name of the database to connect to.
        user (str): The username for authentication.
        password (str): The password for authentication.

    :returns: tuple: A tuple containing the connection and cursor objects.
    """
    try:
        conn = psycopg2.connect(f"dbname={dbname} user={user} password={password}")
        cur = conn.cursor()
        print('Connection OK!')
        return conn, cur
    except Exception as e:
        print(e.__class__.__name__, e)

    
class CrudOperations:
    """
    A class to perform the principal methods of CRUD operations and Data Processing.
    """

    def __init__(self, conn: connection, cur: cursor):
        """
        Initializes the CrudOperations class.

        :parameters:
            conn (connection): The database connection object.
            cur (cursor): The cursor object for database operations.
        """
        self.conn = conn
        self.cur = cur
        
    def insert_data(self, data: list):
        """
        Inserts the data into the database.

        :parameters: data (list): The data to be inserted into the database.
        """
        if data[4] is not None:
            data[6] = round(data[4]-data[5], 2) # Auto Calc the Amount Due

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
    
    def read_all_data(self, data:list[str]) -> list[tuple]:
        """
        Retrieves all information stored in the table based on the provided data.

        :parameters: data (list[str]): The data used for filtering the results.
        :returns:list[tuple]: A list of tuples containing the retrieved data.
        """
        new_data = remove_none(data)

        if len(new_data) == 3:
            self.cur.execute("""SELECT * FROM record_table WHERE name=%s AND date BETWEEN %s AND %s ORDER BY id ASC""", new_data)
            rows = self.cur.fetchall()
            return rows
        elif verifier(new_data):
            self.cur.execute("""SELECT * FROM record_table WHERE name=%s ORDER BY id ASC""", new_data)
            rows = self.cur.fetchall()
            return rows
        self.cur.execute("""SELECT * FROM record_table WHERE date BETWEEN %s AND %s ORDER BY id ASC""", new_data)
        rows = self.cur.fetchall()
        return rows
    
    def max_id(self) -> int:
        """
        Retrieves the maximum ID number from the table.

        :returns: int: The maximum ID number plus one to make an auto serial.
        """
        self.cur.execute("SELECT MAX(id) FROM record_table")
        max_id = self.cur.fetchone()

        if max_id[0] is None:
            return 1

        return max_id[0]+1
        

    def update_data(self, data:list):
        """
        Updates data in the database based on the provided data.

        :parameters: data (list): The data used for updating records in the database.
        """
        try:
            data_name, data_amount, data_date = update_conversor(data)
            self.insert_data([self.max_id(), data_name, None, data_date, None, data_amount, None]) # Here we insert the payment day
            # After, our system is going to update the rows of a specific client
            self.cur.execute("SELECT * FROM record_table WHERE name=%s AND amount_due > 0", (data_name,)) 
            rows = self.cur.fetchall()
            difference = 0
            for row in rows:
                amount, amount_paid, amount_due = row[-3:]
                query_id = row[0]

                if difference == 0 and data_amount == 0:
                    break
                elif difference != 0 and difference > amount_due:
                    difference -= amount_due
                    amount_due = 0
                    amount_paid = amount
                elif difference != 0 and difference <= amount_due:
                    amount_paid += difference
                    amount_due = amount - amount_paid
                    difference = 0
                elif difference == 0 and data_amount > amount_due:
                    difference = data_amount - amount_due
                    amount_due = 0
                    amount_paid = amount
                elif difference == 0 and data_amount <= amount_due:
                    amount_paid += data_amount
                    amount_due = amount - amount_paid
                    data_amount = 0

                self.cur.execute("UPDATE record_table SET amount_paid=%s, amount_due=%s WHERE id=%s", 
                (round(amount_paid, 2), round(amount_due, 2), query_id,))
                self.conn.commit()
            print('Update OK!')

        except Exception as e:
            print('Update Fail')
            print(e.__class__.__name__, e)
            self.conn.rollback()
