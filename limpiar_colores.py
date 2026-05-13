import json
from collections import Counter

RUTA = r'c:\Users\Sebastian\Desktop\tienda-ropa\inventario.json'

with open(RUTA, encoding='utf-8') as f:
    inv = json.load(f)

NORMALIZACION = {
    "blanc0":                    "blanco",
    "blanca":                    "blanco",
    "girs":                      "gris",
    "azul  noche":               "azul noche",
    "azul /blanco":              "azul/blanco",
    "celeste /blanco":           "celeste/blanco",
    "azulino / azul marino":     "azulino/azul marino",
    "azulino verde":             "azulino/verde",
    "rosa bb":                   "rosado",
    "rosa bebe":                 "rosado",
    "blanco california life":    "blanco",
    "blanco stand out":          "blanco",
    "celeste stand out":         "celeste",
}

sin_mapeo = []
for p in inv:
    nuevo = NORMALIZACION.get(p['color'])
    if nuevo:
        sin_mapeo.append(f"  [{p['codigo']}] '{p['color']}' -> '{nuevo}'")
        p['color'] = nuevo

for linea in sin_mapeo:
    print(linea)

with open(RUTA, 'w', encoding='utf-8') as f:
    json.dump(inv, f, ensure_ascii=False, indent=2)

print(f"\nProductos corregidos: {len(sin_mapeo)}")
print(f"\nColores unicos finales:")
conteo = Counter(p['color'] for p in inv)
for color, n in sorted(conteo.items()):
    print(f"  {color:<35} {n:>3}")
print(f"\nTotal colores: {len(conteo)}")
