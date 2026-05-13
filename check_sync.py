html = open(r'c:\Users\Sebastian\Desktop\tienda-ropa\catalogo.html', encoding='utf-8').read()
checks = [
    ('function setQty'   in html, 'setQty definida'),
    ('function syncPanelRow' in html, 'syncPanelRow definida'),
    # cardAdj y adjustQty ahora son wrappers de una línea sobre setQty
    ('function cardAdj'  in html, 'cardAdj presente'),
    ('function adjustQty' in html, 'adjustQty presente'),
    # ambas deben llamar a setQty, no tocar cart directamente
    (html.count('cart.set') == 1, 'cart.set solo en setQty (1 ocurrencia)'),
    (html.count('cart.delete') == 1, 'cart.delete solo en setQty (1 ocurrencia)'),
    ('renderCardBtn(cod)' in html, 'renderCardBtn llamado desde setQty'),
    ('syncPanelRow(cod)'  in html, 'syncPanelRow llamado desde setQty'),
]
for ok, label in checks:
    print(('OK  ' if ok else 'FALLA'), label)
