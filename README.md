# Aplikasi Informasi dan Kalkulasi Harga Padi

Aplikasi ini dibuat menggunakan Python dan berbasis CLI (Command Line Interface) untuk membantu pengguna (admin dan anggota/member) dalam melakukan:

- Registrasi dan login akun
- Pengelolaan data harga padi, pupuk, dan pestisida
- Kalkulasi biaya pertanian dan estimasi keuntungan
- Manajemen data CSV secara langsung

## 📁 Struktur Folder

```
.
├── data_csv/
│   ├── list1_padi.csv
│   ├── pupuk_padi.csv
│   ├── pestisida_padi.csv
│   ├── hasil_kalkulasi.csv
│   ├── data_login.csv
│   └── admin_login.csv
├── data_txt/
│   ├── login_padi.txt
│   ├── menu_admin.txt
│   └── menu_member.txt
├── main.py
└── README.md
```

## 👤 Role Pengguna

1. **Admin**:
   - Login dari file `admin_login.csv`
   - Bisa mengelola harga padi, pupuk, dan pestisida
   - Dapat melihat hasil kalkulasi dan data akun member

2. **Member (Anggota)**:
   - Registrasi akun dan login
   - Dapat melihat harga dan melakukan kalkulasi keuntungan

## ✅ Fitur Utama

- Registrasi & login (admin/member)
- Menu interaktif berdasarkan peran pengguna
- CRUD data:
  - Jenis padi dan harga bibit
  - Pupuk dan pestisida
- Simulasi perhitungan biaya pertanian dan keuntungan
- Menyimpan dan menampilkan data dalam bentuk tabel menggunakan `tabulate`

## 💾 Teknologi & Library

- Python 3.x
- `pandas`
- `csv`
- `os`, `sys`, `getpass`
- `tabulate`

## ▶️ Menjalankan Program

1. Pastikan direktori `data_csv/` dan `data_txt/` sudah tersedia
2. Jalankan `main.py` dengan Python:
```bash
python main.py
```

## ⚠️ Catatan

- Data login admin hanya bisa dibuat manual melalui file CSV
- Password saat login dan registrasi tidak terlihat (menggunakan `getpass`)
- Semua perubahan data langsung disimpan ke file `.csv`


## 🗂️ Referensi File CSV

| File CSV | Deskripsi |
|----------|-----------|
| `list1_padi.csv` | Daftar jenis padi, harga bibit, musim, dan umur |
| `pupuk_padi.csv` | Daftar jenis pupuk berdasarkan jenis padi |
| `pestisida_padi.csv` | Daftar pestisida per jenis padi |
| `hasil_kalkulasi.csv` | Hasil kalkulasi biaya dan keuntungan |
| `data_login.csv` | Data akun anggota |
| `admin_login.csv` | Data akun admin |

---

Dikembangkan untuk kebutuhan sistem simulasi pengelolaan data harga dan kalkulasi hasil pertanian.
