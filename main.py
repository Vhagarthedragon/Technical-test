# main.py

from flask import Flask, request, jsonify

app = Flask(__name__)

# Almacenamiento en memoria para simplificar. En producción, usar Google Cloud Datastore o SQL.
data_store = []

@app.route('/')
def home():
    return "Operativo ····"

@app.route('/load_data', methods=['POST'])
def load_data():
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

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
