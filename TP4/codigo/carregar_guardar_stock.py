import json
import os

def carregar_stock():
    if os.path.exists('stock.json'):
        with open('stock.json', 'r') as f:
            return json.load(f)
    else:
        return None

def guardar_stock(stock):
    with open('stock.json', 'w') as f:
        json.dump(stock, f, indent=2)