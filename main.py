"""
Aqui está o Main desse projeto, é aqui que fará a conexão entre o front-end para o back-end por meio da API,
além de também conectar ao banco de dados PostgreSQL
"""

from os import getenv
from dotenv import load_dotenv
from flask import Flask
from pg_manager import db_connect, CrudOperations





if __name__ == '__main__':

    load_dotenv()
    DBNAME, DBUSER, DBPASSWORD = getenv('DBNAME'), getenv('DBUSER'), getenv('DBPASSWORD')

    conn, cur = db_connect(DBNAME,DBUSER,DBPASSWORD)

    operations = CrudOperations(conn, cur)
    
    ...







