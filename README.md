# Flask Simple Mod Template

Template yang sengaja dirancang untuk pengembangan website penelitian IoT dengan kebutuhan pengkodean algoritma menggunakan bahasa pemrograman Python. 

Default template dashboard menggunakan <a href="https://zuramai.github.io/mazer/" target="_blank">Mazer</a>

Dokumentasi <a href="https://flask.palletsprojects.com/en/stable/" target="_blank">Flask</a>

## 🗂️ Struktur Folder

```
project_root/
├── app/
│   ├── __init__.py         # Inisialisasi Flask app, timezone, DB, dan Blueprint
│   ├── http_routes/        
|   |     |── api/          # Routing khusus API
|   |     |── web/          # Routing khusus Web
│   ├── models/             # Model database (SQLAlchemy)
│   ├── providers/          # Provider untuk register route dan extensions
│   ├── helpers.py          # Helpers yang berisi function bantuan
│   └── ...
├── config/                 # Konfigurasi database, logging, dan timezone
├── logs/                   # Folder logging app
├── static/                 
│   ├── css/                # Folder static assets css
│   └── ...
├── templates/              
│   ├── layouts/            # Folder layout html
│   ├── pages/              # Folder halaman-halaman html
│   └── ...
├── .env.example            # Contoh Variabel lingkungan
├── .gitignore              # File/folder yang diabaikan oleh Git
|── init.py                 # Kode inisialisasi User
├── requirements.txt        # Daftar dependensi Python
├── run.py                  # Entry point untuk menjalankan aplikasi
└── README.md               # Dokumentasi proyek ini
```

## ⚙️ Langkah-langkah Inisialisasi Proyek

### 1. Clone Repositori

```bash
git clone https://github.com/valentviktor/flask-mod-iot-template.git <nama-projek>
cd <nama-projek>
```

### 2. Buat dan Aktifkan Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Install Dependensi

```bash
pip install -r requirements.txt
```

### 4. Buat File `.env`

```bash
cp .env.example .env
```
atau anda dapat copy paste manual

Generate secret key

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```
Setelah itu copy paste ke APP_KEY pada file .env

Sesuaikan konfigurasi, contoh sebagai berikut:
```
APP_NAME="Flask Mod IoT"
APP_KEY=ghv2345uyg2f5u234
APP_DEBUG=True
APP_TIMEZONE=Asia/Jakarta

DB_CONNECTION=mysql
DB_HOST=localhost
DB_PORT=3306
DB_USERNAME=root
DB_PASSWORD=
DB_DATABASE=flask_mod_iot
```

### 5. Inisialisasi Database

```bash
flask init-db
flask seed
```

### 6. Jalankan Aplikasi

```bash
flask run
# or
python run.py      # hot reload
```

Akses aplikasi di [http://127.0.0.1:5000](http://127.0.0.1:5000) atau sesuai konfigurasi anda.


_Template ini hanya gambaran, karena flask tidak mempunyai aturan tetap, anda dapat mengubahnya sesuai keinginan anda_
