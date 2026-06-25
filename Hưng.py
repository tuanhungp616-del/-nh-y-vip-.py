# ==================================================
# 🚀 HUNG DEP TRAI - VIP SENSITIVITY 100 TRIỆU
# ✅ GỘP TOÀN BỘ VÀO 1 FILE DUY NHẤ: hung.py
# ✅ KHÔNG CẦN thư mục / file phụ trợ nào khác
# ==================================================
from flask import Flask, request, jsonify, session, redirect, render_template_string
import hashlib, sqlite3, os, time, random
from datetime import datetime, timedelta

# ---------------- CẤU HÌNH MÁY CHỦ ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH  = os.path.join(BASE_DIR, "database.db")
app = Flask(__name__)
app.secret_key = "HUNG_DEP_TRAI_100TRIEU_VIP_2026_FIXED"
app.config["JSON_AS_ASCII"] = False

# ---------------- GIAO DIỆN ĐƯỢC NHÚNG SẴN ----------------
INDEX_HTML = r'''<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>HƯNG ĐẸP TRAI - VIP SENS 100 TRIỆU</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;600;700&display=swap');
:root{--bg:#090a0f;--box:#12141d;--c1:#00f0ff;--c2:#ff0055;--tx:#e6e6e6}
*{box-sizing:border-box;margin:0;padding:0;font-family:'Rajdhani',sans-serif}
body{background:var(--bg);min-height:100vh;display:flex;justify-content:center;align-items:center;color:var(--tx)}
.box{width:92%;max-width:420px;background:#12141dd9;border:1px solid #00f0ff33;border-radius:14px;padding:28px 20px;box-shadow:0 0 30px #00f0ff22;backdrop-filter:blur(8px)}
h1{color:var(--c1);text-align:center;text-transform:uppercase;letter-spacing:2px;text-shadow:0 0 10px #00f0ff88}
.ver{color:var(--c2);text-align:center;font-weight:600;margin-bottom:18px}
input,select{width:100%;padding:12px;margin:8px 0;background:#0008;border:1px solid #2a2a3a;border-radius:8px;color:#fff;outline:none;font-size:15px}
input:focus,select:focus{border-color:var(--c1);box-shadow:0 0 8px #00f0ff55}
button{width:100%;padding:13px;margin-top:8px;background:linear-gradient(90deg,#00f0ff,#00a8ff);color:#000;border:none;border-radius:8px;font-weight:700;letter-spacing:1px;cursor:pointer;text-transform:uppercase}
button:hover{box-shadow:0 0 18px #00f0ffaa}
.btn-red{background:transparent;color:var(--c2);border:1px solid var(--c2);margin-top:14px}
.info{border:1px dashed var(--c1);padding:10px;border-radius:8px;margin:10px 0;font-size:14px;background:#00f0ff08}
.info b{color:var(--c1)}
.res{margin-top:14px;display:none}
.gr{background:#0006;border:1px solid #222;border-radius:8px;padding:10px;margin:8px 0}
.gr h4{color:#888;font-size:12px;border-bottom:1px solid #2a2a3a;padding-bottom:4px;margin-bottom:6px;text-transform:uppercase}
.r{display:flex;justify-content:space-between;padding:3px 0}
.r .v{color:var(--c1);font-weight:700}
.r .d{color:var(--c2);font-weight:700}
.load{display:none;text-align:center;color:var(--c1);padding:10px;animation:blink 1s infinite}
@keyframes blink{50%{opacity:.4}}
#main,#adminBtn{display:none}
</style></head><body>
<div class="box" id="login">
    <h1>HƯNG ĐẸP TRAI</h1>
    <div class="ver">⚡ VIP SENSITIVITY v3.0 · 100 TRIỆU</div>
    <input id="key" placeholder="🔑 Nhập LICENSE KEY">
    <button onclick="login()">KÍCH HOẠT VIP</button>
    <div class="load" id="l1">Đang kết nối server...</div>
</div>
<div class="box" id="main">
    <h1>PANEL VIP</h1>
    <div class="info">User: <b id="u"></b><br>HSD: <b id="e"></b><br>Trạng thái: <b style="color:#0f0">Hoạt động · Bypass tự động</b></div>
    <button id="adminBtn" onclick="location.href='/admin'">⚙️ VÀO TRANG QUẢN LÝ ADMIN</button>
    <input id="dev" placeholder="📱 Tên máy: VD iPhone 16 Pro / Samsung S24">
    <select id="wp">
        <option value="ALL">🎯 TỔNG HỢP - PHUN CẢ BĂNG</option>
        <option value="ONETAP">💥 ONETAP - M1887 / DEAGLE</option>
        <option value="SMG">🔥 SẤY ĐẦU - MP40 / UMP / MAC10</option>
        <option value="AR">🎯 BẮN XA - SCAR / GROZA / AK</option>
    </select>
    <button onclick="calc()">⚡ TÍNH ĐỘ NHẠY VIP</button>
    <div class="load" id="l2">Đang chạy thuật toán 100 triệu tổ hợp...</div>
    <div class="res" id="res">
        <div class="gr"><h4>Độ nhạy trong game (0‑200)</h4>
            <div class="r"><span>Nhìn xung quanh</span><span class="v" id="s1"></span></div>
            <div class="r"><span>Red Dot</span><span class="v" id="s2"></span></div>
            <div class="r"><span>Ống 2x</span><span class="v" id="s3"></span></div>
            <div class="r"><span>Ống 4x</span><span class="v" id="s4"></span></div>
            <div class="r"><span>AWM / Ống 8x</span><span class="v" id="s5"></span></div>
            <div class="r"><span>Nhìn tự do</span><span class="v" id="s6"></span></div>
        </div>
        <div class="gr"><h4>Cấu hình nâng cao hệ thống</h4>
            <div class="r"><span>Kích thước nút bắn</span><span class="d" id="b1"></span></div>
            <div class="r"><span>DPI đề xuất</span><span class="v" id="b2"></span></div>
            <div class="r"><span>Tốc độ con trỏ</span><span class="v" id="b3"></span></div>
        </div>
    </div>
    <button class="btn-red" onclick="location.href='/api/logout'">ĐĂNG XUẤT</button>
</div>
<script>
async function post(u,d){return(await fetch(u,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(d)})).json()}
async function login(){
    const k=document.getElementById("key").value.trim();
    if(!k) return alert("⚠️ Vui lòng nhập key");
    document.getElementById("l1").style.display="block";
    const r=await post("/api/auth",{key:k});
    document.getElementById("l1").style.display="none";
    if(!r.ok) return alert("❌ "+r.msg);
    if(r.role==="admin") document.getElementById("adminBtn").style.display="block";
    document.getElementById("u").innerText=r.user;
    document.getElementById("e").innerText=r.exp;
    document.getElementById("login").style.display="none";
    document.getElementById("main").style.display="block";
}
async function calc(){
    const dev=document.getElementById("dev").value.trim();
    if(!dev) return alert("⚠️ Nhập tên máy để phân tích cảm biến");
    document.getElementById("l2").style.display="block";
    const r=await post("/api/calc",{device:dev,weapon:document.getElementById("wp").value});
    document.getElementById("l2").style.display="none";
    if(!r.ok) return alert("❌ "+r.msg);
    const d=r.data;
    document.getElementById("s1").textContent=d.look_around;
    document.getElementById("s2").textContent=d.red_dot;
    document.getElementById("s3").textContent=d.scope2x;
    document.getElementById("s4").textContent=d.scope4x;
    document.getElementById("s5").textContent=d.awm;
    document.getElementById("s6").textContent=d.free_look;
    document.getElementById("b1").textContent=d.button_size+"%";
    document.getElementById("b2").textContent=d.dpi;
    document.getElementById("b3").textContent=d.pointer_speed+"%";
    document.getElementById("res").style.display="block";
}
</script></body></html>'''

