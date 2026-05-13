import json

with open(r'c:\Users\Sebastian\Desktop\tienda-ropa\inventario.json', encoding='utf-8') as f:
    inv = json.load(f)

data_js = json.dumps(inv, ensure_ascii=False)

def talla_key(t):
    if 'meses' in t.lower():
        nums = [int(x) for x in t.replace('-',' ').split() if x.isdigit()]
        return (0, nums[0] if nums else 0)
    if t.isdigit():
        return (1, int(t))
    order = {'xs':0,'s':1,'m':2,'l':3,'xl':4,'xxl':5}
    return (2, order.get(t.lower().strip(), 99))

tipos  = sorted(set(p['tipo']  for p in inv))
tallas = sorted(set(p['talla'] for p in inv), key=talla_key)

tipo_opts  = ''.join(f'<option value="{t}">{t.title()}</option>' for t in tipos)
talla_opts = ''.join(f'<option value="{t}">{t}</option>'         for t in tallas)

CSS = """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#f5f5f5;color:#222}
img{max-width:100%;display:block}
button{cursor:pointer;border:none;outline:none;background:none}
select,input{outline:none;border:none;font-family:inherit}
:root{--or:#FF6B35;--ord:#e55a27;--gr:#f0f0f0;--sh:0 2px 12px rgba(0,0,0,.10);--rad:12px}

/* HEADER */
.hdr-top{background:var(--or);padding:12px 16px;display:flex;align-items:center;gap:12px;position:sticky;top:0;z-index:50}
.logo{width:42px;height:42px;border-radius:50%;object-fit:cover;border:2px solid rgba(255,255,255,.4);flex-shrink:0}
.hdr-title{color:#fff;font-size:18px;font-weight:800;flex:1}
.banner{position:relative;overflow:hidden;height:200px}
.banner img{width:100%;height:200px;object-fit:cover}
.banner-ov{position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,.45) 0%,transparent 55%);
  display:flex;flex-direction:column;align-items:center;justify-content:flex-end;padding:16px;gap:10px}
.tagline{color:#fff;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.5px;text-align:center}
.btn-wa{background:#25D366;color:#fff;padding:9px 18px;border-radius:50px;font-weight:700;font-size:13px;
  text-decoration:none;display:inline-flex;align-items:center;gap:6px;transition:transform .15s}
.btn-wa:active{transform:scale(.97)}

/* FILTERS */
.filters{background:#fff;padding:10px 14px;position:sticky;top:66px;z-index:40;box-shadow:0 2px 8px rgba(0,0,0,.07)}
.f-gender{display:flex;gap:7px;margin-bottom:9px}
.btn-g{flex:1;padding:7px 4px;border-radius:50px;background:var(--gr);color:#888;font-size:13px;font-weight:700;transition:background .2s,color .2s}
.btn-g.active{background:var(--or);color:#fff}
.f-row{display:flex;gap:7px;margin-bottom:7px}
.fsel{flex:1;padding:8px 10px;border-radius:8px;background:var(--gr);font-size:12px;color:#333;-webkit-appearance:none;appearance:none}
.srch{position:relative}
.srch input{width:100%;padding:8px 34px 8px 12px;border-radius:8px;background:var(--gr);font-size:13px;color:#333}
.srch input::placeholder{color:#aaa}
.srch-ic{position:absolute;right:10px;top:50%;transform:translateY(-50%);color:#aaa;pointer-events:none;font-size:14px}

/* INFO */
.res-info{padding:8px 14px;font-size:12px;color:#999}

/* GRID */
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;padding:0 10px 130px}
@media(min-width:480px){.grid{grid-template-columns:repeat(3,1fr)}}
@media(min-width:720px){.grid{grid-template-columns:repeat(4,1fr);gap:14px;padding:0 16px 130px}}
@media(min-width:1024px){.grid{grid-template-columns:repeat(5,1fr)}}

/* CARD */
.card{background:#fff;border-radius:var(--rad);box-shadow:var(--sh);overflow:hidden;display:flex;flex-direction:column;transition:transform .2s}
.card.vendido{opacity:.5}
.photo-wrap{position:relative;cursor:pointer;overflow:hidden;background:#f5f5f5}
.photo-wrap img{width:100%;aspect-ratio:1/1;object-fit:cover;transition:opacity .2s}
.badge-ago{position:absolute;top:6px;left:6px;background:#e53935;color:#fff;font-size:9px;font-weight:900;padding:3px 7px;border-radius:4px;letter-spacing:.5px}
.badge-cod{position:absolute;bottom:5px;right:6px;background:rgba(0,0,0,.45);color:#fff;font-size:9px;padding:2px 5px;border-radius:3px}
.dots{position:absolute;bottom:6px;left:50%;transform:translateX(-50%);display:flex;gap:4px}
.dot{width:5px;height:5px;border-radius:50%;background:rgba(255,255,255,.5)}
.dot.on{background:#fff}
.cbody{padding:8px 9px 10px;display:flex;flex-direction:column;flex:1;gap:2px}
.c-tipo{font-size:12px;font-weight:800;color:#222;text-transform:capitalize}
.c-mod{font-size:11px;color:#999;text-transform:capitalize;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.c-meta{font-size:11px;color:#aaa;text-transform:capitalize}
.c-price{font-size:15px;font-weight:900;color:var(--or);margin-top:3px}
.stock-badge{display:inline-block;font-size:10px;font-weight:800;padding:2px 7px;border-radius:4px;margin-top:3px;letter-spacing:.3px}
.stock-1{background:#ffeaea;color:#e53935}
.stock-2{background:#fff3e0;color:var(--or)}
.btn-add{margin-top:6px;width:100%;padding:7px;border-radius:8px;background:var(--or);color:#fff;font-size:12px;font-weight:700;transition:background .2s}
.btn-add:disabled{background:#ccc;color:#999;cursor:not-allowed}
.card-qty{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:4px;margin-top:6px}
.cq-btn{height:30px;border-radius:8px;background:var(--gr);color:#333;font-size:17px;font-weight:800;line-height:1;width:100%}
.cq-btn:disabled{opacity:.3;cursor:not-allowed}
.cq-n{text-align:center;font-size:15px;font-weight:900;color:var(--or)}

/* CART BAR */
.cart-bar{position:fixed;bottom:0;left:0;right:0;background:var(--or);color:#fff;padding:10px 14px 16px;
  display:none;flex-direction:column;gap:7px;z-index:90;box-shadow:0 -4px 16px rgba(0,0,0,.2)}
.cart-bar.on{display:flex}
.cart-sum{display:flex;justify-content:space-between;align-items:center}
.cart-cnt{font-size:14px;font-weight:600}
.cart-tot{font-size:19px;font-weight:900}
.cart-warn{font-size:12px;background:rgba(0,0,0,.22);padding:4px 10px;border-radius:6px;text-align:center}
.btn-order{width:100%;padding:12px;border-radius:10px;background:#25D366;color:#fff;font-size:15px;font-weight:800}
.btn-order:disabled{background:rgba(255,255,255,.3);color:rgba(255,255,255,.5);cursor:not-allowed}

/* CART REVIEW PANEL */
.cart-panel-ov{position:fixed;inset:0;background:rgba(0,0,0,.5);display:none;z-index:150;align-items:flex-end;justify-content:center}
.cart-panel-ov.open{display:flex}
@media(min-width:520px){.cart-panel-ov{align-items:center}}
.cart-panel{background:#fff;border-radius:20px 20px 0 0;width:100%;max-width:460px;max-height:80vh;
  display:flex;flex-direction:column;animation:up .25s ease}
@media(min-width:520px){.cart-panel{border-radius:20px}}
.cp-hdr{padding:16px 16px 12px;display:flex;justify-content:space-between;align-items:center;
  border-bottom:1px solid var(--gr)}
.cp-hdr h3{font-size:16px;font-weight:800}
.cp-close{background:var(--gr);border-radius:50%;width:28px;height:28px;font-size:15px;
  display:flex;align-items:center;justify-content:center;color:#555}
.cp-list{overflow-y:auto;flex:1;padding:10px 14px}
.cp-item{display:flex;align-items:center;gap:10px;padding:9px 0;border-bottom:1px solid var(--gr)}
.cp-item:last-child{border-bottom:none}
.cp-img{width:44px;height:44px;border-radius:8px;object-fit:cover;flex-shrink:0;background:var(--gr)}
.cp-info{flex:1;min-width:0}
.cp-name{font-size:13px;font-weight:700;text-transform:capitalize;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.cp-sub{font-size:11px;color:#999;text-transform:capitalize}
.cp-price{font-size:14px;font-weight:800;color:var(--or);white-space:nowrap}
.cp-qty{display:flex;align-items:center;gap:5px;flex-shrink:0}
.cp-qty-btn{width:26px;height:26px;border-radius:50%;background:var(--gr);color:#333;font-size:16px;font-weight:700;
  display:flex;align-items:center;justify-content:center;line-height:1}
.cp-qty-btn:disabled{opacity:.3;cursor:not-allowed}
.cp-qty-n{font-size:15px;font-weight:800;min-width:18px;text-align:center;color:#222}
.cp-foot{padding:12px 14px 20px;border-top:1px solid var(--gr)}
.cp-total{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px}
.cp-total span:first-child{font-size:14px;font-weight:600}
.cp-total span:last-child{font-size:20px;font-weight:900;color:var(--or)}

/* MODAL OVERLAY */
.ov{position:fixed;inset:0;background:rgba(0,0,0,.6);display:none;align-items:flex-end;justify-content:center;z-index:200}
.ov.open{display:flex}
@media(min-width:520px){.ov{align-items:center}}
.sheet{background:#fff;border-radius:20px 20px 0 0;padding:24px 20px 32px;width:100%;max-width:460px;
  max-height:90vh;overflow-y:auto;position:relative;animation:up .3s ease}
@media(min-width:520px){.sheet{border-radius:20px}}
@keyframes up{from{transform:translateY(100%)}to{transform:translateY(0)}}
.sh-close{position:absolute;top:12px;right:12px;background:var(--gr);border-radius:50%;width:30px;height:30px;
  font-size:16px;display:flex;align-items:center;justify-content:center;color:#555}
.sh-title{font-size:18px;font-weight:900;text-align:center;margin-bottom:16px}
/* PASSWORD MODAL */
.pwd-box{background:#fff;border-radius:20px;padding:28px 24px;width:calc(100% - 48px);max-width:320px;text-align:center}
.pwd-title{font-size:18px;font-weight:800;margin-bottom:16px}
.pwd-in{width:100%;padding:12px;border-radius:10px;background:var(--gr);font-size:15px;margin-bottom:10px;text-align:center}
.btn-pwd{width:100%;padding:12px;border-radius:10px;background:var(--or);color:#fff;font-size:15px;font-weight:800}
.pwd-err{color:#e53935;font-size:13px;margin-top:8px;display:none}

/* ADMIN PANEL */
.adm{display:none;position:fixed;inset:0;background:#fff;z-index:300;overflow-y:auto}
.adm.open{display:block}
.adm-hdr{background:var(--or);color:#fff;padding:14px 16px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;z-index:10}
.adm-hdr h2{font-size:17px;font-weight:800}
.btn-adm-cls{background:rgba(255,255,255,.3);color:#fff;padding:6px 14px;border-radius:8px;font-weight:700;font-size:13px}
.adm-stats{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;padding:14px}
.stat{background:var(--gr);border-radius:12px;padding:14px;text-align:center}
.stat-n{font-size:26px;font-weight:900;color:var(--or)}
.stat-l{font-size:12px;color:#999;margin-top:2px}
.adm-wrap{padding:0 14px 40px;overflow-x:auto}
table{width:100%;border-collapse:collapse;font-size:13px}
th{background:var(--gr);padding:9px 7px;text-align:left;font-weight:700;color:#888;white-space:nowrap}
td{padding:8px 7px;border-bottom:1px solid var(--gr);vertical-align:middle}
tr.sold td{color:#bbb}
.tog{position:relative;display:inline-block;width:42px;height:23px}
.tog input{display:none}
.tog-sl{position:absolute;inset:0;background:#ccc;border-radius:50px;cursor:pointer;transition:background .25s}
.tog-sl::before{content:'';position:absolute;width:17px;height:17px;left:3px;top:3px;background:#fff;border-radius:50%;transition:transform .25s}
.tog input:checked + .tog-sl{background:var(--or)}
.tog input:checked + .tog-sl::before{transform:translateX(19px)}

/* FOOTER */
footer{background:#222;color:#777;text-align:center;padding:20px 16px 30px;font-size:12px}
.adm-trig{display:none}

/* EMPTY */
.empty{grid-column:1/-1;text-align:center;padding:60px 20px;color:#bbb;font-size:15px}
"""

