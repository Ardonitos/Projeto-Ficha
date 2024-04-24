"""
Aqui está o Main desse projeto, é aqui que fará a conexão entre o front-end para o back-end por meio da API,
além de também conectar ao banco de dados PostgreSQL
"""

from os import getenv
from dotenv import load_dotenv
from datetime import date
from flask import Flask, jsonify, request, render_template
from pg_manager import db_connect, CrudOperations

def rightdateformatter(date: date):
    dateformat = date.strftime('%d-%m-%Y')
    return dateformat

def float_conversor(value: list) -> list:
    list_index = [4, 5, 6]
    for i in list_index:
        if value[i] is not None:
            value[i] = float(value[i])
    return value

def date_conversor(value: list[tuple]) -> list[list]:
    date_index = 3
    return_value = [list(i) for i in value]
    for i in return_value:
        i[date_index] = rightdateformatter(i[date_index])
        
    return return_value

def remove_none(data:list):
    for j, i in enumerate(data):
        if i is None:
            data.pop(j)
    return data
        

if __name__ == '__main__':

    load_dotenv()
    DBNAME, DBUSER, DBPASSWORD = getenv('DBNAME'), getenv('DBUSER'), getenv('DBPASSWORD')

    conn, cur = db_connect(DBNAME,DBUSER,DBPASSWORD)
    operations = CrudOperations(conn, cur)

    
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('cadastro.html')
    
    @app.route('/consulta')
    def consulta():
        return render_template('consulta.html')

    @app.route('/read', methods=['POST'])
    def read_db():
        data_request: dict = request.get_json()
        data = list(data_request.values())
        rows = operations.read_all_data(data=remove_none(data))
        print(rows)
        return jsonify(date_conversor(rows)) 

    @app.route('/insert', methods=['POST'])
    def insert_into_db():
        data_request: dict = request.get_json()
        data = list(data_request.values())
        data.insert(0, operations.max_id()+1)
        converted_data = float_conversor(data)
        print(converted_data)
        operations.insert_data(converted_data)
        return jsonify('Ok!')


    app.run(debug=True)