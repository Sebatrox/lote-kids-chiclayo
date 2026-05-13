import pandas as pd

df = pd.read_excel(r'c:\Users\Sebastian\Desktop\tienda-ropa\Inventario_Ropa_niños_COMPLETO.xlsx')
print("Nombres exactos (repr):")
for c in df.columns:
    print(f"  {repr(c)}")

# Encontrar la columna de liquidacion
liq_col = [c for c in df.columns if 'LIQUIDACI' in c.upper()]
print(f"\nColumna liquidacion encontrada: {repr(liq_col[0]) if liq_col else 'NO ENCONTRADA'}")
if liq_col:
    col = liq_col[0]
    validos = df[col].notna() & (df[col] != 0)
    print(f"Filas con valor: {validos.sum()} / {len(df)}")
    print(f"Primeros valores: {df[col].dropna().head(5).tolist()}")