JS = r"""
const INV_BASE = %%DATA%%;
let inv = [], cart = new Map(); // codigo -> cantidad pedida
let F = {g:'todos', tipo:'', talla:'', q:''};
const WA = '51976235299';
const PWD_HASH = 'eb09a17085982cf7a7b1c8c26538de53067a208eb311309a1797e14b8787113a';
const KW_HASH  = 'b8b8eb83374c0bf3b1c3224159f6119dbfff1b7ed6dfecdd80d4e8a895790a34';
const LSK = 'lk_v2';
const PH  = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Crect fill='%23f0f0f0' width='200' height='200'/%3E%3Ctext fill='%23ccc' x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-size='48'%3E%3F%3C/text%3E%3C/svg%3E";

async function sha256(str){
  const buf=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(str));
  return Array.from(new Uint8Array(buf)).map(b=>b.toString(16).padStart(2,'0')).join('');
}

function init(){
  const saved = JSON.parse(localStorage.getItem(LSK)||'{}');
  inv = INV_BASE.map(p=>({...p, estado: saved[p.codigo]??p.estado}));
  renderGrid();
}

function saveState(cod,est){
  const s=JSON.parse(localStorage.getItem(LSK)||'{}');
  s[cod]=est; localStorage.setItem(LSK,JSON.stringify(s));
  const p=inv.find(x=>x.codigo===cod); if(p) p.estado=est;
}

/* FILTERS */
function setG(g,btn){
  F.g=g;
  document.querySelectorAll('.btn-g').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  renderGrid();
}
async function applyF(){
  const raw = document.getElementById('srch').value;
  const trimmed = raw.trim();
  if(trimmed.length === 9){
    const h = await sha256(trimmed);
    if(h === KW_HASH){
      document.getElementById('srch').value = '';
      openLogin();
      return;
    }
  }
  F.tipo  = document.getElementById('sel-t').value;
  F.talla = document.getElementById('sel-ta').value;
  F.q     = trimmed.toLowerCase();
  renderGrid();
}
function match(p){
  if(F.g!=='todos' && p.genero!==F.g) return false;
  if(F.tipo  && p.tipo!==F.tipo)   return false;
  if(F.talla && p.talla!==F.talla) return false;
  if(F.q){
    const h=(p.tipo+' '+p.modelo+' '+p.color+' '+p.codigo).toLowerCase();
    if(!h.includes(F.q)) return false;
  }
  return true;
}

/* RENDER */
function renderGrid(){
  const g=document.getElementById('g');
  const filtered=inv.filter(match);
  document.getElementById('ri').textContent=
    filtered.length===inv.length ? inv.length+' productos'
    : filtered.length+' de '+inv.length+' productos';
  if(!filtered.length){
    g.innerHTML='<div class="empty">Sin resultados — prueba otros filtros</div>';return;
  }
  g.innerHTML=filtered.map(card).join('');
}

function cap(s){return s?s.charAt(0).toUpperCase()+s.slice(1):'';}

function card(p){
  const vnd=p.estado==='vendido';
  const f1=p.fotos[0]?'fotos/'+p.fotos[0]:'';
  const f2=p.fotos[1]?'fotos/'+p.fotos[1]:'';
  const src=f1||PH;
  const dots=f2?`<div class="dots"><div class="dot on" id="d0-${p.codigo}"></div><div class="dot" id="d1-${p.codigo}"></div></div>`:'';
  const ago=vnd?'<span class="badge-ago">AGOTADO</span>':'';
  return `
<div class="card${vnd?' vendido':''}" id="c-${p.codigo}">
  <div class="photo-wrap" data-i="0" onclick="flip('${p.codigo}','${f1}','${f2}')">
    <img id="im-${p.codigo}" src="${src}" alt="${p.tipo}" loading="lazy"
         onerror="this.src='${PH}'">
    ${ago}<span class="badge-cod">${p.codigo}</span>${dots}
  </div>
  <div class="cbody">
    <div class="c-tipo">${cap(p.tipo)}</div>
    <div class="c-mod">${cap(p.modelo)}</div>
    <div class="c-meta">Talla ${p.talla} &middot; ${cap(p.color)}</div>
    <div class="c-price">S/ ${Math.round(p.precio)}</div>
    ${!vnd&&p.cantidad===1?'<span class="stock-badge stock-1">Ultima unidad</span>':!vnd&&p.cantidad===2?'<span class="stock-badge stock-2">Quedan 2</span>':''}
    <div id="bwrap-${p.codigo}">${cardBtnHTML(p,vnd)}</div>
  </div>
</div>`;
}
function cardBtnHTML(p,vnd){
  if(vnd) return '<button class="btn-add" disabled>Agotado</button>';
  const qty=cart.get(p.codigo)||0;
  if(qty===0) return `<button class="btn-add" onclick="cardAdd('${p.codigo}')">Agregar</button>`;
  return `<div class="card-qty">
    <button class="cq-btn" onclick="cardAdj('${p.codigo}',-1)">-</button>
    <span class="cq-n">${qty}</span>
    <button class="cq-btn" onclick="cardAdj('${p.codigo}',1)" ${qty>=p.cantidad?'disabled':''}>+</button>
  </div>`;
}
function renderCardBtn(cod){
  const p=inv.find(x=>x.codigo===cod); if(!p) return;
  const w=document.getElementById('bwrap-'+cod); if(!w) return;
  w.innerHTML=cardBtnHTML(p,p.estado==='vendido');
}

/* PHOTO FLIP */
function flip(cod,f1,f2){
  if(!f2) return;
  const w=document.querySelector(`#c-${cod} .photo-wrap`);
  const im=document.getElementById('im-'+cod);
  let i=parseInt(w.dataset.i||'0'); i=i?0:1;
  w.dataset.i=i; im.style.opacity='.4';
  im.src=i?f2:f1; im.onload=()=>im.style.opacity='1';
  const d0=document.getElementById('d0-'+cod), d1=document.getElementById('d1-'+cod);
  if(d0){d0.className='dot'+(i===0?' on':''); d1.className='dot'+(i===1?' on':'');}
}

/* CART */
// ── Fuente de verdad única ────────────────────────────
function setQty(cod, qty){
  const p=inv.find(x=>x.codigo===cod); if(!p) return;
  const clamped=Math.max(0,Math.min(qty,p.cantidad));
  if(clamped===0){cart.delete(cod);}else{cart.set(cod,clamped);}
  renderCardBtn(cod);                          // actualiza tarjeta
  syncPanelRow(cod);                           // actualiza fila del panel
  updCart();
  if(cart.size===0) closeCartPanel();
}
function cardAdd(cod){
  const p=inv.find(x=>x.codigo===cod); if(!p||p.estado==='vendido') return;
  setQty(cod,1);
}
function cardAdj(cod,delta){
  setQty(cod,(cart.get(cod)||0)+delta);
}
// ── Actualiza solo la fila del panel (sin redibujar toda la lista) ──
function syncPanelRow(cod){
  const row=document.getElementById('cpi-'+cod);
  if(!row) return;                             // panel cerrado o prenda no está
  const p=inv.find(x=>x.codigo===cod);
  const qty=cart.get(cod)||0;
  if(qty===0){ row.remove(); return; }
  const qEl=row.querySelector('.cp-qty-n');
  const pEl=document.getElementById('cpp-'+cod);
  if(qEl) qEl.textContent=qty;
  if(pEl) pEl.textContent='S/'+Math.round(p.precio*qty);
  const btns=row.querySelectorAll('.cp-qty-btn');
  if(btns[1]) btns[1].disabled=qty>=p.cantidad;
  // actualiza totales del panel
  let n=0,tot=0;
  for(const [c,q] of cart){const px=inv.find(x=>x.codigo===c);if(px){n+=q;tot+=px.precio*q;}}
  _cpTotals(n,tot);
}
function updCart(){
  const bar=document.getElementById('cb');
  let n=0, tot=0;
  for(const [c,qty] of cart){const p=inv.find(x=>x.codigo===c);if(p){n+=qty;tot+=p.precio*qty;}}
  if(!n){bar.classList.remove('on');return;}
  bar.classList.add('on');
  document.getElementById('cct').textContent=n===1?'1 prenda':n+' prendas';
  document.getElementById('ctt').textContent='S/ '+Math.round(tot);
  const w=document.getElementById('cw'), bo=document.getElementById('bord');
  if(n<3){w.style.display='block';w.textContent='Mínimo 3 prendas · faltan '+(3-n);bo.disabled=true;}
  else{w.style.display='none';bo.disabled=false;}
}

/* ENVIAR PEDIDO DIRECTO POR WHATSAPP */
function openPay(){
  const lines=[]; let tot=0;
  for(const [c,qty] of cart){
    const p=inv.find(x=>x.codigo===c); if(!p) continue;
    const sub=Math.round(p.precio*qty); tot+=sub;
    const qStr=qty>1?` · x${qty}`:'';
    lines.push(`- [${p.codigo}] ${cap(p.tipo)} · Talla ${p.talla} · ${cap(p.color)}${qStr} · S/${sub}`);
  }
  const msg=
    `Hola! Quiero hacer un pedido en Lote Kids Chiclayo\n\n`+
    `${lines.join('\n')}\n\n`+
    `Total: S/${Math.round(tot)}\n\n`+
    `Mi nombre es: \n`+
    `Mi distrito/ciudad es:`;
  window.open('https://wa.me/'+WA+'?text='+encodeURIComponent(msg),'_blank');
}

/* CART REVIEW PANEL */
function openCartPanel(){
  renderCartPanel();
  document.getElementById('cp-ov').classList.add('open');
}
function closeCartPanel(){
  document.getElementById('cp-ov').classList.remove('open');
}
function renderCartPanel(){
  const rows=[]; let n=0, tot=0;
  for(const [c,qty] of cart){const p=inv.find(x=>x.codigo===c);if(p){rows.push({p,qty});n+=qty;tot+=p.precio*qty;}}
  _cpTotals(n,tot);
  document.getElementById('cp-list').innerHTML=rows.length?rows.map(({p,qty})=>{
    const foto=p.fotos[0]?'fotos/'+p.fotos[0]:PH;
    const badge=p.cantidad===1?'<span class="stock-badge stock-1">Ultima unidad</span>':p.cantidad===2?'<span class="stock-badge stock-2">Quedan 2</span>':'';
    return `<div class="cp-item" id="cpi-${p.codigo}">
      <img class="cp-img" src="${foto}" onerror="this.src='${PH}'">
      <div class="cp-info">
        <div class="cp-name">${cap(p.tipo)} &middot; ${p.talla}</div>
        <div class="cp-sub">${cap(p.color)} &middot; cod. ${p.codigo}</div>
        ${badge}
      </div>
      <div class="cp-qty">
        <button class="cp-qty-btn" onclick="adjustQty('${p.codigo}',-1)">-</button>
        <span class="cp-qty-n" id="cpq-${p.codigo}">${qty}</span>
        <button class="cp-qty-btn" onclick="adjustQty('${p.codigo}',1)" ${qty>=p.cantidad?'disabled':''}>+</button>
      </div>
      <span class="cp-price" id="cpp-${p.codigo}">S/${Math.round(p.precio*qty)}</span>
    </div>`;
  }).join(''):'<p style="text-align:center;color:#aaa;padding:30px 0">No hay prendas seleccionadas</p>';
}
function adjustQty(cod,delta){
  setQty(cod,(cart.get(cod)||0)+delta);
}
function _cpTotals(n,tot){
  document.getElementById('cp-count').textContent=n===1?'1 prenda':n+' prendas';
  document.getElementById('cp-tot').textContent='S/ '+Math.round(tot);
}

/* ADMIN AUTH */
function openLogin(){
  document.getElementById('pwd-in').value='';
  document.getElementById('pwd-err').style.display='none';
  document.getElementById('ov-pwd').classList.add('open');
  setTimeout(()=>document.getElementById('pwd-in').focus(),100);
}
function closePwd(e){if(e.target===e.currentTarget)document.getElementById('ov-pwd').classList.remove('open');}
async function checkPwd(){
  const hash = await sha256(document.getElementById('pwd-in').value);
  if(hash === PWD_HASH){
    document.getElementById('ov-pwd').classList.remove('open');
    openAdm();
  } else {
    document.getElementById('pwd-err').style.display='block';
    document.getElementById('pwd-in').value='';
    document.getElementById('pwd-in').focus();
  }
}

/* ADMIN PANEL */
function openAdm(){
  document.getElementById('adm').classList.add('open');
  renderStats(); renderTable();
}
function closeAdm(){
  document.getElementById('adm').classList.remove('open');
  for(const [c] of [...cart]){const p=inv.find(x=>x.codigo===c);if(p&&p.estado==='vendido')cart.delete(c);}
  renderGrid(); updCart();
}
function renderStats(){
  const tot=inv.length;
  const vnd=inv.filter(p=>p.estado==='vendido').length;
  const dis=tot-vnd;
  const rec=inv.filter(p=>p.estado==='vendido').reduce((s,p)=>s+p.precio,0);
  document.getElementById('as').innerHTML=`
    <div class="stat"><div class="stat-n">${tot}</div><div class="stat-l">Total prendas</div></div>
    <div class="stat"><div class="stat-n" style="color:#4CAF50">${dis}</div><div class="stat-l">Disponibles</div></div>
    <div class="stat"><div class="stat-n" style="color:#e53935">${vnd}</div><div class="stat-l">Vendidas</div></div>
    <div class="stat"><div class="stat-n">S/${rec.toFixed(0)}</div><div class="stat-l">Recaudado</div></div>`;
}
function renderTable(){
  document.getElementById('atb').innerHTML=inv.map(p=>{
    const v=p.estado==='vendido';
    return `<tr id="ar-${p.codigo}" class="${v?'sold':''}">
      <td>${p.codigo}</td>
      <td style="text-transform:capitalize">${p.tipo}</td>
      <td>${p.talla}</td>
      <td style="text-transform:capitalize">${p.color}</td>
      <td style="text-align:center;font-weight:${p.cantidad>1?'700':'400'};color:${p.cantidad>1?'var(--or)':'inherit'}">${p.cantidad}</td>
      <td>${p.precio.toFixed(2)}</td>
      <td>
        <label class="tog">
          <input type="checkbox" ${v?'':'checked'} onchange="togState('${p.codigo}',this.checked)">
          <span class="tog-sl"></span>
        </label>
        <span id="al-${p.codigo}" style="font-size:11px;margin-left:4px;color:${v?'#e53935':'#4CAF50'}">${v?'Vendido':'Disp.'}</span>
      </td></tr>`;
  }).join('');
}
function togState(cod,avail){
  const est=avail?'disponible':'vendido';
  saveState(cod,est);
  const r=document.getElementById('ar-'+cod); if(r) r.className=est==='vendido'?'sold':'';
  const l=document.getElementById('al-'+cod);
  if(l){l.textContent=est==='vendido'?'Vendido':'Disp.';l.style.color=est==='vendido'?'#e53935':'#4CAF50';}
  renderStats();
}

init();
"""