ADMIN_HTML = r'''<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">
<title>⚙️ ADMIN · HƯNG ĐẸP TRAI VIP</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;600;700&display=swap');
body{background:#090a0f;color:#e6e6e6;font-family:'Rajdhani',sans-serif;padding:20px}
h1{color:#00f0ff;letter-spacing:1px}
a{color:#00f0ff}
.card{background:#12141d;border:1px solid #00f0ff33;padding:16px;border-radius:10px;margin:12px 0}
input,select{padding:9px 12px;background:#0008;border:1px solid #2a2a3a;color:#fff;border-radius:6px;margin-right:6px;font-family:Rajdhani}
button{padding:9px 16px;border:none;border-radius:6px;cursor:pointer;font-weight:700;font-family:Rajdhani;letter-spacing:.5px}
.b1{background:#00f0ff;color:#000}.bl{background:#ffaa00;color:#000}.bd{background:#ff0055;color:#fff}
table{width:100%;border-collapse:collapse;margin-top:12px;font-size:14px}
th,td{padding:9px 6px;border-bottom:1px solid #222;text-align:left}
.on{color:#0f0;font-weight:700}.off{color:#ff0055;font-weight:700}
.k{color:#00f0ff;font-weight:700}
</style></head><body>
<h1>⚙️ BẢNG ĐIỀU KHIỂN QUẢN LÝ ADMIN</h1>
<a href="/">← Về trang chính</a>
<div class="card">
    <h3>➕ TẠO KEY MỚI</h3>
    <input id="nu" placeholder="Tên người dùng">
    <input id="nd" type="number" min="1" value="7" style="width:90px">
    <span>ngày</span>
    <select id="rl"><option value="0">👤 USER</option><option value="1">🛡️ ADMIN</option></select>
    <button class="b1" onclick="add()">TẠO KEY NGAY</button>
    <div id="newk" style="margin-top:12px;color:#00f0ff;font-weight:700;font-size:16px"></div>
</div>
<div class="card">
    <h3>📋 DANH SÁCH TẤT CẢ KEY</h3>
    <table id="tb"></table>
</div>
<script>
async function api(u,d){return(await fetch(u,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(d||{})})).json()}
async function load(){
    const r=await fetch("/api/admin/keys").then(x=>x.json())
    const t=document.getElementById("tb")
    t.innerHTML=`<tr><th>ID</th><th>LICENSE KEY</th><th>TÊN</th><th>QUYỀN</th><th>HẾT HẠN</th><th>TRẠNG THÁI</th><th>HÀNH ĐỘNG</th></tr>`
    r.list.forEach(k=>{
        const tr=t.insertRow()
        tr.innerHTML=`<td>${k.id}</td><td class="k">${k.license_key}</td>
        <td>${k.username}</td><td>${k.role.toUpperCase()}</td><td>${k.expired_at}</td>
        <td class="${k.is_active?'on':'off'}">${k.is_active?'✅ HOẠT ĐỘNG':'🔒 BỊ KHOÁ'}</td>
        <td>
            <button class="bl" onclick="tg(${k.id})">${k.is_active?'KHÓA':'MỞ KHÓA'}</button>
            <button class="bd" onclick="del(${k.id})">XÓA</button>
        </td>`
    })
}
async function add(){
    const r=await api("/api/admin/add",{username:document.getElementById("nu").value,days:document.getElementById("nd").value,role:document.getElementById("rl").value})
    if(r.ok){document.getElementById("newk").innerText="✅ TẠO THÀNH CÔNG · KEY: "+r.key;load()}
    else alert("❌ "+r.msg)
}
async function tg(id){await api("/api/admin/toggle",{id});load()}
async function del(id){if(confirm("⚠️ XÓA VĨNH VIỄN KEY NÀY KHÔNG THỂ KHÔI PHỤC?")){await api("/api/admin/del",{id});load()}}
load()
</script></body></html>'''

