import json
from collections import Counter

with open(r'c:\Users\Sebastian\Desktop\tienda-ropa\inventario.json', encoding='utf-8') as f:
    inv = json.load(f)

conteo = Counter(p['tipo'] for p in inv)
print(f"{'TIPO':<30} {'N':>4}")
print("-" * 36)
for tipo, n in sorted(conteo.items()):
    print(f"{tipo:<30} {n:>4}")
print(f"\nTotal tipos únicos: {len(conteo)}")
