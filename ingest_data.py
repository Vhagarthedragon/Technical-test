# ingest_data.py

import csv
import requests

def ingest_data(file_path, api_url, encoding='utf-8'):
    # Leer data del csv
    with open(file_path, 'r', encoding=encoding) as file:
        csv_reader = csv.DictReader(file)
        data = list(csv_reader)

    # envio de data al api
    response = requests.post(api_url + '/load_data', json={'data': data})

    if response.status_code == 200:
        print("Data successfully ingested.")
    else:
        print(f"Error ingesting data. Status code: {response.status_code}")

if __name__ == "__main__":
    file_path = 'netflix_titles.csv'
    api_url = 'http://127.0.0.1:8080'
    
    file_encoding = 'utf-8' 
    
    ingest_data(file_path, api_url, encoding=file_encoding)
