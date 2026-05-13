import json
from collections import Counter

with open(r'c:\Users\Sebastian\Desktop\tienda-ropa\inventario.json', encoding='utf-8') as f:
    inv = json.load(f)

conteo = Counter(p['talla'] for p in inv)

def sort_key(t):
    t = t.lower().strip()
    if 'meses' in t:
        nums = [int(x) for x in t.replace('-', ' ').split() if x.isdigit()]
        return (0, nums[0] if nums else 0, t)
    if t.isdigit():
        return (1, int(t), t)
    order = {'xs': 0, 's': 1, 'm': 2, 'l': 3, 'xl': 4, 'xxl': 5}
    return (2, order.get(t, 99), t)

print(f"{'TALLA':<20} {'N':>4}")
print("-" * 26)
for talla, n in sorted(conteo.items(), key=lambda x: sort_key(x[0])):
    print(f"{talla:<20} {n:>4}")
print(f"\nTotal tallas unicas: {len(conteo)}")
