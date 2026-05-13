import json

with open(r"c:\Users\Sebastian\Desktop\tienda-ropa\inventario.json", encoding="utf-8") as f:
    data = json.load(f)

con_fotos = [p for p in data if p["fotos"]]
sin_fotos = [p for p in data if not p["fotos"]]

print(f"Con al menos una foto: {len(con_fotos)}")
print(f"Sin fotos:             {len(sin_fotos)}")
print()
print("Codigos sin fotos:")
for p in sin_fotos:
    print(f"  {p['codigo']}  |  {p['tipo']}  |  {p['modelo']}")
