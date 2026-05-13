import json
from collections import Counter

with open(r'c:\Users\Sebastian\Desktop\tienda-ropa\inventario.json', encoding='utf-8') as f:
    inv = json.load(f)

conteo = Counter(p['color'] for p in inv)

print(f"{'COLOR':<35} {'N':>4}")
print("-" * 41)
for color, n in sorted(conteo.items()):
    print(f"{color:<35} {n:>4}")
print(f"\nTotal colores unicos: {len(conteo)}")
