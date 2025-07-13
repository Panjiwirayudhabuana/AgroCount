import csv
import pandas as pd
from tabulate import tabulate
import os
from getpass import getpass
import sys



# fungsi registrasi member
def register_anggota():
    os.system("cls")
    username = input("masukkan username anda : ")
    password_check = False
    while password_check == False:
        password = getpass("masukkan password anda : ")
        password_confirm = getpass("**ulangi password anda : ")
        if password != password_confirm:
            print("pasword tidak sesuai!")
            password_check = False
        elif password == password_confirm:
            password_check = True

    data_regis = []
    with open("data_csv/data_login.csv", "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            data_regis.append({"username": row[0], "password": row[1]})

    username_already = False

    for regis in data_regis:
        if username == regis["username"]:
            print("Username sudah ada mohon ganti dengan yang lain !")
            username_already = True
            enter = input("klik enter untuk melanjutkan...")
            print(enter, menu_login())

    if username_already == False:
        new_data = {"username": username, "password": password}
        with open("data_csv/data_login.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=new_data.keys())
            writer.writerow(new_data)

        print("Data berhasil ditambahkan!")
        enter = input("klik enter untuk melanjutkan...")
        print(enter, menu_login())


# login admin
def login_admin():
    os.system("cls")
    username = input("masukkan username anda : ")
    password = getpass("masukkan password anda : ")

    data_regis = []
    with open("data_csv/admin_login.csv", "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            data_regis.append({"username": row[0], "password": row[1]})

    data_login = []
    for i in data_regis:
        if username == i["username"] and password == i["password"]:
            data_login.append(i)
            print("login berhasil")
            menu_fungsi_admin()

    if len(data_login) == 0:
        print("akun tidak ditemukan")
        input("Klik Enter Untuk Ulang...")
        menu_login()


# login member
def login_anggota():
    os.system("cls")
    username = input("masukkan username anda : ")
    password = getpass("masukkan password anda : ")

    data_regis = []
    with open("data_csv/data_login.csv", "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        for row in csv_reader:
            data_regis.append({"username": row[0], "password": row[1]})

    data_login = []
    for i in data_regis:
        if username == i["username"] and password == i["password"]:
            data_login.append(i)
            print("login berhasil")
            menu_fungsi_member()

    if len(data_login) == 0:
        print("akun tidak ditemukan")
        input("Klik Enter Untuk Ulang...")
        menu_login()


# menu login
def menu_login():
    os.system("cls")
    namafile = "data_txt/login_padi.txt"
    with open(namafile, "r") as file:
        isi_file = file.read()
        print(isi_file)

    opsi = int(input("masukkan pilihan : "))

    if opsi == 1:
        register_anggota()
    elif opsi == 2:
        login_anggota()
    elif opsi == 3:
        login_admin()
    else:
        print("Masukkan Pilihan yang tepat")


# menu fungsi pada admin
def menu_fungsi_admin():
    os.system("cls")
    namafile = "data_txt/menu_admin.txt"
    with open(namafile, "r") as file:
        isi_file = file.read()
        print(isi_file)

    while True:
        memilih = input("Pilih (1/2/3/4) : ")

        if memilih == "1":
            main()
            tampilkan_daftar_padi()
            tambah_harga_padi()
            edit_harga_padi()
            hapus_harga_padi()
            baca_dari_csv()
            simpan_ke_csv()
        elif memilih == "2":
            tampilkan_tabel_admin("data_csv/hasil_kalkulasi.csv")
        elif memilih == "3":
            tampilkan_tabel_member()
        elif memilih == "4":
            question = input("apakah anda yakin untuk keluar aplikasi ? (y/n):")
            if question == "y":
                os.system("cls")

                print("Terimakasih sudah menggunakan aplikasi kami.")
                sys.exit()
            elif question == "n":
                print("Melanjutkan aplikasi.")
            else:
                print("Masukkan pilihan yang tepat.")
        else:
            print("pilihan tidak ditemukan.")


# menu fungsi pada member
def menu_fungsi_member():
    os.system("cls")
    namafile = "data_txt/menu_member.txt"
    with open(namafile, "r") as file:
        isi_file = file.read()
        print(isi_file)

    while True:
        memilih = input("Pilih menu (1/2/3): ")

        if memilih == "1":
            main_tambah()
        elif memilih == "2":
            tampilkan_tabel("data_csv/hasil_kalkulasi.csv")
        elif memilih == "3":
            question = input("Apakah anda yakin untuk keluar aplikasi? (y/n): ")
            if question.lower() == "y":
                os.system("cls")

                print("Terimakasih sudah menggunakan aplikasi kami.")
                sys.exit()
            elif question.lower() == "n":
                print("Melanjutkan aplikasi.")
            else:
                print("Masukkan pilihan yang tepat.")
        else:
            print("Masukkan pilihan yang tersedia. Mohon masukkan opsi yang tepat.")


# ========================PADI======================
# menu fungsi informasi harga padi untuk admin
def main():
    os.system("cls")
    nama_berkas = "data_csv/list1_padi.csv"
    data_padi_df = baca_dari_csv(nama_berkas)
    tampilkan_daftar_padi(data_padi_df)

    print("Menu:")
    print("1. Tambah Jenis Padi dan Harga Bibit")
    print("2. Edit Harga Padi")
    print("3. Hapus Jenis Padi")
    print("4. Informasi Pupuk")
    print("5. Informasi pestisida")
    print("6. Kembali")

    while True:
        pilihan = input("Pilih menu (1/2/3/4/5/6): ")
        if pilihan == "1":
            jenis_padi = input("Masukkan jenis padi: ")
            if jenis_padi == "":
                print("Error: Jenis padi tidak boleh kosong!")
                break

            while True:
                try:
                    harga_bibit = float(input("Masukkan harga bibit: "))
                    break
                except ValueError:
                    print("Error: Harga bibit harus berupa angka.")

            while True:
                try:
                    potensi_hasil = float(input("Masukkan potensi hasil: "))
                    break
                except ValueError:
                    print("Error: Potensi hasil harus berupa angka.")
            musim = input("Masukkan musim: ")
            umur = input("Masukkan umur: ")
            data_padi_df = tambah_harga_padi(
                data_padi_df, jenis_padi, harga_bibit, potensi_hasil, musim, umur
            )
            simpan_ke_csv(data_padi_df, nama_berkas)
            main()

        elif pilihan == "2":
            jenis_padi = input("Masukkan jenis padi yang ingin diedit: ")
            while True:
                try:
                    harga_bibit = float(input("Masukkan harga bibit baru : "))
                    break
                except ValueError:
                    print("Error: Harga bibit harus berupa angka.")

            while True:
                try:
                    potensi_hasil = float(input("Masukkan potensi hasil baru: "))
                    break
                except ValueError:
                    print("Error: Potensi hasil harus berupa angka.")
            musim = input("Masukkan musim baru: ")
            umur = input("Masukkan umur baru: ")
            data_padi_df = edit_harga_padi(
                data_padi_df, jenis_padi, harga_bibit, potensi_hasil, musim, umur
            )
            simpan_ke_csv(data_padi_df, nama_berkas)
            print("Data telah diedit")
            input("Klik enter untuk melanjutkan...")
            main()
        elif pilihan == "3":
            jenis_padi = input("Masukkan jenis padi yang ingin dihapus: ")
            data_padi_df = hapus_harga_padi(data_padi_df, jenis_padi)
            simpan_ke_csv(data_padi_df, nama_berkas)
            print("Data telah dihapus")
            input("Klik enter unutk melanjutkan...")
            main()
        elif pilihan == "4":
            main_pupuk()
            tampilkan_daftar_pupuk()
            tambah_harga_pupuk()
            edit_harga_pupuk()
            hapus_harga_pupuk()
            baca_dari_csv_pupuk()
            simpan_ke_csv_pupuk()
        elif pilihan == "5":
            main_pestisida()
            tampilkan_daftar_pestisida()
            tambah_harga_pestisida()
            edit_harga_pestisida()
            hapus_harga_pestisida()
            baca_dari_csv_pestisida()
            simpan_ke_csv_pestisida()
        elif pilihan == "6":
            menu_fungsi_admin()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# menu informasi harga padi untuk member
def main_tambah():
    os.system("cls")
    nama_berkas = "data_csv/list1_padi.csv"
    data_padi_df = baca_dari_csv(nama_berkas)

    tampilkan_daftar_padi(data_padi_df)
    print("1. Informasi Pupuk")
    print("2. Informasi Pestisida")
    print("3. Kembali")

    while True:
        memilih = input("masukkan pilihan : ")
        if memilih == "1":
            main_pupuk_tambah()
        elif memilih == "2":
            main_pestisida_tambah()
        elif memilih == "3":
            menu_fungsi_member()
        else:
            print("Masukkan pilihan yang tepat")


# membaca data yang ada di csv
def baca_dari_csv(nama_berkas):
    os.system("cls")
    try:
        df = pd.read_csv(nama_berkas)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        df = pd.DataFrame(
            columns=["Jenis Padi", "Harga Bibit", "Potensi Hasil", "Musim", "Umur"]
        )
    return df


def tampilkan_daftar_padi(df):
    os.system("cls")

    # Menambah kolom 'Nomor' jika belum ada
    if "Nomor" not in df.columns:
        df.insert(0, "Nomor", range(1, len(df) + 1))

    df["Potensi Hasil"] = df["Potensi Hasil"].apply(
        lambda x: f"{x} (kg)" if "kg" not in str(x) else x
    )
    print("Daftar Harga Padi:")
    print(tabulate(df, headers="keys", tablefmt="pretty", showindex=False))


# Fungsi lainnya
def tambah_harga_padi(df, jenis_padi, harga_bibit, potensi_hasil, musim, umur):
    os.system("cls")
    if jenis_padi in df["Jenis Padi"].values:
        print(f"{jenis_padi} sudah ada dalam daftar harga padi.")
        input("klik enter untuk mengulang...")
        main()
    else:
        nomor_baru = len(df) + 1  # Nomor baru
        new_data = {
            "Nomor": nomor_baru,
            "Jenis Padi": jenis_padi,
            "Harga Bibit": harga_bibit,
            "Potensi Hasil": potensi_hasil,
            "Musim": musim,
            "Umur": umur,
        }
        df = pd.concat([df, pd.DataFrame(new_data, index=[0])], ignore_index=True)
        print(
            f"{jenis_padi} berhasil ditambahkan ke dalam daftar harga padi dengan nomor {nomor_baru}."
        )
        input("klik enter untuk melanjutkan...")

    return df


def edit_harga_padi(df, jenis_padi, harga_bibit, potensi_hasil, musim, umur):
    os.system("cls")
    if jenis_padi in df["Jenis Padi"].values:
        df.loc[
            df["Jenis Padi"] == jenis_padi,
            ["Nomor", "Harga Bibit", "Potensi Hasil", "Musim", "Umur"],
        ] = [
            df[df["Jenis Padi"] == jenis_padi],
            harga_bibit,
            potensi_hasil,
            musim,
            umur,
        ]
    else:
        print(f"{jenis_padi} tidak ditemukan dalam daftar harga padi.")
    return df


def hapus_harga_padi(df, jenis_padi):
    os.system("cls")
    if jenis_padi in df["Jenis Padi"].values:
        nomor_hapus = df[df["Jenis Padi"] == jenis_padi]["Nomor"].values[0]
        df = df[df["Jenis Padi"] != jenis_padi]
        df.reset_index(drop=True, inplace=True)
        # Update kolom 'Nomor' setelah penghapusan
        df["Nomor"] = range(1, len(df) + 1)
        print(f"{jenis_padi} dengan nomor {nomor_hapus} telah dihapus.")
    else:
        print(f"{jenis_padi} tidak ditemukan dalam daftar harga padi.")
    return df


2


# fungsi simpan data ke dalam csv
def simpan_ke_csv(df, nama_berkas):
    os.system("cls")
    df.to_csv(nama_berkas, index=False)


# PUPUK
########################################################################################################
def baca_dari_csv_pupuk(nama_file):
    os.system("cls")
    try:
        df = pd.read_csv(nama_file)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        df = pd.DataFrame(columns=["Jenis Padi", "Pupuk", "Harga Pupuk"])
    return df


# menampilkan tabel
def tampilkan_daftar_pupuk(df):
    os.system("cls")

    # Menambah kolom 'Nomor' jika belum ada
    if "Nomor" not in df.columns:
        df.insert(0, "Nomor", range(1, len(df) + 1))

    print("Daftar Harga Pupuk:")
    print(tabulate(df, headers="keys", tablefmt="pretty", showindex=False))


def tambah_harga_pupuk(df, padi, pupuk, harga_pupuk):
    os.system("cls")
    if padi in df["Jenis Padi"].values:
        print(f"{padi} sudah ada dalam tabel, masukkan jenis padi yang berbeda.")
        input("Klik enter untuk mengulang...")
        main_pupuk()
    else:
        nomor_baru = len(df) + 1  # Nomor baru
        new_data = {
            "Nomor": nomor_baru,
            "Jenis Padi": padi,
            "Pupuk": pupuk,
            "Harga Pupuk": harga_pupuk,
        }
        df = pd.concat([df, pd.DataFrame(new_data, index=[0])], ignore_index=True)
        print(
            f"{padi} berhasil ditambahkan ke dalam daftar harga pupuk dengan nomor {nomor_baru}."
        )
        input("Klik enter untuk melanjutkan")

    return df


def edit_harga_pupuk(df, padi, pupuk, harga_pupuk):
    os.system("cls")
    if padi in df["Jenis Padi"].values:
        df.loc[
            df["Jenis Padi"] == padi,
            ["Pupuk", "Harga Pupuk"],
        ] = [pupuk, harga_pupuk]
    else:
        print(f"{padi} tidak ditemukan dalam daftar harga pupuk.")
    return df


def hapus_harga_pupuk(df, padi):
    os.system("cls")
    if padi in df["Jenis Padi"].values:
        df = df[df["Jenis Padi"] != padi]
        df.reset_index(drop=True, inplace=True)
        # Update kolom 'Nomor' setelah penghapusan
        df["Nomor"] = range(1, len(df) + 1)
    else:
        print(f"{padi} tidak ditemukan dalam daftar harga pupuk.")
    return df


# fungsi simpan data ke dalam csv
def simpan_ke_csv_pupuk(df, nama_file):
    os.system("cls")
    df.to_csv(nama_file, index=False)


# menu fungsi informasi untuk admin
def main_pupuk():
    os.system("cls")
    nama_file = "data_csv/pupuk_padi.csv"
    data_pupuk_df = baca_dari_csv_pupuk(nama_file)
    tampilkan_daftar_pupuk(data_pupuk_df)

    print("Menu:")
    print("1. Tambah Jenis Padi, Pupuk dan Harga Pupuk")
    print("2. Edit Harga Pupuk")
    print("3. Hapus Jenis Pupuk")
    print("4. Kembali")

    while True:
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            padi = input("Masukkan jenis padi: ")
            pupuk = input("Masukkan pupuk: ")
            while True:
                try:
                    harga_pupuk = float(input("Masukkan harga pupuk : "))
                    break
                except ValueError:
                    print("Error: Harga pestisida harus berupa angka.")
            data_pupuk_df = tambah_harga_pupuk(data_pupuk_df, padi, pupuk, harga_pupuk)
            simpan_ke_csv_pupuk(data_pupuk_df, nama_file)
            main_pupuk()

        elif pilihan == "2":
            padi = input("Masukkan jenis padi yang ingin diedit: ")
            pupuk = input("Masukkan pupuk baru: ")
            while True:
                try:
                    harga_pupuk = float(input("Masukkan harga pupuk baru : "))
                    break
                except ValueError:
                    print("Error: Harga pestisida harus berupa angka.")
            data_pupuk_df = edit_harga_pupuk(data_pupuk_df, padi, pupuk, harga_pupuk)
            simpan_ke_csv_pupuk(data_pupuk_df, nama_file)
            print("Data telah diedit")
            input("Klik enter untuk melanjutkan")
            main_pupuk()
        elif pilihan == "3":
            padi = input("Masukkan jenis padi yang ingin dihapus: ")
            data_pupuk_df = hapus_harga_pupuk(data_pupuk_df, padi)
            simpan_ke_csv_pupuk(data_pupuk_df, nama_file)
            print("Data telah terhapus")
            input("Klik enter untuk melanjutkan")
            main_pupuk()
        elif pilihan == "4":
            main()
            tampilkan_daftar_padi()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# fungsi informasi untuk member
def main_pupuk_tambah():
    os.system("cls")
    nama_file = "data_csv/pupuk_padi.csv"

    data_pupuk_df = baca_dari_csv_pupuk(nama_file)

    tampilkan_daftar_pupuk(data_pupuk_df)

    print("Menu:")
    print("1. Kembali")
    while True:
        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            main_tambah()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# PESTISIDA
##############################################################################################################
def baca_dari_csv_pestisida(nama_file):
    os.system("cls")
    try:
        df = pd.read_csv(nama_file)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        df = pd.DataFrame(columns=["Jenis Padi", "Pestisida", "Harga Pestisida"])
    return df


# menampilkan tabel pestisida
def tampilkan_daftar_pestisida(df):
    os.system("cls")

    # Menambah kolom 'Nomor' jika belum ada
    if "Nomor" not in df.columns:
        df.insert(0, "Nomor", range(1, len(df) + 1))

    print("Daftar Harga Pestisida : ")
    print(tabulate(df, headers="keys", tablefmt="pretty", showindex=False))


def tambah_harga_pestisida(df, padi, pestisida, harga_pestisida):
    os.system("cls")
    if padi in df["Jenis Padi"].values:
        print(f"{padi} sudah ada dalam daftar harga pestisida.")
        input("Klik enter untuk mengulang...")
        main_pestisida()
    else:
        new_data = {
            "Nomor": len(df) + 1,  # Nomor baru
            "Jenis Padi": padi,
            "Pestisida": pestisida,
            "Harga Pestisida": harga_pestisida,
        }
        df = pd.concat([df, pd.DataFrame(new_data, index=[0])], ignore_index=True)
        print(f"{padi} berhasil ditambahkan ke dalam daftar harga pestisida.")
        input("Klik enter untuk melanjutkan")
    return df


def edit_harga_pestisida(df, padi, pestisida, harga_pestisida):
    os.system("cls")
    if padi in df["Jenis Padi"].values:
        df.loc[
            df["Jenis Padi"] == padi,
            ["Nomor", "Pestisida", "Harga Pestisida"],
        ] = [df[df["Jenis Padi"] == padi].index[0] + 1, pestisida, harga_pestisida]
    else:
        print(f"{padi} tidak ditemukan dalam daftar harga pestisida.")
    return df


def hapus_harga_pestisida(df, padi):
    os.system("cls")
    if padi in df["Jenis Padi"].values:
        df = df[df["Jenis Padi"] != padi]
        df.reset_index(drop=True, inplace=True)
        # Update kolom 'Nomor' setelah penghapusan
        df["Nomor"] = range(1, len(df) + 1)
    else:
        print(f"{padi} tidak ditemukan dalam daftar harga pestisida.")
    return df


# fungsi simpan data ke dalam csv
def simpan_ke_csv_pestisida(df, nama_file):
    os.system("cls")
    df.to_csv(nama_file, index=False)


# menu fungsi informasi untuk admin
def main_pestisida():
    os.system("cls")
    nama_file = "data_csv/pestisida_padi.csv"

    data_pestisida_df = baca_dari_csv_pestisida(nama_file)

    tampilkan_daftar_pestisida(data_pestisida_df)

    print("Menu:")
    print("1. Tambah Jenis Padi dan Harga Bibit")
    print("2. Edit Harga Pestisida")
    print("3. Hapus Jenis Pestisida")
    print("4. Kembali")
    for _ in range(5):
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            padi = input("Masukkan jenis padi: ")
            pestisida = input("Masukkan pestisida : ")
            while True:
                try:
                    harga_pestisida = float(input("Masukkan harga pestisida : "))
                    break
                except ValueError:
                    print("Error: Harga pestisida harus berupa angka.")
            data_pestisida_df = tambah_harga_pestisida(
                data_pestisida_df, padi, pestisida, harga_pestisida
            )
            simpan_ke_csv_pestisida(data_pestisida_df, nama_file)
            main_pestisida()
        elif pilihan == "2":
            padi = input("Masukkan jenis padi yang ingin diedit : ")
            pestisida = input("Masukkan pestisida baru: ")
            while True:
                try:
                    harga_pestisida = float(input("Masukkan harga pestisida : "))
                    break
                except ValueError:
                    print("Error: Harga pestisida harus berupa angka.")
            data_pestisida_df = edit_harga_pestisida(
                data_pestisida_df, padi, pestisida, harga_pestisida
            )
            simpan_ke_csv_pestisida(data_pestisida_df, nama_file)
            print("data telah diedit")
            input("Klik enter untuk melanjutkan")
            main_pestisida()
        elif pilihan == "3":
            padi = input("Masukkan jenis padi yang ingin dihapus : ")
            data_pestisida_df = hapus_harga_pupuk(data_pestisida_df, padi)
            simpan_ke_csv_pestisida(data_pestisida_df, nama_file)
            print("data telah dihapus")
            input("Klik enter untuk melanjutkan...")
            main_pestisida()
        elif pilihan == "4":
            main()
            tampilkan_daftar_padi()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# fungsi informasi untuk member
def main_pestisida_tambah():
    os.system("cls")
    nama_file = "data_csv/pestisida_padi.csv"

    data_pestisida_df = baca_dari_csv_pestisida(nama_file)

    tampilkan_daftar_pestisida(data_pestisida_df)

    print("Menu:")
    print("1. Kembali")
    while True:
        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            main_tambah()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# KALKULASI
# ==================================================================================================================
# fungsi menyimpan data kalkulasi
def simpan_hasil_kalkulasi(
    jenis_padi,
    jumlah_bibit,
    jumlah_pupuk,
    jumlah_pestisida,
    biaya_sdm,
    total_harga,
    harga_jual,
    keuntungan,
    nama_file,
):
    os.system("cls")
    header_exist = os.path.exists(nama_file)

    with open(nama_file, "a", newline="") as file:
        # Menambah header jika file masih kosong
        if not header_exist:
            file.write(
                "Jenis Padi,Jumlah Bibit,Jumlah Pupuk,Jumlah Pestisida,Biaya SDM,Total Harga,Harga Jual,Keuntungan\n"
            )

        # Menulis data ke file CSV
        file.write(
            f"{jenis_padi},{jumlah_bibit},{jumlah_pupuk},{jumlah_pestisida},{biaya_sdm},{total_harga},{harga_jual},{keuntungan}\n"
        )


# fungsi menghitung total
def kalkulasi_total(
    data_padi_df,
    data_pupuk_df,
    data_pestisida_df,
    jenis_padi,
    jumlah_bibit,
    jumlah_pupuk,
    jumlah_pestisida,
    biaya_sdm,
):
    os.system("cls")
    if jenis_padi in data_padi_df["Jenis Padi"].values:
        harga_bibit = data_padi_df[data_padi_df["Jenis Padi"] == jenis_padi][
            "Harga Bibit"
        ].values[0]

        if jenis_padi in data_pupuk_df["Jenis Padi"].values:
            harga_pupuk = data_pupuk_df[data_pupuk_df["Jenis Padi"] == jenis_padi][
                "Harga Pupuk"
            ].values[0]
        else:
            harga_pupuk = 0

        if jenis_padi in data_pestisida_df["Jenis Padi"].values:
            harga_pestisida = data_pestisida_df[
                data_pestisida_df["Jenis Padi"] == jenis_padi
            ]["Harga Pestisida"].values[0]
        else:
            harga_pestisida = 0

        total_bibit = harga_bibit * jumlah_bibit
        total_pupuk = harga_pupuk * jumlah_pupuk
        total_pestisida = harga_pestisida * jumlah_pestisida
        total_biaya_sdm = biaya_sdm

        total_harga = total_bibit + total_pupuk + total_pestisida + total_biaya_sdm

        return total_harga
    else:
        print(f"{jenis_padi} tidak ditemukan dalam daftar harga padi.")
        return None


# fungsi menghitung keuntungan
def main_kalkulasi():
    os.system("cls")
    data_padi_df = pd.read_csv("data_csv/list1_padi.csv")
    data_pupuk_df = pd.read_csv("data_csv/pupuk_padi.csv")
    data_pestisida_df = pd.read_csv("data_csv/pestisida_padi.csv")

    jenis_padi = input("Masukkan jenis padi: ")
    while True:
        try:
            jumlah_bibit = int(input("Masukkan jumlah bibit: "))
            break
        except ValueError:
            print("Error: Jumlah bibit harus berupa angka")
    while True:
        try:
            jumlah_pupuk = int(input("Masukkan jumlah pupuk: "))
            break
        except ValueError:
            print("Error: Jumlah pupuk harus berupa angka")
    while True:
        try:
            jumlah_pestisida = int(input("Masukkan jumlah pestisida: "))
            break
        except ValueError:
            print("Error: Jumlah pestisida harus berupa angka")
    while True:
        try:
            biaya_sdm = float(input("Masukkan biaya SDM: "))
            break
        except ValueError:
            print("Error: Biaya SDM harus berupa angka")

    total_harga = kalkulasi_total(
        data_padi_df,
        data_pupuk_df,
        data_pestisida_df,
        jenis_padi,
        jumlah_bibit,
        jumlah_pupuk,
        jumlah_pestisida,
        biaya_sdm,
    )

    if total_harga is not None:
        print(f"Total Harga: {total_harga}")
        while True:
            try:
                harga_jual = float(input("Masukkan harga jual: "))
                break
            except ValueError:
                print("Error: Harga jual harus berupa angka")

        keuntungan = harga_jual - total_harga
        print(f"Keuntungan: {keuntungan}")

        simpan_hasil_kalkulasi(
            jenis_padi,
            jumlah_bibit,
            jumlah_pupuk,
            jumlah_pestisida,
            biaya_sdm,
            total_harga,
            harga_jual,
            keuntungan,
            "data_csv/hasil_kalkulasi.csv",
        )
    tampilkan_tabel_admin("data_csv/hasil_kalkulasi.csv")


# Tampilkan tabel dengan nomor indeks untuk member
def tampilkan_tabel(nama_file):
    os.system("cls")
    try:
        df = pd.read_csv(nama_file)
        if not df.empty:
            # Menambah kolom 'Nomor' jika belum ada
            if "Nomor" not in df.columns:
                df.insert(0, "Nomor", range(1, len(df) + 1))
            print(tabulate(df, headers="keys", tablefmt="pretty", showindex=False))
        else:
            print(f"File {nama_file} kosong.")
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")

    print("1. Kembali")
    memilih = input("Pilih opsi : ")
    if memilih == "1":
        menu_fungsi_member()
    else:
        tampilkan_tabel(nama_file)


# Tampilkan tabel dengan nomor indeks untuk admin
def tampilkan_tabel_admin(nama_file):
    os.system("cls")
    try:
        df = pd.read_csv(nama_file)
        if not df.empty:
            # Menambah kolom 'Nomor' jika belum ada
            if "Nomor" not in df.columns:
                df.insert(0, "Nomor", range(1, len(df) + 1))
            print(tabulate(df, headers="keys", tablefmt="pretty", showindex=False))
        else:
            print(f"File {nama_file} kosong.")
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")

    print("1. Mulai kalkulasi ")
    print("2. Kembali")
    memilih = input("Pilih opsi : ")
    if memilih == "1":
        main_kalkulasi()
    elif memilih == "2":
        menu_fungsi_admin()
    else:
        print("Opsi tidak ditemukan")
        input("Klik enter untuk memilih ulang...")
        tampilkan_tabel_admin(nama_file)


# ================fungsi hapus member===================
# tabel data akun member
# Tampilkan tabel member dengan nomor indeks di paling kiri
def tampilkan_tabel_member():
    os.system("cls")
    df = pd.read_csv("data_csv/data_login.csv")
    if not df.empty:
        # Menambah kolom 'Nomor' jika belum ada
        if "Nomor" not in df.columns:
            df.insert(0, "Nomor", range(1, len(df) + 1))
        print("Tabel Keseluruhan:")
        print(tabulate(df, headers="keys", tablefmt="pretty", showindex=False))
    else:
        print("Data member kosong.")
    menu_tabel_member()


# fungsi tambah data akun member
def tambah_member(username, password):
    os.system("cls")
    df = pd.read_csv("data_csv/data_login.csv")
    if username in df["username"].values:
        print(f"Username {username} sudah terdaftar. Masukkan username yang berbeda.")
        input("Klik enter untuk mengulang...")
        tampilkan_tabel_member()
    else:
        new_member = pd.DataFrame({"username": [username], "password": [password]})
        df = pd.concat([df, new_member], ignore_index=True)
        df.to_csv("data_csv/data_login.csv", index=False)
        print(f"Akun dengan username {username} berhasil ditambahkan.")
        input("Klik enter untuk melanjutkan...")


# fungsi hapus data akun member
def hapus_member(username):
    os.system("cls")
    df = pd.read_csv("data_csv/data_login.csv")
    if "username" in df.columns:
        df = df[df["username"] != username]
        df.to_csv("data_csv/data_login.csv", index=False)
    else:
        print("Tidak ditemukan.")


# menu pada data member
def menu_tabel_member():
    print("1. Tambah Member")
    print("2. Hapus Member")
    print("3. Kembali")
    memilih = input("pilih opsi : ")
    while True:
        if memilih == "1":
            username = input("masukan username:")
            password = input("masukan password:")
            tambah_member(username, password)
            tampilkan_tabel_member()
            break
        elif memilih == "2":
            username = input("masukan username yang ingin dihapus:")
            hapus_member(username)
            tampilkan_tabel_member()
            break
        elif memilih == "3":
            menu_fungsi_admin()
        else:
            print("Opsi tidak ditemukan")
            input("Tekan Enter Untuk Mengulang...")
            tampilkan_tabel_member()
            menu_tabel_member()


menu_login()


# memilih = int(input("pilih opsi:"))
# while True:
#     if memilih=="1":
#         print("kodingan berhasil")
#     elif memilih =="2":
#         print("kodingan berjalan")
#     else:
#         print("ulang kodingan")
