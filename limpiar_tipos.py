import json
from collections import Counter

RUTA = r'c:\Users\Sebastian\Desktop\tienda-ropa\inventario.json'

with open(RUTA, encoding='utf-8') as f:
    inv = json.load(f)

NORMALIZACION = {
    "bermuda":       "Short",
    "bividi":        "Bividi",
    "buzo":          "Buzo",
    "cafarena":      "Cafarena",
    "camisa m/c":    "Camisa M/C",
    "camisa m/l":    "Camisa M/L",
    "chaqueta":      "Chaqueta",
    "cortaviento":   "Cortaviento",
    "leggins":       "Leggins",
    "pantalon":      "Pantalon",
    "polera":        "Polera",
    "polera + buzo": "Polera + Buzo",
    "polera m/l":    "Polera",
    "polo m/c":      "Polo M/C",
    "polo m/l":      "Polo M/L",
    "short":         "Short",
}

sin_mapeo = set()
for p in inv:
    tipo_nuevo = NORMALIZACION.get(p['tipo'])
    if tipo_nuevo:
        p['tipo'] = tipo_nuevo
    else:
        sin_mapeo.add(p['tipo'])

if sin_mapeo:
    print(f"ADVERTENCIA - tipos sin mapeo: {sin_mapeo}")

with open(RUTA, 'w', encoding='utf-8') as f:
    json.dump(inv, f, ensure_ascii=False, indent=2)

print("Tipos unicos finales:")
conteo = Counter(p['tipo'] for p in inv)
for tipo, n in sorted(conteo.items()):
    print(f"  {tipo:<22} {n:>3}")
print(f"\nTotal tipos: {len(conteo)}")
