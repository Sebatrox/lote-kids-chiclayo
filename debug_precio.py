import pandas as pd

df = pd.read_excel(r'c:\Users\Sebastian\Desktop\tienda-ropa\Inventario_Ropa_niños_COMPLETO.xlsx')
df.columns = df.columns.str.strip()

# Solo filas con código en rango 1-221
df['Codigo'] = df['Codigo'].astype(str).str.strip().str.split('.').str[0]
mask = df['Codigo'].str.isdigit()
df = df[mask]
df = df[df['Codigo'].astype(int).between(1, 221)]

print(f"Total filas en rango 1-221: {len(df)}")

p_col = 'Precio_etiqueta_unidad'
print(f"\nValores en '{p_col}':")
print(f"  NaN: {df[p_col].isna().sum()}")
print(f"  == 0: {(df[p_col] == 0).sum()}")
print(f"  > 0:  {(df[p_col] > 0).sum()}")

print("\nFilas donde precio es NaN o 0:")
bad = df[df[p_col].isna() | (df[p_col] == 0)]
print(bad[['Codigo','Tipo','Talla', p_col, 'Precio costo']].to_string())
