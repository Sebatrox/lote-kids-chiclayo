import json

with open(r'c:\Users\Sebastian\Desktop\tienda-ropa\inventario.json', encoding='utf-8') as f:
    inv = json.load(f)

c1 = [p['codigo'] for p in inv if p['cantidad'] == 1]
c2 = [p['codigo'] for p in inv if p['cantidad'] == 2]
print(f"Cantidad = 1: {len(c1)} productos (badge rojo 'Ultima unidad')")
print(f"Cantidad = 2: {len(c2)} productos (badge naranja 'Quedan 2') -> {c2}")

html = open(r'c:\Users\Sebastian\Desktop\tienda-ropa\catalogo.html', encoding='utf-8').read()
print(f"\nstock-1 en HTML: {html.count('stock-1')} (1 CSS + 2 usos JS)")
print(f"stock-2 en HTML: {html.count('stock-2')} (1 CSS + 2 usos JS)")
