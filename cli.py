# cli.py

import requests
import argparse

def query_data(api_url, title):
    response = requests.get(api_url + f'/query_data?title={title}')
    data = response.json()
    
    if data:
        print(f"Título: {data[0]['title']}")
        print(f"Descripción: {data[0]['description']}")
    else:
        print("No se encontraron datos para el título proporcionado.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Consultar datos desde system_module_2.")
    parser.add_argument('title', type=str, help='Título a consultar')
    args = parser.parse_args()

    system_module_2_api_url = 'https://technical-test-404920.ue.r.appspot.com/'
    query_data(system_module_2_api_url, args.title)
