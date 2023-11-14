# main.py

from flask import Flask, request, jsonify
from io import StringIO  # Para leer el contenido del archivo CSV desde la solicitud
import csv

app = Flask(__name__)

# Almacenamiento en memoria para simplificar. En producción, usar Google Cloud Datastore o SQL.
data_store = []

@app.route('/')
def home():
    return "Operativo ····"

@app.route('/load_data_file', methods=['POST'])
def load_data():
    try:
        # Lee el archivo CSV desde la solicitud
        csv_data = request.files['file'].read().decode('utf-8')
        
        # Parsea el contenido del CSV
        csv_reader = csv.DictReader(StringIO(csv_data))
        data = list(csv_reader)

        # Almacena los datos
        data_store.extend(data)

        return jsonify({"message": "Datos cargados con éxito"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/load_data_json', methods=['POST'])
def load_json():
    data = request.get_json().get('data')
    data_store.extend(data)
    return jsonify({"message": "CSV cargado con éxito"})

@app.route('/query_data', methods=['GET'])
def query_data():
    # Ejemplo de punto final de consulta. Implementa según sea necesario. se puede mejorar
    title = request.args.get('title')
    result = [entry for entry in data_store if entry.get('title') == title]
    print(result)
    return jsonify(result)

# produccion
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)

# QA
#if __name__ == '__main__':
#    app.run(host='127.0.0.1', port=8080, debug=True)
