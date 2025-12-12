Project ini adalah aplikasi CRUD (Create, Read, Update, Delete) sederhana menggunakan Flask, SQLAlchemy, dan MySQL. Aplikasi ini menyediakan REST API untuk mengelola data user seperti id, name, email, dan password (hashed).

🚀 Fitur Utama

Create user

Read semua user atau 1 user

Update user

Delete user

Response JSON standar

Menggunakan MySQL sebagai database

Struktur project terorganisir (MVC sederhana)

project/
│── app/
│   ├── __init__.py
│   ├── models/
│   │   └── user.py
│   ├── controller/
│   │   └── UserController.py
│   ├── response.py
│   └── config.py
│
│── migrations/   (otomatis setelah flask db init/migrate)
│── main.py
│── README.md

🛠 Persiapan Environment
1️⃣ Install Dependencies

Pastikan sudah menginstall library berikut:

pip install flask flask_sqlalchemy pymysql flask_migrate flask_cors

2️⃣ Buat Database MySQL

Masuk ke phpMyAdmin atau MySQL:

CREATE DATABASE crud_flask;

3️⃣ Setting config.py

Pastikan isi config sesuai database kamu:

class Config(object):
    HOST = "localhost"
    DATABASE = "crud_flask"
    USERNAME = "root"
    PASSWORD = ""

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"

🗄️ Migrasi Database

Jalankan:

flask db init
flask db migrate
flask db upgrade

▶️ Menjalankan Aplikasi

Jalankan:

python main.py


Server akan berjalan di:

http://127.0.0.1:5000

📡 Endpoint API
🔹 1. GET /users

Mengambil semua user.

Response:

{
  "status": 200,
  "data": [...],
  "message": ""
}

🔹 2. GET /users/<id>

Mengambil 1 user berdasarkan ID.

🔹 3. POST /users

Menambah user baru.

Body JSON:

{
  "name": "User Baru",
  "email": "user@email.com",
  "password": "12345"
}

🔹 4. PUT /users/<id>

Mengubah data user berdasarkan ID.

🔹 5. DELETE /users/<id>

Menghapus user berdasarkan ID.

✔️ Contoh Response JSON (Standar)
{
  "status": 200,
  "message": "Successfully update data!",
  "data": null
}

📘 Penjelasan Singkat Komponen

models/user.py → Struktur tabel user + hashing password

controller/UserController.py → Logika CRUD

response.py → Format response JSON standar

main.py → Daftar routing API

config.py → Konfigurasi database
