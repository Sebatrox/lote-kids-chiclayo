html = open(r'c:\Users\Sebastian\Desktop\tienda-ropa\catalogo.html', encoding='utf-8').read()
checks = [
    ('cardAdd'       in html, 'cardAdd presente'),
    ('cardAdj'       in html, 'cardAdj presente'),
    ('cardBtnHTML'   in html, 'cardBtnHTML presente'),
    ('renderCardBtn' in html, 'renderCardBtn presente'),
    ('bwrap-'        in html, 'wrapper bwrap presente'),
    ('card-qty'      in html, 'CSS card-qty presente'),
    ('cq-btn'        in html, 'CSS cq-btn presente'),
    ('tog('      not in html, 'tog() eliminado'),
    ('btn-add.added' not in html, 'clase added eliminada'),
]
for ok, label in checks:
    print(('OK  ' if ok else 'FALLA'), label)
