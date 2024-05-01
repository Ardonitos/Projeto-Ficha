"""
Record Management System
Runs the Web Application, with an API to make the connection of front-end to back-end.
"""

from os import getenv
from dotenv import load_dotenv
from flask import Flask, jsonify, request, render_template
from pg_manager import db_connect, CrudOperations
from aux_fuctions import read_conversor, float_conversor


# Load environment variables
load_dotenv()

# Get database credentials from environment variables
DBNAME, DBUSER, DBPASSWORD = getenv('DBNAME'), getenv('DBUSER'), getenv('DBPASSWORD')

# Connect to the database
conn, cur = db_connect(DBNAME, DBUSER, DBPASSWORD)
operations = CrudOperations(conn, cur)

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def register_page():
    """
    Renders the register page.

    :returns: str: The rendered HTML template for the register page.
    """
    return render_template('cadastro.html')
    
@app.route('/consulta')
def consultation_page():
    """
    Renders the consultation page.

    :returns: str: The rendered HTML template for the consultation page.
    """
    return render_template('consulta.html')
    
@app.route('/atualizar')
def update_page():
    """
    Renders the update page.

    :returns: str: The rendered HTML template for the update page.
    """
    return render_template('atualizar.html')

@app.route('/read', methods=['POST'])
def read_db():
    """
    Reads data from the database based on the provided input.

    :returns: str: JSON response containing the retrieved data.
    """
    data_request: dict = request.get_json()
    data = list(data_request.values())
    rows = operations.read_all_data(data)
    return jsonify(read_conversor(rows))

@app.route('/insert', methods=['POST'])
def insert_into_db():
    """
    Inserts data into the database based on the provided input.

    :returns: str: JSON response indicating the success of the operation.
    """
    data_request: dict = request.get_json()
    data = list(data_request.values())
    data.insert(0, operations.max_id()) # Insert the next row ID
    operations.insert_data(float_conversor(data))
    return jsonify('Success')
    
@app.route('/update', methods=['PUT'])
def update_row():
    """
    Updates data in the database based on the provided input.

    :returns: str: JSON response indicating the success of the operation.
    """
    data_request: dict = request.get_json()
    data = list(data_request.values())
    operations.update_data(data)
    return jsonify('Success')

# Run the Flask app
app.run()
