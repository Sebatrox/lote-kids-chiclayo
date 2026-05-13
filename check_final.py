import json
with open(r'c:\Users\Sebastian\Desktop\tienda-ropa\inventario.json', encoding='utf-8') as f:
    inv = json.load(f)
tipos   = sorted(set(p['tipo']  for p in inv))
colores = sorted(set(p['color'] for p in inv))
sin_foto = [p for p in inv if not p['fotos']]
multi    = [p for p in inv if p['cantidad'] > 1]
print(f"Productos     : {len(inv)}")
print(f"Tipos unicos  : {len(tipos)}")
print(f"Colores unicos: {len(colores)}")
print(f"Sin fotos     : {len(sin_foto)}")
print(f"Cantidad > 1  : {len(multi)}")
