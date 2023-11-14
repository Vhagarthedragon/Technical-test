# Technical-test
Technical-test of Michaelpage
(codigo en branch master)

# Flask Data Visualization API

Este proyecto consiste en una aplicación Flask que proporciona endpoints para cargar y consultar datos almacenados en memoria. Los datos pueden ser cargados en formato CSV y consultados mediante parámetros de consulta.

## Requisitos

- Python 3.x
- Flask
- Flask-WTF
- Gunicorn (para implementación en producción)
- (Otros requisitos según sea necesario)

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/flask-data-visualization.git
   cd flask-data-visualization

2. link del proyecto en google cloud para pruebas
   https://technical-test-404920.ue.r.appspot.com/

3. Endpoint de consulta
   https://technical-test-404920.ue.r.appspot.com/query_data?title=Confessions%20of%20an%20Invisible%20Girl #entorno produccion
   http://127.0.0.1:8080/query_data?title=Confessions%20of%20an%20Invisible%20Girl #entorno local
   ## metodo GET, query

5. Endpoint carga de datos
   https://technical-test-404920.ue.r.appspot.com/load_data_file #entorno produccion
   http://127.0.0.1:8080/load_data_file #entorno local
   ## metodo POST, multipart/form-data

 ## Almacenamiento en memoria para simplificar. En producción, considera usar Google Cloud Datastore o SQL.