HTML = (
"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=5.0">
<meta name="theme-color" content="#FF6B35">
<link rel="icon" href="logo.png">
<title>Lote Kids Chiclayo — Liquidación</title>
<style>""" + CSS + """</style>
</head>
<body>

<div class="hdr-top">
  <img src="logo.png" alt="" class="logo" onerror="this.style.display='none'">
  <span class="hdr-title">Lote Kids Chiclayo</span>
</div>
<div class="banner">
  <img src="portada.png" alt="Portada" onerror="this.style.display='none'">
  <div class="banner-ov">
    <p class="tagline">Liquidación total &nbsp;·&nbsp; precio de costo &nbsp;·&nbsp; stock limitado</p>
    <a href="https://wa.me/51976235299" target="_blank" class="btn-wa">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>
      Comprar por WhatsApp
    </a>
  </div>
</div>

<section class="filters">
  <div class="f-gender">
    <button class="btn-g active" onclick="setG('todos',this)">Todos</button>
    <button class="btn-g"        onclick="setG('niño',this)">Niño</button>
    <button class="btn-g"        onclick="setG('niña',this)">Niña</button>
  </div>
  <div class="f-row">
    <select class="fsel" id="sel-t"  onchange="applyF()">
      <option value="">Todos los tipos</option>""" + tipo_opts + """
    </select>
    <select class="fsel" id="sel-ta" onchange="applyF()">
      <option value="">Todas las tallas</option>""" + talla_opts + """
    </select>
  </div>
  <div class="srch">
    <input type="text" id="srch" placeholder="Buscar modelo, color, código..." oninput="applyF()">
    <span class="srch-ic">🔍</span>
  </div>
</section>

<div class="res-info" id="ri"></div>
<main class="grid" id="g"></main>

<!-- CART BAR -->
<div class="cart-bar" id="cb">
  <div class="cart-sum">
    <span class="cart-cnt" id="cct">0 prendas</span>
    <div style="display:flex;align-items:center;gap:8px">
      <span class="cart-tot" id="ctt">S/ 0.00</span>
      <button style="background:rgba(255,255,255,.25);color:#fff;padding:5px 11px;border-radius:20px;font-size:12px;font-weight:700" onclick="openCartPanel()">Ver pedido</button>
    </div>
  </div>
  <div class="cart-warn" id="cw" style="display:none"></div>
  <button class="btn-order" id="bord" onclick="openPay()" disabled>Enviar pedido por WhatsApp</button>
</div>

<!-- CART REVIEW PANEL -->
<div class="cart-panel-ov" id="cp-ov" onclick="if(event.target===this)closeCartPanel()">
  <div class="cart-panel">
    <div class="cp-hdr">
      <h3>Mi pedido</h3>
      <button class="cp-close" onclick="closeCartPanel()">x</button>
    </div>
    <div class="cp-list" id="cp-list"></div>
    <div class="cp-foot">
      <div class="cp-total">
        <span id="cp-count">0 prendas</span>
        <span id="cp-tot">S/ 0</span>
      </div>
      <button class="btn-order" style="width:100%;padding:12px;border-radius:10px;background:#25D366;color:#fff;font-size:15px;font-weight:800" onclick="closeCartPanel();openPay()">Enviar pedido por WhatsApp</button>
    </div>
  </div>
</div>

<!-- PASSWORD MODAL -->
<div class="ov" id="ov-pwd" onclick="closePwd(event)">
  <div class="pwd-box">
    <p class="pwd-title">🔒 Acceso Admin</p>
    <input class="pwd-in" type="password" id="pwd-in" placeholder="Contraseña"
           onkeydown="if(event.key==='Enter')checkPwd()">
    <button class="btn-pwd" onclick="checkPwd()">Ingresar</button>
    <p class="pwd-err" id="pwd-err">Contraseña incorrecta</p>
  </div>
</div>

<!-- ADMIN PANEL -->
<div class="adm" id="adm">
  <div class="adm-hdr">
    <h2>⚙ Panel Admin</h2>
    <button class="btn-adm-cls" onclick="closeAdm()">✕ Cerrar</button>
  </div>
  <div class="adm-stats" id="as"></div>
  <div class="adm-wrap">
    <table>
      <thead><tr><th>Cód.</th><th>Tipo</th><th>Talla</th><th>Color</th><th>Cant.</th><th>S/</th><th>Estado</th></tr></thead>
      <tbody id="atb"></tbody>
    </table>
  </div>
</div>

<footer>
  <p>© 2025 Lote Kids Chiclayo</p>
  <span class="adm-trig"></span>
</footer>

<script>
""" + JS.replace('%%DATA%%', data_js) + """
</script>
</body>
</html>"""
)

out = r'c:\Users\Sebastian\Desktop\tienda-ropa\catalogo.html'
with open(out, 'w', encoding='utf-8') as f:
    f.write(HTML)

print(f'catalogo.html generado  ({len(HTML):,} caracteres)')
