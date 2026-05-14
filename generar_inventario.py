import pandas as pd
import json
import os
from pathlib import Path

BASE = Path(r"c:\Users\Sebastian\Desktop\tienda-ropa")
FOTOS_DIR = BASE / "fotos"
EXCEL_PATH = BASE / "Inventario_Ropa_niños_Precio_Óptimo.xlsx"
OUTPUT_PATH = BASE / "inventario.json"

# Indexar fotos existentes por código
fotos_por_codigo: dict[str, list[str]] = {}
for fname in sorted(os.listdir(FOTOS_DIR)):
    if not fname.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        continue
    codigo = fname.split("_")[0]
    fotos_por_codigo.setdefault(codigo, []).append(fname)

df = pd.read_excel(EXCEL_PATH, dtype={"Codigo": str})
df.columns = df.columns.str.strip()  # elimina espacios al inicio/fin de cada nombre

genero_col = [c for c in df.columns if "nero" in c.lower()][0]

# Detecta la columna PRECIO ÓPTIMO por búsqueda parcial (evita problemas de codificación con tilde)
precio_liq_col = [c for c in df.columns if "PTIMO" in c.upper()][0]
print(f"Columna precio optimo: {repr(precio_liq_col)}")

productos = []
for _, row in df.iterrows():
    raw_codigo = str(row["Codigo"]).strip().split(".")[0]
    codigo = raw_codigo.zfill(4)

    try:
        num_codigo = int(codigo)
    except ValueError:
        continue
    if not (1 <= num_codigo <= 221):
        continue

    tipo  = str(row["Tipo"]).strip().lower()
    talla = str(row["Talla"]).strip().lower()

    v_liq = row[precio_liq_col]
    if pd.notna(v_liq) and float(v_liq) > 0:
        precio = float(v_liq)
    else:
        precio = 0.0

    if tipo in ("nan", "") or talla in ("nan", "") or precio == 0.0:
        continue

    cantidad = int(row["Cantidad"]) if pd.notna(row["Cantidad"]) else 1

    producto = {
        "codigo":   codigo,
        "genero":   str(row[genero_col]).strip().lower(),
        "tipo":     tipo,
        "modelo":   str(row["Modelo"]).strip().lower(),
        "talla":    talla,
        "color":    str(row["Color"]).strip().lower(),
        "cantidad": cantidad,
        "precio":   precio,
        "estado":   "disponible",
        "fotos":    fotos_por_codigo.get(codigo, []),
    }
    productos.append(producto)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(productos, f, ensure_ascii=False, indent=2)

print(f"Productos generados: {len(productos)}")
print(f"Con cantidad > 1:    {sum(1 for p in productos if p['cantidad'] > 1)}")
print(f"Sin fotos:           {sum(1 for p in productos if not p['fotos'])}")
print(f"Ejemplo 0001:        S/{productos[0]['precio']}")
print(f"Ejemplo 0009:        S/{next(p['precio'] for p in productos if p['codigo']=='0009')}")