# ---------------- CƠ SỞ DỮ LIỆU ----------------
def query(sql,args=(),one=False,commit=False):
    conn=sqlite3.connect(DB_PATH);conn.row_factory=sqlite3.Row;c=conn.cursor()
    c.execute(sql,args);res=c.fetchone() if one else c.fetchall()
    if commit: conn.commit()
    conn.close();return res

def init_db():
    conn=sqlite3.connect(DB_PATH);c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS `keys`(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        license_key TEXT UNIQUE NOT NULL,
        username TEXT NOT NULL,
        role TEXT DEFAULT 'user',
        duration_days INTEGER DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        expired_at TIMESTAMP NOT NULL,
        is_active INTEGER DEFAULT 1)''')
    conn.commit()
    if not c.execute("SELECT 1 FROM `keys` WHERE role='admin' LIMIT 1").fetchone():
        k="admin123456"
        exp=(datetime.now()+timedelta(days=3650)).strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO `keys`(license_key,username,role,duration_days,expired_at)VALUES(?,?,?,?,?)",
                  (k,"ADMIN CHÍNH HƯNG","admin",3650,exp))
        conn.commit()
        print("\n🛡️ ADMIN MẶC ĐỊNH ĐƯỢC TẠO:")
        print(f"🔑 KEY : {k}")
        print(f"👤 TÊN : ADMIN CHÍNH HƯNG\n")
    conn.close()

# ---------------- THUẬT TOÁN 100 TRIỆU TỔ HỢP ----------------
def sens_100trieu(device,weapon):
    device=device.strip().lower();weapon=weapon.strip().upper()
    SALT="HUNG|100TRIEU|SALT|v3.1|SENSITIVITY"
    h=hashlib.sha256(f"{device}|{weapon}|{SALT}".encode()).hexdigest()
    seed=0
    for ch in h: seed=(seed*16+int(ch,16))%(10**8+7)
    rnd=random.Random(seed)
    COEF={"ALL":(96,1.00),"ONETAP":(112,1.08),"SMG":(105,1.04),"AR":(88,0.96)}.get(weapon,(96,1.0))
    base,amp=COEF
    def g(lo,hi,bias=0):
        v=rnd.gauss(base+bias,18)*amp
        return max(lo,min(hi,round(v,1)))
    return {
        "look_around":g(75,190,0),
        "red_dot":g(85,198,6),
        "scope2x":g(78,192,-2),
        "scope4x":g(65,180,-12),
        "awm":g(55,160,-22),
        "free_look":g(70,185,-5),
        "button_size":round(rnd.uniform(42,62),1),
        "dpi":int(max(380,min(960,rnd.gauss(580,110)))),
        "pointer_speed":round(rnd.uniform(55,100),1)
    }

# ---------------- HÀM KIỂM TRA QUYỀN ----------------
def is_admin(): return session.get("role")=="admin"

# ---------------- ROUTE GIAO DIỆN ----------------
@app.route("/")
def idx(): return render_template_string(INDEX_HTML)

@app.route("/admin")
def adm():
    if not is_admin(): return redirect("/")
    return render_template_string(ADMIN_HTML)

# ---------------- API XÁC THỰC KEY ----------------
@app.route("/api/auth",methods=["POST"])
def auth():
    d=request.get_json(silent=True) or request.form
    k=str(d.get("key","")).strip()
    if not k: return jsonify({"ok":0,"msg":"Vui lòng nhập license key"})
    r=query("SELECT * FROM `keys` WHERE license_key=?",(k,),one=True)
    if not r: return jsonify({"ok":0,"msg":"Key không tồn tại trong hệ thống"})
    if r["is_active"]==0:
        return jsonify({"ok":0,"msg":"🔒 KEY BỊ KHOÁ. Ai nói bị tao khoá key r đấy cu 😎"})
    if datetime.strptime(r["expired_at"],"%Y-%m-%d %H:%M:%S")<datetime.now():
        return jsonify({"ok":0,"msg":"Key đã hết hạn sử dụng"})
    session["key"]=r["license_key"];session["role"]=r["role"]
    return jsonify({"ok":1,"user":r["username"],"exp":r["expired_at"],"role":r["role"]})

# ---------------- API TÍNH ĐỘ NHẠY ----------------
@app.route("/api/calc",methods=["POST"])
def calc():
    if "key" not in session: return jsonify({"ok":0,"msg":"Chưa kích hoạt key"})
    d=request.get_json(silent=True) or request.form
    dev=str(d.get("device","")).strip()
    wp=str(d.get("weapon","ALL")).strip()
    if not dev: return jsonify({"ok":0,"msg":"Nhập tên thiết bị"})
    return jsonify({"ok":1,"data":sens_100trieu(dev,wp)})

# ---------------- API QUẢN LÝ ADMIN ----------------
@app.route("/api/admin/keys")
def list_keys():
    if not is_admin(): return jsonify({"ok":0,"msg":"Cần quyền admin"})
    return jsonify({"ok":1,"list":[dict(x) for x in query("SELECT * FROM `keys` ORDER BY id DESC")]})

@app.route("/api/admin/add",methods=["POST"])
def add_key():
    if not is_admin(): return jsonify({"ok":0,"msg":"Cần quyền admin"})
    d=request.get_json(silent=True) or request.form
    key=d.get("key") or hashlib.md5(os.urandom(10)).hexdigest()[:12].upper()
    user=d.get("username","Khách VIP")
    days=max(1,int(d.get("days",1)))
    role="admin" if str(d.get("role","0"))=="1" else "user"
    exp=(datetime.now()+timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")
    try:
        query("INSERT INTO `keys`(license_key,username,role,duration_days,expired_at)VALUES(?,?,?,?,?)",
              (key,user,role,days,exp),commit=True)
        return jsonify({"ok":1,"key":key,"msg":"Thành công"})
    except: return jsonify({"ok":0,"msg":"Key này đã tồn tại"})

@app.route("/api/admin/toggle",methods=["POST"])
def toggle():
    if not is_admin(): return jsonify({"ok":0})
    i=request.json.get("id")
    st=query("SELECT is_active FROM `keys` WHERE id=?",(i,),one=True)
    new=0 if st["is_active"]==1 else 1
    query("UPDATE `keys` SET is_active=? WHERE id=?",(new,i),commit=True)
    return jsonify({"ok":1,"now":new})

@app.route("/api/admin/del",methods=["POST"])
def delete():
    if not is_admin(): return jsonify({"ok":0})
    query("DELETE FROM `keys` WHERE id=?",(request.json.get("id"),),commit=True)
    return jsonify({"ok":1})

@app.route("/api/logout")
def logout(): session.clear(); return redirect("/")

# ---------------- XỬ LÝ LỖI KHÔNG CHO TRẮNG 500 ----------------
@app.errorhandler(500)
def e500(e):
    import traceback
    return "<pre style='color:#ff3355;background:#000;padding:20px;font-size:13px;white-space:pre-wrap'>=== LỖI HỆ THỐNG ===\n"+traceback.format_exc()+"</pre>",500
@app.errorhandler(404)
def e404(e): return "❌ Đường dẫn không tồn tại",404

# ---------------- CHẠY MÁY CHỦ ----------------
if __name__=="__main__":
    init_db()
    print("="*50)
    print("🚀 HUNG DEP TRAI - VIP SENS 100 TRIỆU")
    print("📡 Đang chạy tại: http://127.0.0.1:8080")
    print("🌐 Mạng nội bộ : http://0.0.0.0:8080")
    print("="*50)
    app.run(host="0.0.0.0",port=8080,debug=False,threaded=True)
