html = open(r'c:\Users\Sebastian\Desktop\tienda-ropa\catalogo.html', encoding='utf-8').read()
checks = [
    ('new Map()'        in html, 'cart es Map'),
    ('cart.set('        in html, 'cart.set presente'),
    ('adjustQty'        in html, 'adjustQty presente'),
    ('cp-qty-btn'       in html, 'Botones +/- CSS'),
    ('cp-qty-n'         in html, 'Contador qty'),
    ('x${qty}'          in html, 'xN en mensaje WA'),
    ('Math.round(tot)'  in html, 'Total redondeado'),
    ('new Set()'    not in html, 'Sin Set residual'),
]
for ok, label in checks:
    print(('OK  ' if ok else 'FALLA'), label)
