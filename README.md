# 🚗 RENTCAR - Sistem Informasi Rental Mobil

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-6-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)

## 📖 Tentang Project

RENTCAR merupakan aplikasi rental mobil berbasis web yang dikembangkan menggunakan **Django Framework** sebagai tugas UAS Mata Kuliah Pemrograman Web.

Aplikasi ini memudahkan proses penyewaan mobil mulai dari pengelolaan data mobil, penyewaan, pembayaran, hingga pengembalian kendaraan.

---

## ✨ Fitur

### 👨‍💼 Administrator
- Dashboard Administrator
- CRUD Data Mobil
- Verifikasi Pelanggan
- Kelola Penyewaan
- Kelola Pembayaran
- Kelola Pengembalian
- Laporan Penyewaan

### 👨‍🔧 Petugas
- Dashboard Petugas
- Kelola Penyewaan
- Kelola Pengembalian
- Data Pembayaran

### 👤 Pelanggan
- Login
- Melihat Daftar Mobil
- Mengajukan Penyewaan
- Riwayat Penyewaan
- Pembayaran
- Status Pengembalian

---

## 🛠️ Teknologi

- Python
- Django
- Bootstrap 5
- HTML5
- CSS3
- JavaScript
- SQLite

---

## 📂 Struktur Project

```
rentcar/
│
├── administrator/
├── pelanggan/
├── petugas/
├── accounts/
├── templates/
├── static/
├── manage.py
└── README.md
```

---

## 🚀 Cara Menjalankan

Clone repository

```bash
git clone https://github.com/nadira-08/rental_mobil.git
```

Masuk ke folder project

```bash
cd rental_mobil
```

Install dependency

```bash
pip install -r requirements.txt
```

Migrasi database

```bash
python manage.py migrate
```

Menjalankan server

```bash
python manage.py runserver
```

Buka browser

```
http://127.0.0.1:8000/
```

---

## 📋 Fitur CRUD

| Modul | Create | Read | Update | Delete |
|--------|--------|------|--------|--------|
| Data Mobil | ✅ | ✅ | ✅ | ✅ |
| Penyewaan | ✅ | ✅ | ✅ | ✅ |
| Pembayaran | ✅ | ✅ | ✅ | ✅ |
| Pengembalian | ✅ | ✅ | ✅ | ✅ |
| Pelanggan | ✅ | ✅ | ✅ | ✅ |

---

## 👩‍💻 Developer

**Nadiratul Laili**

Program Studi Teknik Informatika

Universitas Nurul Jadid

---

## 📄 Lisensi

Project ini dibuat untuk keperluan pembelajaran dan penyelesaian tugas mata kuliah Pemrograman Web.
