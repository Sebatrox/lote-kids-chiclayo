import hashlib, re, json

html = open(r'c:\Users\Sebastian\Desktop\tienda-ropa\catalogo.html', encoding='utf-8').read()

print("=" * 55)
print("AUDITORIA DE SEGURIDAD — catalogo.html")
print("=" * 55)

# 1. Contraseña en texto plano
pwd_match = re.search(r"const PWD\s*=\s*'(.*?)'", html)
if pwd_match:
    pwd = pwd_match.group(1)
    sha = hashlib.sha256(pwd.encode()).hexdigest()
    print(f"\n[CRITICO] Contraseña expuesta en fuente: '{pwd}'")
    print(f"          SHA-256: {sha}")
else:
    print("\n[OK] Contraseña no encontrada en texto plano")

# 2. Keyword admin en fuente
if 'admin2024' in html:
    print("\n[MEDIO]  Keyword 'admin2024' visible en codigo fuente")
else:
    print("\n[OK] Keyword de admin no encontrada en texto plano")

# 3. WhatsApp
wa_count = html.count('51976235299')
print(f"\n[INFO]   WhatsApp +51976235299 aparece {wa_count} veces (dato publico intencional)")

# 4. XSS — buscar si F.q se inserta en innerHTML
inner_blocks = re.findall(r'innerHTML\s*=\s*[^;]{0,300}', html)
xss_risk = any('F.q' in b or 'srch' in b or 'search' in b.lower() for b in inner_blocks)
print(f"\n[{'CRITICO' if xss_risk else 'OK'}]   XSS via buscador en innerHTML: {xss_risk}")

# 5. Datos en inventario.json
inv = json.load(open(r'c:\Users\Sebastian\Desktop\tienda-ropa\inventario.json', encoding='utf-8'))
campos = sorted(set(k for p in inv for k in p.keys()))
sensibles = [c for c in campos if any(x in c.lower() for x in ['email','phone','tel','rut','dni','pass','token','secret','address','direccion'])]
print(f"\n[OK]     Campos en inventario.json: {campos}")
print(f"         Campos sensibles detectados: {sensibles if sensibles else 'ninguno'}")

# 6. Datos personales adicionales
for dato in ['Sebastian Vigil', 'sebastian', 'vigil', 'vigilvargass']:
    if dato.lower() in html.lower():
        print(f"\n[INFO]   Dato personal encontrado: '{dato}' (revisar si es necesario)")

print("\n" + "=" * 55)
print("Resumen de riesgos a corregir:")
if pwd_match:
    print("  1. Reemplazar contraseña por hash SHA-256")
if 'admin2024' in html:
    print("  2. Keyword admin visible (mitigado por contrasena hasheada)")
print("=" * 55)
