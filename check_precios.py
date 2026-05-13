import json

with open(r'c:\Users\Sebastian\Desktop\tienda-ropa\inventario.json', encoding='utf-8') as f:
    inv = json.load(f)

codigos = ['0082','0017','0095','0166','0167','0171','0184','0185','0213']
print(f"{'COD':<6} {'TIPO':<18} {'TALLA':<10} {'P.UNIT':>8} {'x2':>8}")
print("-" * 56)
for cod in codigos:
    p = next((x for x in inv if x['codigo'] == cod), None)
    if p:
        print(f"{p['codigo']:<6} {p['tipo']:<18} {p['talla']:<10} {p['precio']:>8.0f} {p['precio']*2:>8.0f}")
    else:
        print(f"{cod}: NO ENCONTRADO")
